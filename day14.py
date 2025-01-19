from time import time
from threading import Thread

import requests


# 繼承Thread類建立自定義的執行緒類
class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Hao/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 透過requests模組的get函式獲取網路資源
    # 下面的程式碼中使用了天行資料介面提供的網路API
    # 要使用該資料介面需要在天行資料的網站上註冊
    # 然後用自己的Key替換掉下面程式碼的中APIKey即可
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=APIKey&num=10')
    # 將伺服器返回的JSON格式的資料解析為字典
    data_model = resp.json()
    for mm_dict in data_model['tip']:
        url = mm_dict['picUrl']
        # 透過多執行緒的方式實現圖片下載
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()