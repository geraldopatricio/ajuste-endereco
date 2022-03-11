FROM python:3.6.9-slim-buster

ENV ENV=production

WORKDIR /src
COPY ./src .
COPY ./requirements.txt .

RUN apt-get update \
 && apt-get install -y \
 --no-install-recommends \
 --no-install-suggests \
 rclone \ 
 && apt-get autoclean \
 && apt-get autoremove 

RUN pip install -r requirements.txt && rm requirements.txt

CMD ["python", "/src/index.py"]
