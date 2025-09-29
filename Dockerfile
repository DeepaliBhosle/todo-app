# Use lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY todo.py .

# Run the app
CMD ["python", "todo.py"]
