import requests


def get_exchange_rate(currency, exch_to):
    rate_url = 'http://www.floatrates.com'
    exch_url_path = f'{rate_url}/daily/{currency}.json'

    usd_resp = requests.get(exch_url_path)
    return usd_resp.json()[exch_to]['rate']


def check_if_exchange_rate_is_cached(dict_cache, currency):
    print('Checking the cache...')
    if currency in dict_cache:
        print('Oh! It is in the cache!')
        return dict_cache[currency]
    else:
        print('Sorry, but it is not in the cache!')
        return False


dict_exch_rate = {}
user_main_currency = input().lower()

if user_main_currency == 'eur':
    dict_exch_rate['usd'] = get_exchange_rate('eur', 'usd')
elif user_main_currency == 'usd':
    dict_exch_rate['eur'] = get_exchange_rate('usd', 'eur')
else:
    dict_exch_rate['eur'] = get_exchange_rate(user_main_currency, 'eur')
    dict_exch_rate['usd'] = get_exchange_rate(user_main_currency, 'usd')

while user_currency_input := input().lower():
    amount_to_exch = float(input())
    resp = check_if_exchange_rate_is_cached(dict_exch_rate, user_currency_input)
    if resp is False:
        dict_exch_rate[user_currency_input] = get_exchange_rate(
            user_main_currency, user_currency_input)
    print(f'You received {round(dict_exch_rate[user_currency_input] * amount_to_exch, 2)} '
          f'{user_currency_input.upper()}.')
