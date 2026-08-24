from AlgorithmImports import *
from datetime import datetime
import statistics
import random


class M62P2CatalystOutcomeExtraction(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2020, 10, 1)
        self.set_end_date(2025, 8, 1)
        self.set_cash(100000)
        self.set_time_zone(TimeZones.NEW_YORK)

        self.primary_cost = 0.0025
        self.events = [
            ('E1-ALNY-20240624','E1','ALNY',2024,6,24,10,0),
            ('E1-CYTK-20231227','E1','CYTK',2023,12,27,10,0),
            ('E1-MDGL-20221219','E1','MDGL',2022,12,19,10,0),
            ('E1-LLY-20230503','E1','LLY',2023,5,3,10,0),
            ('E1-BIIB-20220927','E1','BIIB',2022,9,28,10,0),
            ('E1-REGN-20230323','E1','REGN',2023,3,23,10,0),
            ('E1-VRTX-20240130','E1','VRTX',2024,1,30,10,0),
            ('E1-GILD-20240620','E1','GILD',2024,6,20,10,0),
            ('E1-BMY-20240926','E1','BMY',2024,9,27,10,0),
            ('E1-PFE-20230531','E1','PFE',2023,6,1,10,0),
            ('E2-NVDA-20230524','E2','NVDA',2023,5,25,10,0),
            ('E2-META-20230426','E2','META',2023,4,27,10,0),
            ('E2-FDX-20220915','E2','FDX',2022,9,16,10,0),
            ('E2-WMT-20220725','E2','WMT',2022,7,26,10,0),
            ('E2-AAPL-20230504','E2','AAPL',2023,5,5,10,0),
            ('E2-MSFT-20230425','E2','MSFT',2023,4,26,10,0),
            ('E2-AMZN-20230427','E2','AMZN',2023,4,28,10,0),
            ('E2-GOOGL-20230425','E2','GOOGL',2023,4,26,10,0),
            ('E2-NFLX-20230119','E2','NFLX',2023,1,20,10,0),
            ('E2-TSLA-20230125','E2','TSLA',2023,1,26,10,0),
            ('E2-ARM-20240207','E2','ARM',2024,2,8,10,0),
            ('E3-PLTR-20211005','E3','PLTR',2021,10,6,10,0),
            ('E3-AVAV-20240828','E3','AVAV',2024,8,28,11,30),
            ('E3-CEG-20240920','E3','CEG',2024,9,20,10,0),
            ('E3-MP-20250710','E3','MP',2025,7,10,10,0),
            ('E3-INTC-20240320','E3','INTC',2024,3,20,10,0),
            ('E3-MU-20240425','E3','MU',2024,4,25,10,0),
            ('E3-TSM-20240408','E3','TSM',2024,4,8,10,0),
            ('E3-MSFT-20240508','E3','MSFT',2024,5,8,10,0),
            ('E3-AMZN-20240425','E3','AMZN',2024,4,25,10,0),
            ('E4-GE-20211109','E4','GE',2021,11,9,10,0),
            ('E4-JNJ-20211112','E4','JNJ',2021,11,12,10,0),
            ('E4-IBM-20201008','E4','IBM',2020,10,8,10,0),
            ('E4-K-20220621','E4','K',2022,6,21,10,0),
            ('E4-NVDA-20240318','E4','NVDA',2024,3,19,10,0),
            ('E4-AMD-20231206','E4','AMD',2023,12,7,10,0),
            ('E4-ORCL-20250121','E4','ORCL',2025,1,22,10,0),
            ('E4-F-20220302','E4','F',2022,3,2,10,0),
            ('E4-AAPL-20230605','E4','AAPL',2023,6,6,10,0),
            ('E5-ATVI-20220118','E5','ATVI',2022,1,18,10,0),
            ('E5-HES-20231023','E5','HES',2023,10,23,10,0),
            ('E5-PXD-20231011','E5','PXD',2023,10,11,10,0),
            ('E5-TWTR-20220425','E5','TWTR',2022,4,25,15,20),
            ('E5-DRE-20220613','E5','DRE',2022,6,13,10,0),
            ('E5-DFS-20240219','E5','DFS',2024,2,20,10,0),
            ('E5-ACI-20221014','E5','ACI',2022,10,14,10,0),
        ]

        self.symbols = {}
        self.ticker_by_symbol = {}
        tickers = sorted(set(x[2] for x in self.events))
        for ticker in tickers:
            sec = self.add_equity(ticker, Resolution.MINUTE, fill_forward=False, extended_market_hours=False)
            sec.set_data_normalization_mode(DataNormalizationMode.RAW)
            self.symbols[ticker] = sec.symbol
            self.ticker_by_symbol[sec.symbol] = ticker
        spy = self.add_equity('SPY', Resolution.MINUTE, fill_forward=False, extended_market_hours=False)
        spy.set_data_normalization_mode(DataNormalizationMode.RAW)
        self.spy = spy.symbol

        self.rows = {}
        self.events_by_date = {}
        for event_id, cat, ticker, y, m, d, hh, mm in self.events:
            decision = datetime(y, m, d, hh, mm)
            self.rows[event_id] = {
                'id': event_id, 'cat': cat, 'ticker': ticker, 'decision': decision,
                'entered': False, 'complete': False, 'failed': False,
                'entry': None, 'entry_time': None, 'entry_date': None,
                'prior': None, 'shock': None, 'dir': 0, 'delay': None,
                'spy_entry': None, 'sessions_after': 0,
                'mfe': 0.0, 'mae': 0.0, 'h': {}
            }
            self.events_by_date.setdefault(decision.date(), []).append(event_id)

        self.last_bar_date = {}
        self.last_close = {}
        self.prior_session_close = {}
        self.current_global_date = None

    def on_data(self, data):
        now = self.time
        today = now.date()
        if self.current_global_date is None:
            self.current_global_date = today
        elif today != self.current_global_date:
            self.finalize_market_day(self.current_global_date)
            self.current_global_date = today

        for symbol, bar in data.bars.items():
            if symbol == self.spy:
                key = 'SPY'
            elif symbol in self.ticker_by_symbol:
                key = self.ticker_by_symbol[symbol]
            else:
                continue
            bdate = bar.end_time.date()
            if key in self.last_bar_date and self.last_bar_date[key] != bdate:
                self.prior_session_close[key] = self.last_close[key]
            self.last_bar_date[key] = bdate
            self.last_close[key] = float(bar.close)

        for event_id in self.events_by_date.get(today, []):
            r = self.rows[event_id]
            if r['entered'] or now < r['decision']:
                continue
            symbol = self.symbols[r['ticker']]
            if symbol not in data.bars:
                continue
            bar = data.bars[symbol]
            if bar.end_time < r['decision']:
                continue
            prior = self.prior_session_close.get(r['ticker'])
            if prior is None or prior <= 0:
                r['failed'] = True
                continue
            r['entered'] = True
            r['entry'] = float(bar.close)
            r['entry_time'] = bar.end_time
            r['entry_date'] = bar.end_time.date()
            r['prior'] = float(prior)
            r['shock'] = r['entry'] / r['prior'] - 1.0
            r['dir'] = 1 if r['shock'] > 0 else (-1 if r['shock'] < 0 else 0)
            r['delay'] = max(0.0, (r['entry_time'] - r['decision']).total_seconds() / 60.0)
            if self.spy in data.bars and data.bars[self.spy].end_time >= r['entry_time']:
                r['spy_entry'] = float(data.bars[self.spy].close)

        if self.spy in data.bars:
            spy_bar = data.bars[self.spy]
            for r in self.rows.values():
                if r['entered'] and not r['complete'] and not r['failed'] and r['spy_entry'] is None:
                    if spy_bar.end_time >= r['entry_time']:
                        r['spy_entry'] = float(spy_bar.close)

        for r in self.rows.values():
            if not r['entered'] or r['complete'] or r['failed'] or r['dir'] == 0:
                continue
            symbol = self.symbols[r['ticker']]
            if symbol not in data.bars:
                continue
            bar = data.bars[symbol]
            if bar.end_time <= r['entry_time']:
                continue
            if r['dir'] > 0:
                favorable = float(bar.high) / r['entry'] - 1.0
                adverse = float(bar.low) / r['entry'] - 1.0
            else:
                favorable = -(float(bar.low) / r['entry'] - 1.0)
                adverse = -(float(bar.high) / r['entry'] - 1.0)
            r['mfe'] = max(r['mfe'], favorable)
            r['mae'] = min(r['mae'], adverse)

    def finalize_market_day(self, day):
        if self.last_bar_date.get('SPY') != day:
            return
        spy_close = self.last_close.get('SPY')
        if spy_close is None or spy_close <= 0:
            return
        for r in self.rows.values():
            if not r['entered'] or r['complete'] or r['failed']:
                continue
            if day <= r['entry_date']:
                continue
            r['sessions_after'] += 1
            h = r['sessions_after']
            if h not in (1, 3, 5):
                continue
            ticker = r['ticker']
            if self.last_bar_date.get(ticker) != day or r['spy_entry'] is None or r['spy_entry'] <= 0:
                r['failed'] = True
                continue
            stock_close = self.last_close[ticker]
            stock_ret = stock_close / r['entry'] - 1.0
            spy_ret = spy_close / r['spy_entry'] - 1.0
            directional = r['dir'] * stock_ret
            directional_excess = r['dir'] * (stock_ret - spy_ret)
            r['h'][h] = {
                'stock': stock_ret, 'spy': spy_ret, 'd': directional, 'dx': directional_excess,
                'n10': directional_excess - 0.0010 if r['dir'] != 0 else 0.0,
                'n25': directional_excess - 0.0025 if r['dir'] != 0 else 0.0,
                'n50': directional_excess - 0.0050 if r['dir'] != 0 else 0.0,
                'mfe': r['mfe'], 'mae': r['mae'], 'date': day
            }
            if h == 5:
                r['complete'] = True

    def on_end_of_algorithm(self):
        if self.current_global_date is not None:
            self.finalize_market_day(self.current_global_date)
        complete = [r for r in self.rows.values() if r['complete'] and all(h in r['h'] for h in (1, 3, 5))]
        failed = [r['id'] for r in self.rows.values() if r not in complete]

        self.set_runtime_statistic('P2 Protocol', 'M6.2_P2_OUTCOME_EXTRACTION_PROTOCOL_V0_1')
        self.set_runtime_statistic('P2 Implementation', 'v0.1R_EVENT_DRIVEN_NO_FUTURE_HISTORY')
        self.set_runtime_statistic('P2 Expected', str(len(self.events)))
        self.set_runtime_statistic('P2 Extracted', str(len(complete)))
        self.set_runtime_statistic('P2 DataLimited', str(len(failed)))
        self.set_runtime_statistic('P2 Failed IDs', 'NONE' if not failed else '|'.join(failed))
        self.set_runtime_statistic('P2 Orders', '0')

        complete.sort(key=lambda x: x['id'])
        for i, r in enumerate(complete, 1):
            self.set_runtime_statistic('P2_%02d' % i, self.compact_row(r))
        self.summarize(complete)

    def compact_row(self, r):
        vals = [
            r['id'], r['cat'], r['ticker'], r['entry_time'].strftime('%Y-%m-%dT%H:%M'),
            '%.4f' % r['entry'], '%.4f' % r['prior'], '%.6f' % r['shock'], str(r['dir']), '%.1f' % r['delay'],
            '%.6f' % r['h'][1]['stock'], '%.6f' % r['h'][3]['stock'], '%.6f' % r['h'][5]['stock'],
            '%.6f' % r['h'][1]['spy'], '%.6f' % r['h'][3]['spy'], '%.6f' % r['h'][5]['spy'],
            '%.6f' % r['h'][1]['dx'], '%.6f' % r['h'][3]['dx'], '%.6f' % r['h'][5]['dx'],
            '%.6f' % r['h'][1]['n25'], '%.6f' % r['h'][3]['n25'], '%.6f' % r['h'][5]['n25'],
            '%.6f' % r['h'][1]['mfe'], '%.6f' % r['h'][1]['mae'], '%.6f' % r['h'][3]['mfe'], '%.6f' % r['h'][3]['mae'],
            '%.6f' % r['h'][5]['mfe'], '%.6f' % r['h'][5]['mae'],
            'DELAY' if r['delay'] is not None and r['delay'] > 2.0 else 'OK'
        ]
        return '|'.join(vals)

    def mean(self, xs):
        return sum(xs) / len(xs) if xs else 0.0

    def trimmed_mean(self, xs, frac=0.10):
        if not xs:
            return 0.0
        ys = sorted(xs)
        k = int(len(ys) * frac)
        if 2 * k >= len(ys):
            return self.mean(ys)
        return self.mean(ys[k:len(ys)-k])

    def cluster_bootstrap_ci(self, rows, h=3, reps=5000):
        clusters = {}
        for r in rows:
            clusters.setdefault(r['ticker'], []).append(r['h'][h]['n25'])
        names = sorted(clusters.keys())
        if not names:
            return 0.0, 0.0
        rng = random.Random(620026)
        values = []
        for _ in range(reps):
            sample = []
            for _j in range(len(names)):
                name = names[rng.randrange(len(names))]
                sample.extend(clusters[name])
            values.append(self.mean(sample))
        values.sort()
        lo = values[int(0.025 * (len(values) - 1))]
        hi = values[int(0.975 * (len(values) - 1))]
        return lo, hi

    def summarize(self, rows):
        valid = [r for r in rows if r['dir'] != 0]
        self.set_runtime_statistic('P2 Direction +', str(sum(1 for r in valid if r['dir'] > 0)))
        self.set_runtime_statistic('P2 Direction -', str(sum(1 for r in valid if r['dir'] < 0)))
        self.set_runtime_statistic('P2 Direction 0', str(sum(1 for r in rows if r['dir'] == 0)))
        self.set_runtime_statistic('P2 Delayed Entry', str(sum(1 for r in rows if r['delay'] is not None and r['delay'] > 2.0)))
        if not valid:
            self.set_runtime_statistic('P2 H1 Gate', 'NO_GO_NO_DIRECTION')
            return

        for h in (1, 3, 5):
            for label, key in [('10', 'n10'), ('25', 'n25'), ('50', 'n50')]:
                xs = [r['h'][h][key] for r in valid]
                self.set_runtime_statistic('P2 T%d Mean Net%s' % (h, label), '%.6f' % self.mean(xs))
            xs25 = [r['h'][h]['n25'] for r in valid]
            self.set_runtime_statistic('P2 T%d Median Net25' % h, '%.6f' % statistics.median(xs25))
            self.set_runtime_statistic('P2 T%d Hit Net25' % h, '%.4f' % (sum(1 for x in xs25 if x > 0) / len(xs25)))

        primary = [r['h'][3]['n25'] for r in valid]
        pmean = self.mean(primary)
        pmedian = statistics.median(primary)
        ptrim = self.trimmed_mean(primary)
        ci_lo, ci_hi = self.cluster_bootstrap_ci(valid, 3)
        abs_total = sum(abs(x) for x in primary)
        top3_abs = sum(sorted((abs(x) for x in primary), reverse=True)[:3])
        pos = sorted((x for x in primary if x > 0), reverse=True)
        pos_total = sum(pos)
        top3_pos = sum(pos[:3])
        top3_abs_share = top3_abs / abs_total if abs_total > 0 else 0.0
        top3_pos_share = top3_pos / pos_total if pos_total > 0 else 0.0

        self.set_runtime_statistic('P2 Primary T3 Mean', '%.6f' % pmean)
        self.set_runtime_statistic('P2 Primary T3 Median', '%.6f' % pmedian)
        self.set_runtime_statistic('P2 Primary T3 Trim10', '%.6f' % ptrim)
        self.set_runtime_statistic('P2 Primary T3 CI95', '%.6f,%.6f' % (ci_lo, ci_hi))
        self.set_runtime_statistic('P2 Primary Top3AbsShare', '%.4f' % top3_abs_share)
        self.set_runtime_statistic('P2 Primary Top3PosShare', '%.4f' % top3_pos_share)

        m1 = self.mean([r['h'][1]['n25'] for r in valid])
        m5 = self.mean([r['h'][5]['n25'] for r in valid])
        if pmean > 0 and ptrim > 0 and ci_lo > 0 and m1 >= 0 and m5 >= 0:
            gate = 'GO'
        elif pmean > 0 and ptrim > 0:
            gate = 'INCONCLUSIVE'
        else:
            gate = 'NO_GO'
        self.set_runtime_statistic('P2 H1 Gate', gate)
        self.set_runtime_statistic('P2 Interpretation', 'PILOT_NOT_PRODUCTION_VALIDATION')
