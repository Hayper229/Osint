#!/bin/python3

import requests

num = input('Number: ')

url = 'https://найти-телефон.com/search-mobile-number'

log = requests.post(url, data=num)
f = open('result.txt', 'w')
f.write(log.text)
f.close()
