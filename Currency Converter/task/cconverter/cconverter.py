import requests

rates = requests.get(f'http://www.floatrates.com/daily/{input().lower()}.json').json()
cache = {'usd': 0, 'eur': 0}
while code := input().lower():
    check = ('Sorry, but it is not', 'Oh! It is')[code in cache]
    cache[code] = round(float(input()) * rates[code.lower()]['rate'], 2)
    print(f'Checking the cache...\n{check} in the cache!\nYou recieved {cache[code]} {code}.')
