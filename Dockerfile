FROM centos/python-36-centos7 

USER root

COPY ./requirements.txt /app/requirements.txt 

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN python setup.py install

CMD mkdir -p /opt/wibot

ENTRYPOINT [ "python" ]

CMD [ "-m", "wibot.wibot" ]
