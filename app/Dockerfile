# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Create logs directory
RUN mkdir -p /app/logs

# Run as non-root user
RUN useradd -m myuser
USER myuser

# Expose port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]