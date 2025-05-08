# Use official Python 3.9 base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only necessary files (add .dockerignore for safety)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
