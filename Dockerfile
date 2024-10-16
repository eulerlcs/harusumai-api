FROM python:3.11-alpine


WORKDIR /app

COPY requirements.txt app config ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
