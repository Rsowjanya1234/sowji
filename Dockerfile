FROM python:3.8-slim
RUN pip install xmltodict
# Set the working directory in the container
WORKDIR /testwork

 

COPY parser.xml /testwork/
# Copy the Python script to the container
COPY xml2.py /testwork/

 

# Run the Python script when the container launches
ENTRYPOINT ["python", "/testwork/xml2.py"]
