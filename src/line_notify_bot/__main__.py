import argparse

from line_notify_bot.line_notify_bot import LINENotifyBot


def main():
    parser = argparse.ArgumentParser(
        prog='line_notify_bot',
        usage=(
            'python src/line_notify_bot_line_notify_bot.py -a path/to/access_token '
            '-m <messsage> -i path/to/image -sp <sticker package ID> -s <sticker ID>'
        ),
        description=(
            'Send messages, images, or stickers to a LINE group via LINE Notify.'
        ),
        epilog='end',
        add_help=True,
    )
    parser.add_argument(
        'accesstoken',
        help='path to a file in which an access token is written',
        action='store',
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
        help='sticker package ID',
        type=int,
        action='store',
        required=False,
        default=None,
    )
    parser.add_argument(
        '-s',
        '--sticker',
        help='sticker ID',
        type=int,
        action='store',
        required=False,
        default=None,
    )
    args = parser.parse_args()
    access_token_path = args.accesstoken
    message = args.message
    image_path = args.image
    sticker_package_id = args.stickerpackage
    sticker_id = args.sticker

    """
    message = 'test'
    image_path = 'test.png'
    sticker_package_id = 1
    sticker_id = 13
    """

    with open(access_token_path, 'r') as fin:
        access_token = fin.read().strip()
    bot = LINENotifyBot(access_token=access_token)
    bot.send(
        message,
        image=image_path,
        sticker_package_id=sticker_package_id,
        sticker_id=sticker_id,
    )


if __name__ == '__main__':
    main()
