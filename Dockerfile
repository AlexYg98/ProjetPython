FROM node:latest

RUN apt update && apt install -y git bash sudo curl

COPY main.py /app/

WORKDIR /app

CMD ["python", "/app/main.py"]