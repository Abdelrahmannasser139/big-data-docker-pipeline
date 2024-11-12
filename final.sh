#!/bin/bash

# Define container and local directories
CONTAINER_DIR="/home/doc-bd-a1"
LOCAL_DIR="."

# Copy output files
docker cp bd-a1-container:${CONTAINER_DIR}/res_dpre.csv ${LOCAL_DIR}
docker cp bd-a1-container:${CONTAINER_DIR}/eda-in-1.txt ${LOCAL_DIR}
docker cp bd-a1-container:${CONTAINER_DIR}/eda-in-2.txt ${LOCAL_DIR}
docker cp bd-a1-container:${CONTAINER_DIR}/eda-in-3.txt ${LOCAL_DIR}
docker cp bd-a1-container:${CONTAINER_DIR}/vis.png ${LOCAL_DIR}
docker cp bd-a1-container:${CONTAINER_DIR}/k.txt ${LOCAL_DIR}

echo "Files copied to the local machine."
