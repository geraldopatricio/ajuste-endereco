from utils.safebox import SafeBox
import requests
import json
import sys

class PierService:
    def __init__(self, script_name):
        self.safebox = SafeBox()
        self.url = self.safebox.get_secret('API-PIER-URL')
        self.access_token = self.safebox.get_secret('API-PIER-TOKEN')
        self.client_id = self.safebox.get_secret('API-PIER-CLIENTID')
        self.pier_report = None
        self.script_name = script_name

        try:
            log_file_name = "pierReport.log"
            self.pier_report = open(log_file_name, 'a+')
        except:
            sys.exit("Ocorreu um erro na abertura do arquivo de log dos clientes")

        self.pier_report.write(f"\n\n[[ {self.script_name.upper()} ]]\n\n")

    def pier_headers(self):
        headers = {
            "access_token": self.access_token,
            "client_id": self.client_id,
            "Content-Type": "application/json",
        }
        return headers

    def close_log(self):
        self.pier_report.close()

    async def ajuste_logradouro(self, id_endereco, logradouro, id_pessoa, uf, cidade, bairro, id_tipo_endereco, numero_endereco, cep, complemento) -> dict:
        body = { "id": id_endereco, 
        "logradouro": logradouro,
        "idPessoa": id_pessoa,
        "idTipoEndereco": id_tipo_endereco,
        "cidade": cidade,
        "bairro": bairro,
        "numero": numero_endereco,
        "complemento": complemento,
        "cep": cep,
        "uf": uf }
        headers = self.pier_headers()
        response = requests.put(url=f"{self.url}/enderecos?id={id_endereco}&idPessoa={id_pessoa}&idTipoEndereco={id_tipo_endereco}&logradouro={logradouro}&bairro={bairro}&cidade={cidade}&uf={uf}&numero={numero_endereco}&complemento={complemento}&cep={cep}", data=json.dumps(body), headers=headers)
        result = None

        if hasattr(response, 'status_code') and response.status_code == 200:
            result = json.loads(response.text)
            self.pier_report.write(f"[SUCESSO NO AJUSTE DE ENDEREÇO] {response.text}\n")
            print("SUCESSO NO AJUSTE DE ENDEREÇO")
        else:
            self.pier_report.write(f"[FALHA NO AJUSTE DE ENDEREÇO] {response.text}\n")
            print("FALHA NO AJUSTE DE ENDEREÇO")

        return result