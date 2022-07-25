## Minha Agenda 🗓️

---

[![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/docs)  [![Django](https://img.shields.io/badge/Django-3.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13.0-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/) [![Docker](https://img.shields.io/badge/Docker-20.10-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/) [![License](https://img.shields.io/badge/License-MIT-8CA1AF?style=for-the-badge&logoColor=white)](https://opensource.org/licenses/MIT)

---

## Variáveis de Ambiente

O projeto conta com um arquivo `.env`, que armazena as variáveis de ambiente utilizadas pela aplicação e pelo Docker.

- `.env` - Armazena as variáveis do ambiente WEB e Banco de Dados.

## Arquivo `.env`

| Variável | Tipo | Valor Padrão | Descrição |
| -- | -- | -- | -- |
| SECRET_KEY | ```string``` | ```None``` | Define a chave secreta de instalação do Django. Usada para fornecer uma assinatura de criptografia e deve ser definida com um valor único e imprevisível.
| DEBUG | ```boolean``` | ```False``` | Define se o debug estará ativo ou não. Em produção é recomendado deixar ```False```.
| ALLOWED_HOSTS | ```string``` | ```'*'``` | Uma lista com os hosts/nomes de domínio que o Django servirá a aplicação.
| POSTGRES_DB | ```string``` | ```None``` | Nome do banco de dados que será criado e posteriormente será utilizado pelo Django.
| POSTGRES_USER | ```string``` | ```None``` | Nome do usuário que será utilizado na configuração do banco de dados e posteriormente será utilizado pelo Django para se conectar ao banco de dados.
| POSTGRES_PASSWORD | ```string``` | ```None``` | Senha do usuário que será utilizado na configuração do banco de dados e posteriormente será utilizado pelo Django para se conectar ao banco de dados.
| POSTGRES_HOST | ```string``` | ```db``` | Nome do host onde o banco de dados está sendo executado.
| POSTGRES_PORT | ```string``` | ```5432``` | Porta utilizada pelo banco de dados.
| LANGUAGE_CODE | ```string``` | ```pt-br``` | Idioma padrão da aplicação.
| TIME_ZONE | ```string``` | ```America/Sao_Paulo``` | Time zone da aplicação.

## Licença

Distribuído sob a licença MIT. Consulte o arquivo ```LICENSE.md``` para mais informações.

## Executando

[Instale o Docker](https://docs.docker.com/get-docker/)

Crie o arquivo ```.env``` no diretório raiz da aplicação. Para criar o arquivo, utilize os mesmos nomes de variáveis informados acima.

Execute ```docker-compose build``` para compilar o container e a aplicação.

Execute ```docker-compose up``` para iniciar o servidor.

Pronto, a aplicação está em funcionamento!

## Executando sem o Docker

Caso não queira utilizar o Docker para rodar a aplicação, você pode rodar localmente utilizando o servidor de desenvolvimento servido pelo Django.

- 1º Passo: Crie um ambiente virtual para instalar os pacotes necessários para executar a aplicação. Dentro da pasta do projeto execute o comando.

No Windows:
```
    python -m virtualenv -p python3 venv
```

No Linux:
```
    python3 -m virtualenv -p python3 venv
```

- 2º Passo: Ative o ambiente virtual.

No Windows:
```
    .\venv\Scripts\activate
```

No Linux:
```
    source venv/bin/activate
```

- 3º Passo: Instale os pacotes.

```
    pip install -r requirements.txt
```

- 4º Passo: Crie as migrations.

```
    python manage.py makemigrations
```

- 5º Passo: Rode as migrations.

```
    python manage.py migrate
```

- 6º Passo: Execute o servidor de desenvolvimento.

```
    python manage.py runserver
```

Pronto! A aplicação estará sendo executada no endereço: ```http://127.0.0.1:8000```
