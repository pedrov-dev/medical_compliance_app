# backend/Dockerfile
FROM python:alpine

# Set the working directory
WORKDIR /app

# Install necessary build utilities.
RUN apt-get update && apt-get install -y gcc

# Copy backend requirements and install them
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the API port
EXPOSE 8000

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
