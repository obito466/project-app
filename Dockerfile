# 1. Base image: small official Python image
FROM python:3.12-slim

# 2. Environment settings
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Working directory inside the container
WORKDIR /app

# 4. Install dependencies first (cached unless requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the application source code
COPY . .

# 6. Run as a non-root user for security
RUN useradd --create-home appuser
USER appuser

# 7. Document the port the app listens on
EXPOSE 5000

# 8. Start the app with a production server (gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
