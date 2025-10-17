# --- STAGE 1: The "Workshop" ---
# This is where we install all the heavy dependencies
FROM python:3.11-slim as builder

# Set the working directory
WORKDIR /app

# Install build tools that might be needed for some libraries
# and then install our Python packages
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# --- STAGE 2: The Final "Showroom" ---
# This is our final, lean image. We start fresh.
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy only the installed packages from the "workshop" stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy only the application code from the "workshop" stage
COPY --from=builder /app /app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
