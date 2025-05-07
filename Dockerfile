FROM python:3.9-slim

# Update and upgrade system packages for security patches (only for Debian-based images)
RUN apt-get update && apt-get upgrade -y

# Set working directory
WORKDIR /app

# Copy the app code
COPY app.py .

# Install Flask and upgrade setuptools
RUN pip install --upgrade setuptools && pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

