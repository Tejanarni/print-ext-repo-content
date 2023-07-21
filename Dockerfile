# Use the official Python image as the base image
FROM python:3.9-slim

# Install git and other system dependencies
RUN apt-get update && apt-get install -y git

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and requirements file to the working directory
COPY app.py requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Git executable
ENV GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git

# Run the Python script when the container starts
CMD ["python", "app.py"]
