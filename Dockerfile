# Use Python 3.9 base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy only necessary files, excluding sensitive ones
COPY . . 

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the command to run the app
CMD ["python", "app.py"]
