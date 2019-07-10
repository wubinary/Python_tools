from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re,requests,time

def jsonRequest(url):   
    req = requests.get(url)
    
    return req.json()

def htmlRequest(url,headers={'User-Agent': 'Mozilla/5.0'}):    
    req = Request(url, headers=headers)

    web_byte = urlopen(req).read()

    webpage = web_byte.decode('utf-8')

    return webpage

'''
contractAddress = '0x7ec0285db4a27ff017fc42137c342337c17f9d95'
holderAddress = '0xa3cb0c49d93e17f6e2c75b2dc56636b3e8599691'
url = '{}{}{}{}'.format('https://ropsten.etherscan.io/token/',contractAddress,'?a=',holderAddress)
html_doc = htmlRequest(url)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.p)
'''

'''
ropstenApi = 'https://api-ropsten.etherscan.io/api?module='
standardApi = 'https://api.etherscan.io/api?module='
url2 = 'http://api.etherscan.io/api?module=account&action=txlist&'\
            'address=0xd462c12f4e40167ccaf5b9ad6c69998c3d758761&startblock=0&endblock=99999999&sort=asc&apikey=YourApiKeyToken'
print(jsonRequest(url2))
'''
