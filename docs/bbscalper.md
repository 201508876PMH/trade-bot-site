# BBScalper Strategy
#### Type <Badge type="warning" text="HF"/><Badge type="tip" text="Indicators"/>
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

````md{11}
<!--@include: /backtest_results/bbscalper/backtest_report.md-->
````

**LEFT OPEN TRADES REPORT**

```md{7}
<!--@include: /backtest_results/bbscalper/left_open_trades_report.md-->
```

**ENTER TAG STATS**

```md{5}
<!--@include: /backtest_results/bbscalper/enter_tags.md-->
```

**EXIT REASON STATS**

```md{7}
<!--@include: /backtest_results/bbscalper/exit_tags.md-->
```
**MIXED TAG STATS**

```md
<!--@include: /backtest_results/bbscalper/mixed_tags.md-->
```

**SUMMARY METRICS**

```md{13}
<!--@include: /backtest_results/bbscalper/summary_metrics.md-->
```

**STRATEGY SUMMARY**

```md
<!--@include: /backtest_results/bbscalper/strategy_summary.md-->
```