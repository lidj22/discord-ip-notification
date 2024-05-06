FROM python:3.11-alpine

WORKDIR /workdir

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY main.py main.py
CMD python3 main.py