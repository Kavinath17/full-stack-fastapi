# Step 1: Use Python base image
FROM python:3.14-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Install git (needed for pip install from GitHub)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Step 4: Copy dependency files
COPY requirements.txt .

# Step 5: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy project files
COPY . .

# Step 7: Expose FastAPI port
EXPOSE 8000

# Step 8: Run FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
