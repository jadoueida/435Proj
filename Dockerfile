# Use the official Python image as a base image
FROM python:3.8

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port that the app will run on
EXPOSE 8000

# Start the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
