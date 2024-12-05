# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"

# Copy only requirements to cache dependencies
COPY pyproject.toml poetry.lock* ./

# Configure Poetry:
# - Do not create a virtual environment inside the Docker container
# - Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Use uvicorn to run the application
CMD ["uvicorn", "animals_api.main:app", "--host", "0.0.0.0", "--port", "8000"]