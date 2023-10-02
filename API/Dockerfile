# Use an official Python runtime as a parent image
FROM python:alpine3.18

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
