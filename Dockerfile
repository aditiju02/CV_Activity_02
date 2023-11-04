# Use the official Python image as the base image
# FROM python:3.11.6
FROM python:3.9
RUN pip install --upgrade pip
# Set the working directory in the container
WORKDIR /app/
COPY . .

# Update the PATH to include the venv's bin directory
# ENV PATH="/app/venv/bin:${PATH}"

RUN python -m venv /opt/env

# # Enable venv
ENV PATH="/opt/env/bin:${PATH}"

# # Install gunicorn
# RUN pip install gunicorn

# # Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install opencv-python
# # Copy the application files into the working directory
# COPY . .

# Expose the server port
EXPOSE 8080

# Command to start the server
# CMD ["gunicorn", "-b", "8080", "run:app"]
CMD ["python3", "./run.py"]

