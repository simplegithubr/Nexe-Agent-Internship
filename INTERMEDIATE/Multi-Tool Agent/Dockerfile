FROM python:3.10-slim

WORKDIR /app

# Copy backend requirements and install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project structure
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Create database directory
RUN mkdir -p /app/backend/database

# Set working directory to backend
WORKDIR /app/backend

# Expose port 7860 (Hugging Face Spaces default)
EXPOSE 7860

# Set environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1
ENV DATABASE_PATH=/app/backend/database/agent_data.db

# Run the application
CMD ["python", "app.py"]
