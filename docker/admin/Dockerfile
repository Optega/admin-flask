FROM python:3.9-slim-buster

WORKDIR /app

COPY admin/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY admin .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
