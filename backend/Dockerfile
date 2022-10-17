FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#EXPOSE 8080
CMD ["uvicorn", "application:app", "--host", "0.0.0.0", "--port", "8080"]
