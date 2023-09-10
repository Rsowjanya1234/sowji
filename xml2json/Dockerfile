# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python scripts and server configurationfile into the container
COPY xml_to_json.py /app/
COPY input.xml /app/

# Command to run the server script
ENTRYPOINT ["python", "/app/xml_to_json.py"]
