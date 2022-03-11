import csv
import sys
import asyncio
import os
import re

from tqdm import tqdm

from utils.pier import PierService

try:
    handle = open(os.sep + "src" + os.sep + "enderecos" + os.sep + "data.csv", 'r')
    reader = csv.DictReader(handle, delimiter=",")
except:
    sys.exit("Ocorreu um problema ao ler os dados", file=sys.stderr)

pier = PierService("ajuste_logradouro")
i = 0

for row in tqdm(reader, "AJUSTANDO ENDEREÇOS", colour="yellow"):
    i += 1
    id_endereco = row["ID_ENDERECO"]
    logradouro = re.sub(' +', ' ', row["DS_LOGRADOURO"].strip())
    id_pessoa = row["ID_PESSOA_FISICA"]
    uf = row["DS_UF"].strip()
    cidade = re.sub(' +', ' ', row["DS_CIDADE"].strip())
    bairro = re.sub(' +', ' ', row["DS_BAIRRO"].strip())
    tipo_endereco = row["DS_TIPO_ENDERECO"].strip()
    numero_endereco = row["NU_ENDERECO"]
    complemento = re.sub(' +', ' ', row["DS_COMPLEMENTO"].strip())
    cep = str(row["CD_CEP"]).zfill(8)

    if (numero_endereco == "NULL"):
        print(id_endereco, logradouro)
        numero_endereco = 0

    if (tipo_endereco == "RESIDENCIAL"):
        id_tipo_endereco = 1
    elif(tipo_endereco == "COMERCIAL"):
        id_tipo_endereco = 2
    elif(tipo_endereco == "CORRESPONDENCIA"):
        id_tipo_endereco = 3

    print(id_endereco, logradouro, id_pessoa, uf, cidade, bairro, id_tipo_endereco, numero_endereco, cep, complemento)

    result = pier.ajuste_logradouro(id_endereco, logradouro, id_pessoa, uf, cidade, bairro, id_tipo_endereco, numero_endereco, cep, complemento)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(result)
    
loop.close()
