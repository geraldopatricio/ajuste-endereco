from utils.envhelper import EnvHelper
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class SafeBox:
    def __init__(self):
        self.envhelper = EnvHelper()

        if self.envhelper.getenv('APP_ENV') == 'production':
            self.key_vault_name = self.envhelper.getenv('KEY_VAULT_NAME')
            self.kv_uri = 'https://' + self.key_vault_name + '.vault.azure.net'

            self.credential = DefaultAzureCredential()
            self.client = SecretClient(vault_url=self.kv_uri, credential=self.credential)

    def get_secret(self, secret: str):
        if self.envhelper.getenv('APP_ENV') == 'production':
            return self.client.get_secret(secret).value
        
        return self.envhelper.getenv(secret.replace('-', '_'))

