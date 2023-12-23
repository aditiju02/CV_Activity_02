FROM python:3.11.6

# RUN pip install --upgrade pip
RUN pip install --upgrade pip
# Set the working directory in the container
WORKDIR /app/
COPY . .

RUN python -m venv /opt/env

# # Enable venv
ENV PATH="/opt/env/bin:${PATH}"

# # Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Add the 'cv2' directory to Python's module search path within the virtual environment
# RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0
# Expose the server port
EXPOSE 8080

# Command to start the server
CMD ["python3", host="0.0.0.0", "./run.py"]
