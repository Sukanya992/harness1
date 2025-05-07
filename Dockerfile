# Use a minimal Alpine image for Python
FROM python:3.9-alpine

# Install system dependencies for Python packages
RUN apk add curl git unzip wget zip

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
