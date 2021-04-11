"""
Создано 11 апр, 21:18:59 2021

@автор: Бахромжон Пулат
@название: Курсы валют

@документация:
    Вы можете использовать эту программу в качестве примера ниже.

    input:
        Введите код ISO: USD

    output:
        Название -> Доллар США
        Код -> USD
        ЦБ цена -> 10482.97
        NBU цена покупки -> 10430.00
        NBU цена продажи -> 10500.00
        Дата -> 08.04.2021 09:00:01

@источник: https://nbu.uz/exchange-rates/json/

"""
currency = {
    "AED": {
        "title": "Дирхам ОАЭ",
        "code": "AED",
        "cb_price": "2853.91",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "AUD": {
        "title": "Австралийский доллар",
        "code": "AUD",
        "cb_price": "7988.02",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "CAD": {
        "title": "Канадский доллар",
        "code": "CAD",
        "cb_price": "8344.98",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "CHF": {
        "title": "Швейцарский франк",
        "code": "CHF",
        "cb_price": "11114.26",
        "nbu_buy_price": "10600.00",
        "nbu_sell_price": "11800.00",
        "date": "08.04.2021 09:00:01"
    },
    "CNY": {
        "title": "Китайский юань",
        "code": "CNY",
        "cb_price": "1596.29",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "DKK": {
        "title": "Датская крона",
        "code": "DKK",
        "cb_price": "1654.56",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "EGP": {
        "title": "Египетский фунт",
        "code": "EGP",
        "cb_price": "666.86",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "EUR": {
        "title": "Евро",
        "code": "EUR",
        "cb_price": "12308.06",
        "nbu_buy_price": "12200.00",
        "nbu_sell_price": "13000.00",
        "date": "08.04.2021 09:00:01"
    },
    "GBP": {
        "title": "Английский фунт стерлингов",
        "code": "GBP",
        "cb_price": "14524.15",
        "nbu_buy_price": "13800.00",
        "nbu_sell_price": "15000.00",
        "date": "08.04.2021 09:00:01"
    },
    "ISK": {
        "title": "Исландская крона",
        "code": "ISK",
        "cb_price": "82.76",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "JPY": {
        "title": "Японская иена",
        "code": "JPY",
        "cb_price": "94.77",
        "nbu_buy_price": "86.00",
        "nbu_sell_price": "102.00",
        "date": "08.04.2021 09:00:01"
    },
    "KRW": {
        "title": "Южнокорейский вон",
        "code": "KRW",
        "cb_price": "9.29",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "KWD": {
        "title": "Кувейтский динар",
        "code": "KWD",
        "cb_price": "34677.37",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "KZT": {
        "title": "Казахстанский тенге",
        "code": "KZT",
        "cb_price": "24.49",
        "nbu_buy_price": "13.00",
        "nbu_sell_price": "30.00",
        "date": "08.04.2021 09:00:01"
    },
    "LBP": {
        "title": "Ливанский фунт",
        "code": "LBP",
        "cb_price": "6.93",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "MYR": {
        "title": "Малайзийский ринггит",
        "code": "MYR",
        "cb_price": "2530.59",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "NOK": {
        "title": "Норвежская крона",
        "code": "NOK",
        "cb_price": "1226.19",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "PLN": {
        "title": "Польский злотый",
        "code": "PLN",
        "cb_price": "2677.64",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "RUB": {
        "title": "Российский рубль",
        "code": "RUB",
        "cb_price": "137.32",
        "nbu_buy_price": "110.00",
        "nbu_sell_price": "160.00",
        "date": "08.04.2021 09:00:01"
    },
    "SEK": {
        "title": "Шведская крона",
        "code": "SEK",
        "cb_price": "1197.03",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "SGD": {
        "title": "Сингапурский доллар",
        "code": "SGD",
        "cb_price": "7794.03",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "TRY": {
        "title": "Новая Турецкая лира",
        "code": "TRY",
        "cb_price": "1288.45",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "UAH": {
        "title": "Украинская гривна",
        "code": "UAH",
        "cb_price": "375.50",
        "nbu_buy_price": "",
        "nbu_sell_price": "",
        "date": "08.04.2021 09:00:01"
    },
    "USD": {
        "title": "Доллар США",
        "code": "USD",
        "cb_price": "10482.97",
        "nbu_buy_price": "10430.00",
        "nbu_sell_price": "10500.00",
        "date": "08.04.2021 09:00:01"
    }
}

code = input("Введите код ISO: ")
result = currency.get(code.upper())

if result:
    print("Название ->", result['title'])
    print("Код ->", result['code'])
    print("ЦБ цена ->", result['cb_price'])
    print("NBU цена покупки ->", result['nbu_buy_price'])
    print("NBU цена продажи ->", result['nbu_sell_price'])
    print("Дата ->", result['date'])
else:
    print("Безрезультатно")

