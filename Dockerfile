# Use an official Python image as a base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . .

# Install any dependencies from requirements.txt (if applicable)
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the application
CMD ["python", "todo.py"]

