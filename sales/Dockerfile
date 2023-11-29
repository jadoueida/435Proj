# sales/Dockerfile
FROM python:3.8

WORKDIR /app

# Copy the entire project directory (including manage.py) into the Docker image
COPY .. /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]


