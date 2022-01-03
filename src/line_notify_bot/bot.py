# -*- coding: utf-8 -*-


"""line_notify_bot.py

Send messages, images, or stickers to a LINE group via LINE Notify.
This bot can't accept messages, i.e., is not interactive.
Access token can be obtrained from: https://notify-bot.line.me/ja/
Sticker and its package IDs can be chosen from:
https://developers.line.biz/ja/docs/messaging-api/sticker-list/
"""


import traceback
from pathlib import Path
from typing import Callable, Optional, Union

import requests


class LINENotifyBot(object):
    """
    Sends message, image, and sticker to a LINE group.
    Access token can be obtrained from: https://notify-bot.line.me/ja/

    Paramteres:
        access_token: Access token necessary to tap LINE Notify API.

    Attributes:
        __headers: Necessary to send request to LINE Notify.
        API_URL: URL of LINE Notify API.
    """

    API_URL = 'https://notify-api.line.me/api/notify'

    def __init__(self, access_token: str) -> None:
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(
        self,
        message: str,
        image: Optional[Union[str, Path]] = None,
        sticker_package_id: Optional[int] = None,
        sticker_id: Optional[int] = None,
    ) -> requests.models.Response:
        """
        Sends message, image, and sticker to a LINE group designated by access token.
        Sticker and its package IDs can be chosen from:
        https://developers.line.biz/ja/docs/messaging-api/sticker-list/

        Parameters:
            message: Sent message. Maximum length is 1000.
                If is None, message can't be sent.
                In this situation, image and sticker also can't be sent.
            image: Path to image to send.
                Available extentions are only png or jpeg.
                There is a limitation to the number of images
                which can be sent in one hour (1,000 images by default).
            sticker_package_id: ID of sticker package.
                If set to None, only message is sent.
                If set to unregistered integer, even message can't be sent.
            sticker_id: ID of sticker.
                If set to None, only message is sent.
                If set to unregistered integer, even message can't be sent.

        Returns:
            response: Response of the `requests.post`.
        """
        if not message:
            raise ValueError('message must not be None.')
        if sticker_package_id:
            if not sticker_id:
                raise ValueError(
                    '`sticker_package_id` is input, but `sticker_id` is not input.'
                )
        if sticker_id:
            if not sticker_package_id:
                raise ValueError(
                    '`sticker_id` is input, but `sticker_package_id` is not input.'
                )

        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
        }
        files = {}

        if image:
            image_path = Path(image)

            if not image_path.exists():
                raise ValueError(f'The input image file does not exist: `{image_path}`')

            extention = image_path.suffix
            if not extention:
                raise ValueError(
                    'The `image` must not be a directory, '
                    f'but the input was: {image_path}'
                )
            elif extention not in ['.png', '.jpg']:
                raise ValueError(
                    'The input `image` must have `.png` or `.jpg` as its extention, '
                    f'but `{extention}` file was input.'
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

    def notify_error(self, success_message: Optional[str] = None) -> Callable:
        """
        A decorator for a function to notify errors occurred when executing
        the function.

        Parameters:
            success_message: A message sent when the function was successfully executed.
                If set to `None` (default), default message will be sent.
                If set to empty string (''), no message will be sent.

        Example:
            ```
            >>> @bot.notify_error
            ... def test(n):
            ...     if n < 10:
            ...         return n
            ...     else:
            ...         raise ValueError('`n` must be lesser than 10.')
            >>>
            >>> test(2)
            # 'no error occurred when executing `test`' will be sent.
            2
            >>> test(12)
            # '`n` must be lesser than 10.' will be sent.
            ```
        """

        def decorator(func: Callable) -> Callable:
            nonlocal success_message

            if success_message is None:
                success_message = f'no error occurred when executing `{func.__name__}`'

            def _wrapper(*args, **kwargs):
                try:
                    r = func(*args, **kwargs)
                except BaseException as e:
                    t = traceback.format_exc()
                    message = f'error occured when executing `{func.__name__}`\n\n'
                    message += f'```\n{t}```'
                    self.send(message)
                    raise e
                else:
                    if success_message:
                        self.send(success_message)
                return r

            return _wrapper

        return decorator
