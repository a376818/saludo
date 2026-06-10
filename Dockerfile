FROM python:3.14.0

ENV TZ=America/Mexico_City

RUN apt-get update && \
    apt-get install -y git tzdata

WORKDIR /app

RUN git clone https://github.com/a376818/saludo.git .

CMD [ "python", "./saludo.py" ]