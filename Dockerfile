# configura a imagem Docker e a tag que iremos utilizar
# alpine é uma versão leve do Linux para executar em Docker containers
FROM python:3.9-alpine3.13

# responsável por manter esta imagem do Docker
LABEL maintainer="Fabiano Papaiz"

# RECOMENDAVEL: diz para nao armazenar o OUTPUT em buffer e imprimir direto no console, 
# evitando assim atrasos de mensagens, vendo os logs imediatamente na tela quando eles ocorrerem
ENV PYTHONNONBUFFERED=1 

# Copia os requirements necessarios para executar a aplicacao
COPY ./requirements.txt /tmp/requirements.txt

# Copia os requirements de DEVOLOPMENT necessarios para executar a aplicacao
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# copia a pasta onde esta a nossa aplicacao
COPY ./app /app	

# pasta onde serao excutados os comandos que enviarmos para a imagem Docker
WORKDIR /app

# expoe a porta que serah utilizada para acessar a imagem Docker do nosso computador
EXPOSE 8000

# argumentos da linha de comando do build
# Serah mudado pra "true" dentro do "docker-compose.yml"
ARG DEV=false

# Executa os comandos:
# 1. cria ambiente virtual "py"
# 2. faz upgrade no PIP
# 3. instala pacote para acessar o BD PostgreSQL a partir do Django
# 4. instala os pacotes necessarios para instalar o postgres-client de forma que poderemos remove-los depois
# 5. instala os pacotes definidos em requirements.txt
# 6. instala SE PRECISAR os pacotes definidos em requirements.dev.txt
# 7. exclui pasta "tmp"
# 8. remove os pacotes necessarios para compilar o postgresql-client
# 9. cria o usuario "django-user" sem senha e sem pasta "home" 
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client &&\
    apk add --update --no-cache --virtual .tmp-build-deps \ 
        build-base postgresql-dev musl-dev &&\
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# adiciona a pasta dos executaveis do python nna variavel de ambiente "PATH" 
ENV PATH="/py/bin:$PATH"

# a partir deste ponto, mude para o usuario especificado
# Obs: ateh aqui os comandos foram executados como usuario "root"
USER django-user