FROM python:3.9-alpine3.16

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 2000

CMD ["python","./main.py"]
