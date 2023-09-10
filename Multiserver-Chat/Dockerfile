# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python scripts and server configurationfile into the container
COPY client.py /app/
COPY server1.py /app/
COPY server2.py /app/
COPY ip_port_config.json /app/

# Command to run the server script
ENTRYPOINT ["python", "/app/server1.py", "&", "python", "/app/server2.py"]


