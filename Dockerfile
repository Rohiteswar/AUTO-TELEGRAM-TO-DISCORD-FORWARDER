
FROM python:3.11-slim as build

WORKDIR /Auto-Telegram-To-Discord-Forwarder-Bot

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "forward.py" , "config.yaml"]
