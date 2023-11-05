# Use the official Python image as the base image
# FROM python:3.11.6
FROM python:3.9

# Set the working directory in the container
WORKDIR /app/
COPY . .

RUN python -m venv /opt/env

# # Enable venv
ENV PATH="/opt/env/bin:${PATH}"

# # Install gunicorn
# RUN pip install gunicorn

# # Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Add the 'cv2' directory to Python's module search path within the virtual environment
RUN echo 'import sys; sys.path.append("/app/cv2")' >> /opt/env/lib/python3.9/site-packages/cv2_path.pth

# Expose the server port
EXPOSE 8080

# Command to start the server
# CMD ["gunicorn", "-b", "8080", "run:app"]
CMD ["python3", "./run.py"]

