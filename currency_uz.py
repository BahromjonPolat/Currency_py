#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dastur yozildi: Yak Apr 11 19:51:40 2021

@muallif: Bahromjon Po'lat
@sarlavha: Valyuta kursi

@qo'llanma:
    Dasturni ishga tushirganingizdan so'ng, biror davlatning ISO 3166-1 alpha-3
    formatdagi kodini kiritasiz, misol: USD shaklida. Keyin 'Enter' tugmasini bosing.
    Shundan so'ng, agar siz kiritgan kod biror kalitga mos kelsa, o'sh kalitdagi
    ma'lumotlarni natijasini konsolga chiqaradi. Aks holda "Natija yo'q"
    yozuvi chiqadi. Quyida dasuturdan foydalanish uchun misol keltirilgan.

    misol:
        input:
            Davlat kodini kiriting: USD

        output:
            Nomi -> AQSh dollari
            Kodi -> USD
            MB narxi -> 10482.97
            NBU sotib olish narxi -> 10430.00
            NBU sotish narxi -> 10500.00
            Sana -> 08.04.2021 09:00:01

@manba: https://nbu.uz/uz/exchange-rates/json/
"Valyuta kurslari O'zbekiston milliy banki"ning rasmiy saytidan olindi.

"""

currency = {
    "UAE": {
        "title": "BAA dirhami",
        "code": "AED",
        "cb_price": "2853.91",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "AUD": {
        "title": "Avstraliya dollari",
        "code": "AUD",
        "cb_price": "7988.02",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "CAD": {
        "title": "Kanada dollari",
        "code": "CAD",
        "cb_price": "8344.98",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "CHF": {
        "title": "Shveytsariya franki",
        "code": "CHF",
        "cb_price": "11114.26",
        "nbu_buy_price": "10600.00",
        "nbu_cell_price": "11800.00",
        "date": "08.04.2021 09:00:01"
    },
    "CNY": {
        "title": "Xitoy yuani",
        "code": "CNY",
        "cb_price": "1596.29",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "DKK": {
        "title": "Daniya kronasi",
        "code": "DKK",
        "cb_price": "1654.56",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "EGP": {
        "title": "Misr funti",
        "code": "EGP",
        "cb_price": "666.86",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "EUR": {
        "title": "Yevro",
        "code": "EUR",
        "cb_price": "12308.06",
        "nbu_buy_price": "12200.00",
        "nbu_cell_price": "13000.00",
        "date": "08.04.2021 09:00:01"
    },
    "GBP": {
        "title": "Angliya funt sterlingi",
        "code": "GBP",
        "cb_price": "14524.15",
        "nbu_buy_price": "13800.00",
        "nbu_cell_price": "15000.00",
        "date": "08.04.2021 09:00:01"
    },
    "ISK": {
        "title": "Islandiya kronasi",
        "code": "ISK",
        "cb_price": "82.76",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "JPY": {
        "title": "Yaponiya iyenasi",
        "code": "JPY",
        "cb_price": "94.77",
        "nbu_buy_price": "86.00",
        "nbu_cell_price": "102.00",
        "date": "08.04.2021 09:00:01"
    },
    "KRW": {
        "title": "Koreya respublikasi voni",
        "code": "KRW",
        "cb_price": "9.29",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "KWD": {
        "title": "Quvayt dinori",
        "code": "KWD",
        "cb_price": "34677.37",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "KZT": {
        "title": "Qozog‘iston tengesi",
        "code": "KZT",
        "cb_price": "24.49",
        "nbu_buy_price": "13.00",
        "nbu_cell_price": "30.00",
        "date": "08.04.2021 09:00:01"
    },
    "LBP": {
        "title": "Livan funti",
        "code": "LBP",
        "cb_price": "6.93",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "MYR": {
        "title": "Malayziya ringgiti",
        "code": "MYR",
        "cb_price": "2530.59",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "NOK": {
        "title": "Norvegiya kronasi",
        "code": "NOK",
        "cb_price": "1226.19",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "PLN": {
        "title": "Polsha zlotiysi",
        "code": "PLN",
        "cb_price": "2677.64",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "RUB": {
        "title": "Rossiya rubli",
        "code": "RUB",
        "cb_price": "137.32",
        "nbu_buy_price": "110.00",
        "nbu_cell_price": "160.00",
        "date": "08.04.2021 09:00:01"
    },
    "SEK": {
        "title": "Shvetsiya kronasi",
        "code": "SEK",
        "cb_price": "1197.03",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "SGD": {
        "title": "Singapur dollari",
        "code": "SGD",
        "cb_price": "7794.03",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "TRY": {
        "title": "Turkiya lirasi",
        "code": "TRY",
        "cb_price": "1288.45",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "UAH": {
        "title": "Ukraina grivnasi",
        "code": "UAH",
        "cb_price": "375.50",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "USD": {
        "title": "AQSh dollari",
        "code": "USD",
        "cb_price": "10482.97",
        "nbu_buy_price": "10430.00",
        "nbu_cell_price": "10500.00",
        "date": "08.04.2021 09:00:01"
    }
}

code = input("Davlat kodini kiriting: ")
result = currency.get(code.upper())

if result:
    print("Nomi ->", result['title'])
    print("Kodi ->", result['code'])
    print("MB narxi ->", result['cb_price'])
    print("NBU sotib olish narxi ->", result['nbu_buy_price'])
    print("NBU sotish narxi ->", result['nbu_cell_price'])
    print("Sana ->", result['date'])
else:
    print("Natija yo'q")
