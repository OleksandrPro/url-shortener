# File path: src/Dockerfile

# Base image using a lightweight Python image
FROM python:3.11-slim

# Set environment variables for better Python output in containers
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install uv via pip
RUN pip install --no-cache-dir uv

# Copy the dependency management files from the project root
# (We will set the build context to the root in docker-compose)
COPY pyproject.toml uv.lock ./

# Install project dependencies.
# --no-install-project is used because we haven't copied the code yet.
RUN uv sync --no-install-project

# Add the uv virtual environment to the system PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy the actual application code (the src directory) into the container
# Since we already set WORKDIR to /app, this copies src/ into /app/src/
COPY src/ src/

# Expose the port the app runs on (default for FastAPI is often 8000, let's use 80)
EXPOSE 80

# Command to run the application with uvicorn
# We run it as 'src.main:app' because main.py is inside the 'src' package.
# It is vital to set the host to 0.0.0.0 for external connectivity.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]