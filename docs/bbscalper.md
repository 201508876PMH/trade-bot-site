# BBScalper Strategy

This page documents the performance and behavior of the **BBScalper** trading strategy, including backtesting results, key performance metrics, and trade analytics.

The data presented here is based on historical backtesting within a specified time frame and trading conditions. It is intended to provide a quantitative overview of how the strategy performs under simulated market conditions.

::: info Data
Backtest results can be downloaed here: :bar_chart:<code>[test](https://github.com/201508876PMH)</code>
:::
## Backtest.conf
```json:line-numbers{14}
{
  "args": [
    "backtesting",
    "--config", 
      "user_data/config.json",
    "--strategy",    
      "BBScalper",
    "--timerange",
      "20240101-20250101",
    "--timeframe",
      //"4h",
      // "1h",
      //"30m",
      "15m",
      //"5m"
  ]
}
```
## Overview

The following section provides a detailed breakdown of the backtesting results for the **BBScalper** strategy.

### **BACKTESTING REPORT**

````md
┏━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ DOGE/USDT:USDT │    234 │         0.26 │         308.239 │        30.82 │      7:47:00 │   90     0   144  38.5 │
│  ADA/USDT:USDT │    188 │         0.38 │         284.227 │        28.42 │     11:53:00 │   76     0   112  40.4 │
│  ETH/USDT:USDT │    218 │         0.13 │         206.312 │        20.63 │     16:05:00 │   80     0   138  36.7 │
│  BTC/USDT:USDT │    167 │         0.14 │         148.220 │        14.82 │     22:35:00 │   61     0   106  36.5 │
│  SOL/USDT:USDT │    262 │         0.13 │         112.313 │        11.23 │      7:58:00 │   96     0   166  36.6 │
│  SUI/USDT:USDT │    308 │         0.14 │          62.576 │         6.26 │      6:21:00 │  113     0   195  36.7 │
│  TON/USDT:USDT │    198 │         0.09 │          18.149 │         1.81 │     14:56:00 │   71     0   127  35.9 │
│          TOTAL │   1575 │         0.18 │        1140.036 │        114.0 │     11:39:00 │  587     0   988  37.3 │
└────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
````

**LEFT OPEN TRADES REPORT**

```md
┏━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  ETH/USDT:USDT │      1 │         0.02 │           0.160 │         0.02 │      2:45:00 │    1     0     0   100 │
│ DOGE/USDT:USDT │      1 │        -0.06 │          -0.442 │        -0.04 │      2:30:00 │    0     0     1     0 │
│  TON/USDT:USDT │      1 │         -0.4 │          -2.801 │        -0.28 │      2:45:00 │    0     0     1     0 │
│          TOTAL │      3 │        -0.15 │          -3.082 │        -0.31 │      2:40:00 │    1     0     2  33.3 │
└────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
```

**ENTER TAG STATS**

```md
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │    1575 │         0.18 │        1140.036 │        114.0 │     11:39:00 │  587     0   988  37.3 │
│     TOTAL │    1575 │         0.18 │        1140.036 │        114.0 │     11:39:00 │  587     0   988  37.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
```

**EXIT REASON STATS**

```md
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         roi │   586 │         4.02 │       13522.680 │      1352.27 │     13:07:00 │  586     0     0   100 │
│  force_exit │     3 │        -0.15 │          -3.082 │        -0.31 │      2:40:00 │    1     0     2  33.3 │
│   stop_loss │   986 │        -2.11 │      -12379.561 │     -1237.96 │     10:48:00 │    0     0   986     0 │
│       TOTAL │  1575 │         0.18 │        1140.036 │        114.0 │     11:39:00 │  587     0   988  37.3 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
```
**MIXED TAG STATS**

```md
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │         roi │    586 │         4.02 │       13522.680 │      1352.27 │     13:07:00 │  586     0     0   100 │
│           │  force_exit │      3 │        -0.15 │          -3.082 │        -0.31 │      2:40:00 │    1     0     2  33.3 │
│           │   stop_loss │    986 │        -2.11 │      -12379.561 │     -1237.96 │     10:48:00 │    0     0   986     0 │
│     TOTAL │             │   1575 │         0.18 │        1140.036 │        114.0 │     11:39:00 │  587     0   988  37.3 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
```

**SUMMARY METRICS**

```md{13}
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2024-01-03 02:00:00  │
│ Backtesting to                │ 2025-01-01 00:00:00  │
│ Trading Mode                  │ Isolated Futures     │
│ Max open trades               │ 3                    │
│                               │                      │
│ Total/Daily Avg Trades        │ 1575 / 4.34          │
│ Starting balance              │ 1000 USDT            │
│ Final balance                 │ 2140.036 USDT        │
│ Absolute profit               │ 1140.036 USDT        │
│ Total profit %                │ 114.00%              │
│ CAGR %                        │ 114.90%              │
│ Sortino                       │ 16.52                │
│ Sharpe                        │ 3.35                 │
│ Calmar                        │ 13.08                │
│ SQN                           │ 1.60                 │
│ Profit factor                 │ 1.09                 │
│ Expectancy (Ratio)            │ 0.72 (0.06)          │
│ Avg. daily profit %           │ 0.31%                │
│ Avg. stake amount             │ 588.248 USDT         │
│ Total trade volume            │ 1851950.427 USDT     │
│                               │                      │
│ Long / Short                  │ 0 / 1575             │
│ Total profit Long %           │ 0.00%                │
│ Total profit Short %          │ 114.00%              │
│ Absolute profit Long          │ 0 USDT               │
│ Absolute profit Short         │ 1140.036 USDT        │
│                               │                      │
│ Best Pair                     │ ADA/USDT:USDT 28.42% │
│ Worst Pair                    │ TON/USDT:USDT 1.81%  │
│ Best trade                    │ BTC/USDT:USDT 4.44%  │
│ Worst trade                   │ TON/USDT:USDT -2.45% │
│ Best day                      │ 317.672 USDT         │
│ Worst day                     │ -126.781 USDT        │
│ Days win/draw/lose            │ 139 / 33 / 193       │
│ Min/Max/Avg. Duration Winners │ N/A / N/A / 13:06:00 │
│ Min/Max/Avg. Duration Losers  │ N/A / N/A / 10:47:00 │
│ Max Consecutive Wins / Loss   │ 20 / 23              │
│ Rejected Entry signals        │ 8609                 │
│ Entry/Exit Timeouts           │ 0 / 0                │
│                               │                      │
│ Min balance                   │ 986.89 USDT          │
│ Max balance                   │ 3018.569 USDT        │
│ Max % of account underwater   │ 45.86%               │
│ Absolute Drawdown (Account)   │ 45.86%               │
│ Absolute Drawdown             │ 1384.458 USDT        │
│ Drawdown high                 │ 2018.569 USDT        │
│ Drawdown low                  │ 634.112 USDT         │
│ Drawdown Start                │ 2024-08-05 06:15:00  │
│ Drawdown End                  │ 2024-12-08 01:30:00  │
│ Market change                 │ 158.83%              │
└───────────────────────────────┴──────────────────────┘
```

**STRATEGY SUMMARY**

```md
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ BBScalper │   1575 │         0.18 │        1140.036 │        114.0 │     11:39:00 │  587     0   988  37.3 │ 1384.458 USDT  45.86% │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────────┘
```