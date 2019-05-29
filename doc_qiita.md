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


![ImprementExample]( "ImprementExample")


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

アクセストークン






## 参考文献

