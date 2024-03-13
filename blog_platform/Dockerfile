# Set the entrypoint script to be executable
# Run this command before executing the docker build command!
# chmod +x ./entrypoint.sh

# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
# Prevents potential problems with writing .pyc files to volume
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr - helps for debugging
ENV PYTHONUNBUFFERED 1

# Install PostgreSQL client
# We want to ping the database in entrypoint shell before manipulating it
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /code

# Copy project files
COPY . /code/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/code/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]