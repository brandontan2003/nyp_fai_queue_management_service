FROM python:3.11-slim-buster

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENV PYTHONPATH /app

EXPOSE 8080
ENTRYPOINT ["python", "main/controller/QueueManagementController.py"]