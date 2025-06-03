# Freqtrade Automated Crypto Trading Bot

![freqtrade](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/docs/assets/freqtrade_poweredby.svg)

[![Freqtrade CI](https://github.com/freqtrade/freqtrade/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/freqtrade/freqtrade/actions/)
[![DOI](https://joss.theoj.org/papers/10.21105/joss.04864/status.svg)](https://doi.org/10.21105/joss.04864)
[![Coverage Status](https://coveralls.io/repos/github/freqtrade/freqtrade/badge.svg?branch=develop\&service=github)](https://coveralls.io/github/freqtrade/freqtrade?branch=develop)
[![Documentation](https://readthedocs.org/projects/freqtrade/badge/)](https://www.freqtrade.io)
[![Maintainability](https://api.codeclimate.com/v1/badges/5737e6d668200b7518ff/maintainability)](https://codeclimate.com/github/freqtrade/freqtrade/maintainability)

## Overview

Freqtrade is a free and open-source cryptocurrency trading bot written in Python. It supports multiple exchanges and is controllable via Telegram or web UI. Designed for backtesting, plotting, money management, and strategy optimization using machine learning.

![freqtrade](https://raw.githubusercontent.com/freqtrade/freqtrade/develop/docs/assets/freqtrade-screenshot.png)

## Disclaimer

This software is for educational purposes only. Use at your own risk. Always run in dry-run mode first and ensure you fully understand the risks and mechanisms before trading real funds.

## Supported Exchanges

Major supported exchanges:

* Binance
* Bitmart
* BingX
* Bybit
* Gate.io
* HTX
* Hyperliquid (DEX)
* Kraken
* OKX
* MyOKX

Futures (experimental):

* Binance
* Gate.io
* Hyperliquid
* OKX
* Bybit

Community tested:

* Bitvavo
* Kucoin

Refer to [exchange docs](https://www.freqtrade.io/en/stable/exchange/) for special configuration notes.

## Features

* ✅ Python 3.10+
* ✅ Dry-run mode
* ✅ Backtesting
* ✅ Hyperopt strategy optimization
* ✅ Machine learning integration with FreqAI
* ✅ Edge position sizing
* ✅ Whitelisting / Blacklisting coins
* ✅ Built-in Web UI
* ✅ Telegram remote control
* ✅ Fiat-based profit/loss
* ✅ Performance and trade reporting

## Installation

1. Clone the repo:

```bash
git clone https://github.com/freqtrade/freqtrade.git
cd freqtrade
```

2. Install dependencies:

```bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

3. Create user directory and config:

```bash
freqtrade create-userdir --userdir user_data
freqtrade new-config --config user_data/config.json
```

4. Download data:

```bash
freqtrade download-data --exchange binance --quote-currency USDT --timeframe 5m
```

## Configuration

Edit `user_data/config.json` with your keys, exchange name, strategy, etc. Example:

```json
{
  "exchange": {
    "name": "binance",
    "key": "YOUR_API_KEY",
    "secret": "YOUR_API_SECRET"
  },
  "stake_currency": "USDT",
  "stake_amount": "unlimited",
  "timeframe": "5m",
  "strategy": "MyStrategy"
}
```

## Run the Bot

```bash
freqtrade trade --config user_data/config.json --strategy MyStrategy
```

## Use Web UI

```bash
freqtrade webserver --config user_data/config.json
```

Visit [http://localhost:8080](http://localhost:8080)

## Telegram Commands

* `/start` - Start trading
* `/stop` - Stop trading
* `/status` - Show current trades
* `/profit` - Show profit summary
* `/balance` - Show balances
* `/forceexit <id>` - Force close a trade

More: [Telegram Docs](https://www.freqtrade.io/en/stable/telegram-usage/)

## Strategy Example (RSI)

```python
from freqtrade.strategy import IStrategy
import talib.abstract as ta

class MyStrategy(IStrategy):
    timeframe = '5m'

    def populate_indicators(self, dataframe, metadata):
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_buy_trend(self, dataframe, metadata):
        dataframe.loc[dataframe['rsi'] < 30, 'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe, metadata):
        dataframe.loc[dataframe['rsi'] > 70, 'sell'] = 1
        return dataframe
```

## Development Branches

* `develop` – Latest features, may be unstable
* `stable` – Most recent stable release
* `feat/*` – Active development feature branches

## Contributing & Support

* 📚 Docs: [freqtrade.io](https://www.freqtrade.io)
* 💬 Discord: [Join chat](https://discord.gg/p7nuUNVfP7)
* 🐞 Report Bugs: [GitHub Issues](https://github.com/freqtrade/freqtrade/issues)
* ✨ Feature Requests: [Enhancements](https://github.com/freqtrade/freqtrade/labels/enhancement)
* 📦 Pull Requests welcome!

## Requirements

* Python >= 3.10
* pip, git, virtualenv
* Optional: Docker
* Synced system clock (NTP)
* Recommended: 2GB RAM, 2 vCPU, 1GB disk

## Run Summary

To install and run:

```bash
git clone https://github.com/freqtrade/freqtrade.git
cd freqtrade
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
freqtrade create-userdir --userdir user_data
freqtrade new-config --config user_data/config.json
freqtrade download-data --exchange binance --quote-currency USDT --timeframe 5m
freqtrade trade --config user_data/config.json --strategy MyStrategy
```

---

Built with ❤️ using [Freqtrade](https://github.com/freqtrade/freqtrade)
