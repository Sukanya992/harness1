# Use an official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the app code
COPY app.py .

# Install Flask
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
