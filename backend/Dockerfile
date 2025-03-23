FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies required to build blis and spaCy
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

ENV BLIS_ARCH generic

# Copy backend files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Download and install the spaCy model during build!
RUN python -m spacy download en_core_web_sm

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
