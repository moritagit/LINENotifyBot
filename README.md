# LINE Notify Bot

A bot that can send messages, images, or stickers to a LINE group via LINE Notify.
This bot can't accept messages, i.e., is not interactive.

Japanese article: [Python で LINE にメッセージを送る](https://qiita.com/moriita/items/5b199ac6b14ceaa4f7c9)

<img src="https://github.com/moritagit/LINENotifyBot/blob/doc/figures/imprement_example.png" width=30%>

## Requirements

- Python3
- Python Packages
  - `requests`

## Usage

This module can be used via console like:

```console
python src/line_notify_bot \
    <path/to/access_token> \
    <message> \
    -i <path/to/image/file> \
    -sp <sticker package ID> \
    -s <sticker ID>
```

The fist argument is a path to a file which includes access token only.
Access token and message are necessary, and the others are optional.
If you want to send a sticker, both sticker package ID and sticker ID are needed.

Or this can be used in your code like:

```python
from line_notify_bot import LINENotifyBot

bot = LINENotifyBot(access_token='Your Access Token')

bot.send(
    message='message',
    image='path/to/image (png or jpg)',
    sticker_package_id=1,
    sticker_id=10,
    )
```

These usages are also written in `test/test.ipynb.`

## Install

To install, simply clone from GitHub.

```console
git clone https://github.com/moritagit/LINENotifyBot.git
```

## License

This software is released under the MIT License, see LICENSE.

## References

- [LINE Notify](https://notify-bot.line.me/ja/)
- [Sticker ID List](https://developers.line.biz/ja/docs/messaging-api/sticker-list/)
