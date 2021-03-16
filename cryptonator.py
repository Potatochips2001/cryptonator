import requests
import json

def monero():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/xmr-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def xmr():
    return monero()

def bitcoin():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/btc-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def btc():
    return bitcoin()

def ethereum():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/eth-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def eth():
    return ethereum()

def litecoin():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/ltc-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def ltc():
    return litecoin()

def dogecoin():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/doge-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def doge():
    return dogecoin()

def dash():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/dash-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def ripple():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/xrp-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def xrp():
    return ripple()

def tether():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/usdt-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def usdt():
    return tether()

def bittorrent():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/btt-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def btt():
    return bittorrent()

def trueusd():
    get_ = requests.get("https://api.cryptonator.com/api/ticker/tusd-usd", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
    jsonData = json.loads(get_.text)
    return float(jsonData["ticker"]["price"])

def tusd():
    return trueusd()