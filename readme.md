<h1 align="center">
  <br>
  tradestation-api
  <br>
</h1>

<p align="center">
  <a href="https://github.com/pattertj/ts-api/commits/main"><img src="https://img.shields.io/github/last-commit/pattertj/ts-api"></a>
  <a href="https://pypi.org/project/ts-api/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/ts-api"></a>
  <a href="https://github.com/pattertj/ts-api/network/members"><img src="https://img.shields.io/github/forks/pattertj/ts-api?style=flat"></a>
  <a href="https://github.com/pattertj/ts-api/stargazers"><img src="https://img.shields.io/github/stars/pattertj/ts-api?style=flat"></a>
  <a href="https://github.com/pattertj/ts-api/blob/main/LICENSE"><img src="https://img.shields.io/github/license/pattertj/ts-api?style=flat"></a>
</p>

<h4 align="center">An unofficial Python wrapper for the TradeStation API.</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#features">Features</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## Description

tradestation-api is an unofficial wrapper for the TradeStation API. It aims to be as light and unopinionated as possible, offering an elegant programmatic interface over each endpoint. Notable functionality includes:

- Login and authentication
- MarketData, Brokerage, and Order Execution endpoints
- Options chains
- Trades and trade management
- Account info and preferences

**tradestation-api is very much a work in progress and is currently not feature complete. See the [Issues](https://github.com/pattertj/ts-api/issues) to make a suggestion.**

In-flight features include:

- Streaming Client endpoints
- Helpers for complicated dictionary request endpoints

## Why tradestation-api?

tradestation-api has two core goals:

1. **Simplify the OAuth authentication procedure.** This includes initial registration, refresh tokens, and automatic re-authorization of access tokens
2. **Be as lightweight as possible.** tradestation-api takes in the base datatypes and returns the raw responses. No heavy logic or validation. Optional assistance with building orders and complex order groups is in the roadmap for this rather complex task.

## Installation

```shell
# Install ts-api
pip install ts-api
```

## Usage

```python
# Import the TradeStation auth package
import ts.auth as a

# Establish your client
client = a.easy_client("key", "secret", "redirect")

# Call your endpoint
account = client.user_accounts("user_id")
```

## Features

Currently ts-api supports all non-streaming routes found in the [TradeStation API Specification](https://api.tradestation.com/docs/specification). Details for each route can be found below.

### Documentation for Supported API Endpoints

All URIs are relative to _<https://api.tradestation.com>_

| Class               | Method                                                                                                                             | HTTP request                                               | Description             |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------- |
| _BrokerageApi_      | [**get_accounts**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/GetAccounts)                            | **GET** /v3/brokerage/accounts                             | Get Accounts            |
| _BrokerageApi_      | [**get_balances**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/GetBalances)                            | **GET** /v3/brokerage/accounts/{accounts}/balances         | Get Balances            |
| _BrokerageApi_      | [**get_balances_bod**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/GetBalancesBOD)                     | **GET** /v3/brokerage/accounts/{accounts}/bodbalances      | Get Balances BOD        |
| _BrokerageApi_      | [**get_historical_orders**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/GetHistoricalOrders)           | **GET** /v3/brokerage/accounts/{accounts}/historicalorders | Get Historical Orders   |
| _BrokerageApi_      | [**get_orders**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/GetOrders)                                | **GET** /v3/brokerage/accounts/{accounts}/orders           | Get Orders              |
| _BrokerageApi_      | [**get_positions**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/GetPositions)                          | **GET** /v3/brokerage/accounts/{accounts}/positions        | Get Positions           |
| _BrokerageApi_      | [**get_wallets**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/GetWallets)                              | **GET** /v3/brokerage/accounts/{account}/wallets           | Get Wallets             |
| _MarketDataApi_     | [**get_bars**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetBars)                                   | **GET** /v3/marketdata/barcharts/{symbol}                  | Get Bars                |
| _MarketDataApi_     | [**get_crypto_symbol_names**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetCryptoSymbolNames)       | **GET** /v3/marketdata/symbollists/cryptopairs/symbolnames | Get Crypto Symbol Names |
| _MarketDataApi_     | [**get_option_expirations**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetOptionExpirations)        | **GET** /v3/marketdata/options/expirations/{underlying}    | Get Option Expirations  |
| _MarketDataApi_     | [**get_option_risk_reward**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetOptionRiskReward)         | **POST** /v3/marketdata/options/riskreward                 | Get Option Risk Reward  |
| _MarketDataApi_     | [**get_option_spread_types**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetOptionSpreadTypes)       | **GET** /v3/marketdata/options/spreadtypes                 | Get Option Spread Types |
| _MarketDataApi_     | [**get_option_strikes**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetOptionStrikes)                | **GET** /v3/marketdata/options/strikes/{underlying}        | Get Option Strikes      |
| _MarketDataApi_     | [**get_quote_snapshots**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetQuoteSnapshots)              | **GET** /v3/marketdata/quotes/{symbols}                    | Get Quote Snapshots     |
| _MarketDataApi_     | [**get_symbol_details**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetSymbolDetails)                | **GET** /v3/marketdata/symbols/{symbols}                   | Get Symbol Details      |
| _OrderExecutionApi_ | [**cancel_order**](https://api.tradestation.com/docs/specification#tag/Order-Execution/operation/CancelOrder)                      | **DELETE** /v3/orderexecution/orders/{orderID}             | Cancel Order            |
| _OrderExecutionApi_ | [**confirm_group_order**](https://api.tradestation.com/docs/specification#tag/Order-Execution/operation/ConfirmGroupOrder)         | **POST** /v3/orderexecution/ordergroupconfirm              | Confirm Group Order     |
| _OrderExecutionApi_ | [**confirm_order**](https://api.tradestation.com/docs/specification#tag/Order-Execution/operation/ConfirmOrder)                    | **POST** /v3/orderexecution/orderconfirm                   | Confirm Order           |
| _OrderExecutionApi_ | [**get_activation_triggers**](https://api.tradestation.com/docs/specification#tag/Order-Execution/operation/GetActivationTriggers) | **GET** /v3/orderexecution/activationtriggers              | Get Activation Triggers |
| _OrderExecutionApi_ | [**place_group_order**](https://api.tradestation.com/docs/specification#tag/Order-Execution/operation/PlaceGroupOrder)             | **POST** /v3/orderexecution/ordergroups                    | Place Group Order       |
| _OrderExecutionApi_ | [**place_order**](https://api.tradestation.com/docs/specification#tag/Order-Execution/operation/PlaceOrder)                        | **POST** /v3/orderexecution/orders                         | Place Order             |
| _OrderExecutionApi_ | [**replace_order**](https://api.tradestation.com/docs/specification#tag/Order-Execution/operation/ReplaceOrder)                    | **PUT** /v3/orderexecution/orders/{orderID}                | Replace Order           |
| _OrderExecutionApi_ | [**routes**](https://api.tradestation.com/docs/specification#tag/Order-Execution/operation/Routes)                                 | **GET** /v3/orderexecution/routes                          | Get Routes              |

### Not-yet Supported API Endpoints

All URIs are relative to _<https://api.tradestation.com>_

| Class           | Method                                                                                                                                         | HTTP request                                                          | Description                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------ |
| _BrokerageApi_  | [**stream_orders**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/StreamOrders)                                      | **GET** /v3/brokerage/stream/accounts/{accountIds}/orders             | Stream Orders                  |
| _BrokerageApi_  | [**stream_orders_by_order_id**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/StreamOrdersByOrderId)                 | **GET** /v3/brokerage/stream/accounts/{accountIds}/orders/{ordersIds} | Stream Orders by Order Id      |
| _BrokerageApi_  | [**stream_positions**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/StreamPositions)                                | **GET** /v3/brokerage/stream/accounts/{accountIds}/positions          | Stream Positions               |
| _BrokerageApi_  | [**stream_wallets**](https://api.tradestation.com/docs/specification#tag/Brokerage/operation/StreamWallets)                                    | **GET** /v3/brokerage/stream/accounts/{account}/wallets               | Stream Wallets                 |
| _MarketDataApi_ | [**get_option_chain**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetOptionChain)                                | **GET** /v3/marketdata/stream/options/chains/{underlying}             | Stream Option Chain            |
| _MarketDataApi_ | [**get_option_quotes**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetOptionQuotes)                              | **GET** /v3/marketdata/stream/options/quotes                          | Stream Option Quotes           |
| _MarketDataApi_ | [**stream_bars**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/StreamBars)                                         | **GET** /v3/marketdata/stream/barcharts/{symbol}                      | Stream Bars                    |
| _MarketDataApi_ | [**stream_market_depth_aggregates**](<(https://api.tradestation.com/docs/specification#tag/MarketData/operation/StreamMarketDepthAggregates)>) | **GET** /v3/marketdata/stream/marketdepth/aggregates/{symbol}         | Stream Market Depth Aggregates |
| _MarketDataApi_ | [**stream_market_depth_quotes**](<(https://api.tradestation.com/docs/specification#tag/MarketData/operation/StreamMarketDepthQuotes)>)         | **GET** /v3/marketdata/stream/marketdepth/quotes/{symbol}             | Stream Market Depth Quotes     |
| _MarketdataApi_ | [**search_symbols**](https://api.tradestation.com/docs/specification#tag/marketdata/operation/searchSymbols)                                   | **GET** /v2/data/symbols/search/{criteria}                            | Search for Symbols             |
| _MarketdataApi_ | [**suggestsymbols**](https://api.tradestation.com/docs/specification#tag/marketdata/operation/suggestsymbols)                                  | **GET** /v2/data/symbols/suggest/{text}                               | Suggest Symbols                |
| _MarketDataApi_ | [**get_quote_change_stream**](https://api.tradestation.com/docs/specification#tag/MarketData/operation/GetQuoteChangeStream)                   | **GET** /v3/marketdata/stream/quotes/{symbols}                        | Stream Quotes                  |

## Contributing

### Start contributing right now

#### Open an issue

If you've found a problem, you can open an [issue](https://github.com/pattertj/LoopTrader/issues/new)!

#### Solve an issue

If you have a solution to one of the open issues, you will need to fork the repository and submit a pull request.

## Credits

Big thanks to the great people on Discord. You know who you are.

## License

[MIT License](LICENSE)

---

> GitHub [@pattertj](https://github.com/pattertj)
