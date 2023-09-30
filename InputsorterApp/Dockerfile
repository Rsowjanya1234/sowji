# Use an official Python runtime as a parent image

FROM python:3.8-slim

# Set the working directory in the container

WORKDIR /testwork

 

# Copy the current directory contents into the container at /testwork

COPY ascend_descend_sorter.py /testwork/
 

# Define the command to run your application

ENTRYPOINT ["python", "/testwork/ascend_descend_sorter.py"]
