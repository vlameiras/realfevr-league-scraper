# Starting from the Python 3.9 base image
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set the environment variable for the Flask app
ENV FLASK_APP=app.app

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]