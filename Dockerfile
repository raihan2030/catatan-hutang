# Gunakan base image Python
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh proyek ke dalam image
COPY . .

# Expose port yang akan digunakan oleh aplikasi
EXPOSE 8000