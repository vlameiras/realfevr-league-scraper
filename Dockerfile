# Use an official Python runtime as a parent image
FROM python:3.7-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set the environment variable for Flask to run in production mode
ENV FLASK_APP=app/app.py
# Run the command to start the Flask application
CMD ["flask", "run"]