#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 19:18:59 2021

@author: Bakhromjon Polat
@title Currency

@documention:

    You can use this program as an example below.

    input:
        Enter ISO code: USD

     output:
        Title -> US Dollar
        Code -> USD
        CB Price -> 10482.97
        NBU buy price -> 10430.00
        NBU cell price -> 10500.00
        Date -> 04/08/2021 09:00:01 am

source: https://nbu.uz/en/exchange-rates/json/

"""

currency = {
    "UAE": {
        "title": "UAE Dirham",
        "code": "AED",
        "cb_price": "2853.91",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "AUD": {
        "title": "Australian Dollar",
        "code": "AUD",
        "cb_price": "7988.02",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "CAD": {
        "title": "Canadian Dollar",
        "code": "CAD",
        "cb_price": "8344.98",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "CHF": {
        "title": "Swiss Franc",
        "code": "CHF",
        "cb_price": "11114.26",
        "nbu_buy_price": "10600.00",
        "nbu_sell_price": "11800.00",
        "date": "04/08/2021 09:00:01 am"
    },
    "CNY": {
        "title": "Chinese Yuan",
        "code": "CNY",
        "cb_price": "1596.29",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "DKK": {
        "title": "Danish Krone",
        "code": "DKK",
        "cb_price": "1654.56",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "EGP": {
        "title": "Egyptian Pound",
        "code": "EGP",
        "cb_price": "666.86",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "EUR": {
        "title": "EURO",
        "code": "EUR",
        "cb_price": "12308.06",
        "nbu_buy_price": "12200.00",
        "nbu_sell_price": "13000.00",
        "date": "04/08/2021 09:00:01 am"
    },
    "GBP": {
        "title": "British Pound",
        "code": "GBP",
        "cb_price": "14524.15",
        "nbu_buy_price": "13800.00",
        "nbu_sell_price": "15000.00",
        "date": "04/08/2021 09:00:01 am"
    },
    "ISK": {
        "title": "Iceland Krone",
        "code": "ISK",
        "cb_price": "82.76",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "JPY": {
        "title": "Japanese Yen",
        "code": "JPY",
        "cb_price": "94.77",
        "nbu_buy_price": "86.00",
        "nbu_sell_price": "102.00",
        "date": "04/08/2021 09:00:01 am"
    },
    "KRW": {
        "title": "South Korean Won",
        "code": "KRW",
        "cb_price": "9.29",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "KWD": {
        "title": "Kuwaiti Dinar",
        "code": "KWD",
        "cb_price": "34677.37",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "KZT": {
        "title": "Kazakhstan Tenge",
        "code": "KZT",
        "cb_price": "24.49",
        "nbu_buy_price": "13.00",
        "nbu_sell_price": "30.00",
        "date": "04/08/2021 09:00:01 am"
    },
    "LBP": {
        "title": "Lebanese Pound",
        "code": "LBP",
        "cb_price": "6.93",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "MYR": {
        "title": "Malaysian Ringgit",
        "code": "MYR",
        "cb_price": "2530.59",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "NOK": {
        "title": "Norwegian Krone",
        "code": "NOK",
        "cb_price": "1226.19",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "PLN": {
        "title": "Polish Zloty",
        "code": "PLN",
        "cb_price": "2677.64",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "RUB": {
        "title": "Russian Rouble",
        "code": "RUB",
        "cb_price": "137.32",
        "nbu_buy_price": "110.00",
        "nbu_sell_price": "160.00",
        "date": "04/08/2021 09:00:01 am"
    },
    "SEK": {
        "title": "Swedish Krone",
        "code": "SEK",
        "cb_price": "1197.03",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "SGD": {
        "title": "Singapore Dollar",
        "code": "SGD",
        "cb_price": "7794.03",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "TRY": {
        "title": "New Turkish Lira",
        "code": "TRY",
        "cb_price": "1288.45",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "UAH": {
        "title": "Ukrainian Hryvnia",
        "code": "UAH",
        "cb_price": "375.50",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "04/08/2021 09:00:01 am"
    },
    "USD": {
        "title": "US Dollar",
        "code": "USD",
        "cb_price": "10482.97",
        "nbu_buy_price": "10430.00",
        "nbu_sell_price": "10500.00",
        "date": "04/08/2021 09:00:01 am"
    }
}

code = input("Enter ISO code: ")
result = currency.get(code.upper())

if result:
    print("Title ->", result['title'])
    print("Code ->", result['code'])
    print("CB Price ->", result['cb_price'])
    print("NBU buy price ->", result['nbu_buy_price'])
    print("NBU cell price ->", result['nbu_sell_price'])
    print("Date ->", result['date'])
else:
    print("No result")
