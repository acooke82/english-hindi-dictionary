FROM python:3.8

EXPOSE 5000

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD tail -f /dev/null