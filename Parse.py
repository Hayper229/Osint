#!/bin/python3

import os
import requests

url=input('Url: ')
name=input('Name: ')
response=requests.get(url)
with open(f'{name}.png', 'w') as f:
     f.write(response.text)

