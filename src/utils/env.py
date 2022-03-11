import os
from dotenv import load_dotenv


def load_script_environment(root_path: str):
    load_dotenv(root_path + os.sep + '.env')
    if os.getenv('APP_ENV') == 'production':
        load_dotenv(os.sep + 'scripts' + os.sep + '.env', override=True)
