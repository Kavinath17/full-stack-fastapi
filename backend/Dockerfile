# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy dependencies file and install packages
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry && poetry install --no-root

# Copy application code
COPY . /app

# Expose FastAPI port
EXPOSE 8000

# Command to run app
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
