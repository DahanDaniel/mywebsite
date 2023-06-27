# Use an official Python runtime as a parent image
FROM python:3.8.10

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /mywebsite

# Set the working directory to /mywebsite
WORKDIR /mywebsite

# Copy the current directory contents into the container at /mywebsite
ADD . /mywebsite/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
