# Python Requests Lib methods

Status: Not started
Tipo: Programação

# [***Requests Lib Python***](https://requests.readthedocs.io/en/latest/)

Biblioteca de interação com ***apis***

Usada para fazer requisições ou seja pegar alguma informação em um site

[***AwesomeAPI***](https://docs.awesomeapi.com.br/)

[***Google Firebase***](https://console.firebase.google.com/)

## Instalação:

```powershell
pip install -r requirements.txt
```

## Tipos:

### GET(Pegar):

```python
from dotenv import load_dotenv
import requests
import os

load_dotenv()

#Pega as informaçoes
# requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
URL_DB = str(os.getenv("URL_DB"))
requisicao = requests.get(URL_DB)

#mostra o status da requisiçao
print(requisicao)

#mostra o conteudo da requisiçao
print(requisicao.json())
```

### POST(Inserir ou criar informação):

```python
from dotenv import load_dotenv
import requests
import os

load_dotenv()

#Coloca informações inseri no database cria
#Requer envio de dados
# requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#Dado que sera inserido no banco de dados obs: id e criado automaticamente
info = '{"nome":"Matheus"}'

URL_DB_ONE = str(os.getenv("URL_DB_ONE"))

requisicao = requests.post(URL_DB_ONE, data=info)

#mostra o status da requisiçao
print(requisicao)

#mostra o conteudo da requisiçao
print(requisicao.json())
```

### PATCH(Atualizar):

```python
from dotenv import load_dotenv
import requests
import os

load_dotenv()

#Atualiza a informação que ja existe no banco
#Requer algun identificador para saber que sera atualizado
# requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#Dado que sera inserido no banco de dados obs: id e criado automaticamente
info = '{"nome":"Matheus2", "sobrenome":"rodrigues", "idade":"29"}'

URL_DB_ONE = str(os.getenv("URL_DB_ONE"))

requisicao = requests.patch(URL_DB_ONE, data=info)

#mostra o status da requisiçao
print(requisicao)

#mostra o conteudo da requisiçao
print(requisicao.json())
```

### DELETE(Deletar):

```python
from dotenv import load_dotenv
import requests

load_dotenv()

#Deleta algum dado do banco de dados
#Requer algun identificador para saber que sera atualizado
# requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#Dado que sera inserido no banco de dados obs: id e criado automaticamente

url_delete = input("digite a url para ser deletada: ")

requisicao = requests.delete(url_delete)

#mostra o status da requisiçao
print(requisicao)

#mostra o conteudo da requisiçao no caso não tera dados pois foi deletado
print(requisicao.json())
```