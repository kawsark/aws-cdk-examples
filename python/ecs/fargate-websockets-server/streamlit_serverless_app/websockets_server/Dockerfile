# syntax=docker/dockerfile:1.4
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8765
EXPOSE 8080
COPY . .
ENTRYPOINT ["python", "server.py"]
