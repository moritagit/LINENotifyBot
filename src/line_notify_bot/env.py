import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

LINE_NOTIFY_ACCESS_TOKEN = os.getenv('LINE_NOTIFY_ACCESS_TOKEN', None)
