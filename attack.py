import urllib.request
import requests
from bs4 import BeautifulSoup
 
url = "https://main--bucolic-creponne-360862.netlify.app/"

data = urllib.request.urlopen(url)
html = data.read().decode("utf-8")
data.close()
print(html)



username = "admin"
password = "0000"
login_url = "https://main--bucolic-creponne-360862.netlify.app/"

# セッションのインスタンスを作成する。
session = requests.Session()
response_1 = session.post(
        url=login_url,
        data={
            "id": username,
            "pass": password,
        }
    )

print(response_1.text)
# 長いので出力略
# ログイン後に表示される機能メニューのHTMLが得られている。