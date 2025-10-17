# --- STAGE 1: The "Workshop" ---
FROM python:3.11-slim as builder

WORKDIR /app

# --- THE FIX ---
# First, copy ONLY the requirements file. This is crucial for caching and availability.
COPY requirements.txt .

# Now, install system dependencies. Separated for clear debugging.
RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Now, install Python dependencies. Separated for clear debugging.
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Now, copy the rest of the application code
COPY . .

# --- STAGE 2: The Final "Showroom" ---
FROM python:3.11-slim

WORKDIR /app

# Copy only the necessary files from the "workshop" stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]