# -*- coding: utf-8 -*-


"""line_notify_bot.py

Send messages, images, or stickers to a LINE group via LINE Notify.
This bot can't accept messages, i.e., is not interactive.
Access token can be obtrained from: https://notify-bot.line.me/ja/
Sticker and its package IDs can be chosen from:
https://devdocs.line.me/files/sticker_list.pdf
"""


from pathlib import Path

import requests


class LINENotifyBot:
    """Sends message, image, and sticker to a LINE group.
    Access token can be obtrained from: https://notify-bot.line.me/ja/

    Args:
        access_token (str):
            Access token necessary to tap LINE Notify API.

    Attributes:
        __headers (dict): Necessary to send request to LINE Notify.
        API_URL (str): URL of LINE Notify API.
    """

    API_URL = 'https://notify-api.line.me/api/notify'

    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(self, message, image=None, sticker_package_id=None, sticker_id=None):
        """Sends message, image, and sticker to a LINE group designated by access token.
        Sticker and its package IDs can be chosen from:
        https://devdocs.line.me/files/sticker_list.pdf

        Args:
            message (str): Sent message. Maximum length is 1000.
                If is None, message can't be sent.
                In this situation, image and sticker also can't be sent.
            image (str or pathlib.Path): Path to image to send.
                Available extentions are only png or jpeg.
                There is a limitation to the number of images
                which can be sent in one hour (1,000 images by default).
                Defaults to None.
            sticker_package_id (int): ID of sticker package.
                If set to None, only message is sent.
                If set to unregistered integer,
                even message can't be sent.
                Defaults to None.
            sticker_id (int): ID of sticker.
                If set to None, only message is sent.
                If set to unregistered integer,
                even message can't be sent.
                Defaults to None.

        Returns:
            response (requests.models.Response): Response of the requests.post.
        """
        if not message:
            raise ValueError('message must not be None.')
        if not isinstance(message, str):
            raise TypeError(
                f'message must be str. But input message type was: {type(message)}'
            )

        if sticker_package_id:
            if isinstance(sticker_package_id, int):
                pass
            elif isinstance(sticker_package_id, str):
                if sticker_package_id.isdecimal():
                    sticker_package_id = int(sticker_package_id)
                else:
                    raise ValueError(
                        'sticker_package_id can be an arabic decimal str, '
                        f'but the input was: {sticker_package_id}.'
                    )
            else:
                raise TypeError(
                    'sticker_package_id must be int or arabic decimal str, '
                    f'but the input type was: {type(sticker_package_id)}'
                )

            if not sticker_id:
                raise ValueError(
                    'sticker_package_id is input, but sticker_id is not input.'
                )

        if sticker_id:
            if isinstance(sticker_id, int):
                pass
            elif isinstance(sticker_id, str):
                if sticker_id.isdecimal():
                    sticker_id = int(sticker_id)
                else:
                    raise ValueError(
                        'sticker_id can be an arabic decimal str, '
                        f'but the input was: {sticker_id}.'
                    )
            else:
                raise TypeError(
                    'sticker_id must be int or arabic decimal str, '
                    f'but the input type was: {type(sticker_id)}'
                )

            if not sticker_package_id:
                raise ValueError(
                    'sticker_id is input, but sticker_package_id is not input.'
                )

        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
        }
        files = {}

        if image:
            if isinstance(image, str):
                image_path = Path(image)
            elif isinstance(image, Path):
                image_path = image
            else:
                raise TypeError(
                    'image must be str or pathlib.Path. '
                    f'But input image type was: {type(image)}'
                )

            if not image_path.exists():
                raise ValueError(f'image file does not exist: {image_path}')

            extention = image_path.suffix
            if not extention:
                raise ValueError(
                    f'image must not be a directory. But the input was: {image_path}'
                )
            elif extention not in ['.png', '.jpg']:
                raise ValueError(
                    'image must have .png or .jpg as its extention. '
                    f'But {extention} file was input.'
                )

            files = {'imageFile': open(str(image_path), 'rb')}

        response = requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
        )

        if not response.ok:
            raise Exception(
                'The message, image, and sticker can not be sent for some reason. '
                'Maybe you input wrong sticker (or sticker package) ID.'
            )

        return response
