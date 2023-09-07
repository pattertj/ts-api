<h1 align="center">
  <br>
  tradestation-api
  <br>
</h1>

<p align="center">
<!-- <a href="https://github.com/pattertj/LoopTrader/commits/main"><img src="https://img.shields.io/github/last-commit/pattertj/LoopTrader"></a>
  <a href="https://github.com/pattertj/LoopTrader/actions/workflows/python-app.yml"><img src="https://img.shields.io/github/workflow/status/pattertj/looptrader/Build?style=flat"></a>
  <a href="https://github.com/pattertj/LoopTrader/network/members"><img src="https://img.shields.io/github/forks/pattertj/LoopTrader?style=flat"></a>
  <a href="https://github.com/pattertj/LoopTrader/stargazers"><img src="https://img.shields.io/github/stars/pattertj/LoopTrader?style=flat"></a>
  <a href="https://github.com/pattertj/LoopTrader/blob/main/LICENSE"><img src="https://img.shields.io/github/license/pattertj/LoopTrader?style=flat"></a>
  <a href="https://saythanks.io/inbox#badge-modal"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"></a> -->
</p>

<h4 align="center">An unofficial Python wrapper for the TradeStation API.</h4>

<p align="center">
  <a href="#description">Description</a>
  <!-- • -->
  <!-- <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a> -->
</p>

## Description

tradestation-api is an unofficial wrapper for the TradeStation API. It aims to be as light and unopinionated as possible, offering an elegant programmatic interface over each endpoint. Notable functionality includes:

- Login and authentication
- MarketData, Brokerage, and Order Execution endpoints
- Options chains
- Trades and trade management
- Account info and preferences

<b>tradestation-api is very much a work in progress and is currently not feature complete. See the [Issues](https://github.com/pattertj/tradestation-api/issues) to make a suggestion.</b>

## In-Progress Features

Several features are still in flight.

- Streaming Client endpoints
- Helpers for complicated dictionary request endpoints

## Why tradestation-api?

tradestation-api has two core goals:

1) **Simplify the OAuth authentication procedure.** This includes initial registration, refresh tokens, and automtic re-authorizing for access tokens
2) **Be as lightweight as possible.** tradestation-api takes in the base datatypes and returns the raw responses. No heavy logic or validation. Optional assistance with building Orders and complex order groups is in the roadmap for this rather complex task.

## How do I use tradestation-api?

``` python
# Code sample
```
