# Use the official Python image as the base image
FROM python:3.11.6

ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app/

RUN python -m venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:${PATH}"

# Install gunicorn
RUN pip install gunicorn

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the working directory
COPY . .

# Expose the server port
EXPOSE 8080

# Command to start the server
# CMD ["gunicorn", "-b", "8080", "run:app"]
CMD ["python", "./run.py"]

