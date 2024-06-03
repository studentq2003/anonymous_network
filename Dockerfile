# Use the official FastAPI image from tiangolo
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the application code
COPY ./app /app/app

# Copy the .env file
COPY ./.env /app/.env

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
