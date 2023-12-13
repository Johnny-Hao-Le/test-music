import requests
import json

url= 'https://github.com/ashrika786/api-testing-python/blob/main/test_utils.py'
r = requests.get(url)
print(r.text)