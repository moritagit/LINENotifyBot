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

<img src="https://github.com/moritagit/LINENotifyBot/blob/doc/figures/imprement_example.png" width=50%>



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
1. ページ下部の「トークンを発行」をクリック
1. トークン名を指定し，グループを選択して発行
1. 発行されたトークンをコピーしてどこかに保存
1. 解除したいときは「解除」をクリック



## 実装

### ライブラリ

必要なのはrequestsだけなので，

```python
import requests
```


### 準備

LINE NotifyのAPIのURLと，アクセストークンを含んだヘッダが必要になります。

```python
url = "https://notify-api.line.me/api/notify"
access_token = 'Your Access Token'
headers = {'Authorization': 'Bearer ' + access_token}
```


### メッセージを送る

3行でメッセージを送ることができます。

```python
message = 'Write Your Message'
payload = {'message': message}
r = requests.post(url, headers=headers, params=payload,)
```


### 画像を送る

画像を送るときは，`requests.post`にfilesも渡します。
なお，メッセージも一緒でないと送れないので注意が必要です。

```python
message = 'Write Your Message'
image = 'test.png'  # png or jpg
payload = {'message': message}
files = {'imageFile': open(image, 'rb')}
r = requests.post(url, headers=headers, params=payload, files=files,)
```


### スタンプを送る

スタンプを送るときは，`payload`に`stickerPackageId`と`stickerId`を追加します。
これらのIDは[ここ](https://devdocs.line.me/files/sticker_list.pdf)から探してきて指定します。
画像と同様，メッセージも一緒じゃないと送れません。
また，存在しないIDを指定した場合はメッセージも送られないので，注意が必要です。

```python
message = 'Write Your Message'
payload = {
    'message': message,
    'stickerPackageId': 1,
    'stickerId': 13,
    }
r = requests.post(url, headers=headers, params=payload,)
```


### まとめる

以上をまとめてクラスにしてしまうと，次のようになります。

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

実行は次のようになります。

```python
from line_notify_bot import LINENotifyBot

bot = LINENotifyBot(access_token='Your Access Token')

bot.send(
    message='Write Your Message',
    image='test.png',  # png or jpg
    sticker_package_id=1,
    sticker_id=13,
    )
```

こちらはGitHubに公開しているので，使えればOKという方はcloneして頂ければすぐ使えます。

```console
git clone https://github.com/moritagit/LINENotifyBot.git
```



### まとめ

自分が使いやすいように作ってみましたが，かなり簡単に使える割になかなか便利です。
とりあえず深層学習モデルの学習中にlossの値や学習曲線を送ったりしてみてます（tensorboardを使いましょう）。
スタンプを自動で送りたい場面にはまだ出会ってないので，早く出会いたいところ。
