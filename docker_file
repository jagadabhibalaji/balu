# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Install any required dependencies
RUN pip install numpy matplotlib

# Clone your source code from Git
RUN git clone https://github.com/jagadabhibalaji/balu.git

# Set the working directory to your project directory
WORKDIR /app/balu

# Run your script (replace with the actual command)
CMD ["python", "github_source_code.py"]
