import os
from dotenv import load_dotenv

class EnvHelper:
    def __init__(self):
        load_dotenv()

        if os.getenv("APP_ENV") == 'production':
            load_dotenv (os.path.dirname(os.getcwd()) + os.sep + '.env', override=True)

    def getenv(self, key: str):
        return os.getenv(key)