# PythonでLINEにメッセージを送る

<!---
    title: PythonでLINEにメッセージを送る
    tags: Python LineNotify Line bot
    author: moriita
    slide: false
-->



## はじめに

何番煎じかわかりませんが，Python x LINE NotifyでLINEにメッセージを送れるボットを作ったので，その備忘録です。

深層学習モデルの学習など，時間がかかる処理を回しているときに，その場を離れても進捗状況を知りたい！というときに重宝しています。



## できること

LINEのグループや自分自身にメッセージ・画像・スタンプを送る

※こちらからのメッセージには反応できない

![ImprementExample](https://github.com/moritagit/LINENotifyBot/blob/doc/figures/imprement_example.png "ImprementExample")



## LINE Notifyについて

[LINE Notify公式](https://notify-bot.line.me/ja/)

> Webサービスからの通知をLINEで受信
> Webサービスと連携すると、LINEが提供する公式アカウント"LINE Notify"から通知が届きます。
> 複数のサービスと連携でき、グループでも通知を受信することが可能です。



## 動作環境

僕の環境は下の通りです。
が，Pythonで`import requests`できれば動くと思います。

* Windows10 (64bit)
* Python3.6



## 準備

### LINE Notifyと友達になる

まずはLINE Notifyを友達に追加します。
自分に送るだけならこれで大丈夫です。
グループに送りたいときは，そのグループにLINE Notifyを招待しておきます。
このLINE Notifyからメッセージが送られてきます。


### アクセストークンの発行

次に，アクセストークンを発行します。

1. [LINE Notify公式](https://notify-bot.line.me/ja/)にアクセス
1. 右上からログイン
1. ログインと同じところをクリックし，マイページへ
1. ページ下部の「アクセストークンを発行」をクリック
1. 解除したいときは「解除」をクリック



## 実装



```python:line_notify_bot.py
import requests


class LINENotifyBot:
    API_URL = 'https://notify-api.line.me/api/notify'
    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(
            self, message,
            image=None, sticker_package_id=None, sticker_id=None,
            ):
        payload = {
                    'message': message,
                    'stickerPackageId': sticker_package_id,
                    'stickerId': sticker_id,
                    }
        files = {}
        if image != None:
            files = {'imageFile': open(image, 'rb')}
        r = requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
            )
```



## 参考文献

