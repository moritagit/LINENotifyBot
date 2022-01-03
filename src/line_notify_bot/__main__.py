import argparse

from line_notify_bot import LINENotifyBot
from line_notify_bot.env import LINE_NOTIFY_ACCESS_TOKEN


def main():
    parser = argparse.ArgumentParser(
        prog='line_notify_bot',
        usage=(
            'python src/line_notify_bot <messsage> '
            '-i path/to/image -sp <sticker package ID> -s <sticker ID>'
        ),
        description=(
            'Send messages, images, or stickers to a LINE group via LINE Notify.'
        ),
        epilog='end',
        add_help=True,
    )
    parser.add_argument(
        'message',
        help='message to be sent',
        action='store',
    )
    parser.add_argument(
        '-i',
        '--image',
        help='image to be sent',
        action='store',
        required=False,
        default=None,
    )
    parser.add_argument(
        '-sp',
        '--stickerpackage',
        help=(
            'sticker package ID '
            '(see https://developers.line.biz/ja/docs/messaging-api/sticker-list/)'
        ),
        type=int,
        action='store',
        required=False,
        default=None,
    )
    parser.add_argument(
        '-s',
        '--sticker',
        help=(
            'sticker ID '
            '(see https://developers.line.biz/ja/docs/messaging-api/sticker-list/)'
        ),
        type=int,
        action='store',
        required=False,
        default=None,
    )
    args = parser.parse_args()
    message = args.message
    image_path = args.image
    sticker_package_id = args.stickerpackage
    sticker_id = args.sticker

    bot = LINENotifyBot(access_token=LINE_NOTIFY_ACCESS_TOKEN)
    bot.send(
        message,
        image=image_path,
        sticker_package_id=sticker_package_id,
        sticker_id=sticker_id,
    )


if __name__ == '__main__':
    main()
