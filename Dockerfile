FROM python:3.8-alpine

WORKDIR /fibonacci_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY  ./app ./app
COPY  ./static ./static
COPY  ./templates ./templates
EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=80"]
