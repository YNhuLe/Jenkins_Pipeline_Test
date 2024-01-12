# Example Dockerfile
FROM python:3.11

# Install dependencies for the file
RUN pip install pytest

# Set the working directory
WORKDIR /app

# Copy your project files into the container
COPY . /app

