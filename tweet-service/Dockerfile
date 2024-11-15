# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python application code
COPY tweet_service.py .

# Expose the port the app runs on
EXPOSE 3002

# Run the application
CMD ["python", "tweet_service.py"]
