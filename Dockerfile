# Dockerfile

# Base image
FROM ubuntu:latest

# Install Python and other dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y python3-pandas python3-numpy python3-matplotlib python3-scipy python3-sklearn python3-seaborn

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1

# Move the dataset into the container
COPY titanic.csv /home/doc-bd-a1/

# Set the container to open bash on startup
CMD ["bash"]
