# Dockerfile

# Base image
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y python3-pandas python3-numpy python3-matplotlib python3-scipy python3-sklearn python3-seaborn

RUN mkdir -p /home/doc-bd-a1

COPY titanic.csv /home/doc-bd-a1/

CMD ["bash"]
