FROM centos/python-36-centos7 

USER root

COPY ./requirements.txt /app/requirements.txt 

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN python setup.py install

ARG BOT_NAME
ARG BOT_TOKEN
ARG BOT_USERNAME
ARG BOT_PASSWORD
ARG ENABLE_PASSWORD

ENV BOT_NAME=${BOT_NAME:-NOT_DEFINED}\
    BOT_TOKEN=${BOT_TOKEN:-NOT_DEFINED}\
    BOT_USERNAME=${BOT_USERNAME:-NOT_DEFINED}\
    BOT_PASSWORD=${BOT_PASSWORD:-NOT_DEFINED}\
    ENABLE_PASSWORD=${ENABLE_PASSWORD:-NOT_DEFINED}

RUN env  

ENTRYPOINT [ "python" ]

CMD [ "-m", "wibot.wibot" ]
