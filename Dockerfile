FROM centos/python-36-centos7

COPY ./requirements.txt /bot/requirements.txt

WORKDIR /bot

RUN pip install -r requirements.txt

COPY . /bot

CMD mkdir -p /opt/wibot

ENTRYPOINT [ "python" ]

CMD [ "-m", "wibot.wibot" ]