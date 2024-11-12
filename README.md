Big Data Assignment - Dockerized Data Processing Pipeline
Project Overview
This project implements a data processing pipeline within a Docker container using Python. It includes steps for data loading, preprocessing, exploratory data analysis (EDA), visualization, and K-means clustering on a simple dataset. The processed outputs are saved in a directory on the local machine.

Requirements
Docker
Python3 (with pandas, numpy, seaborn, matplotlib, scikit-learn, and scipy libraries)
Project Structure
php
Copy code
bd-a1/
├── <dataset-name>.csv       # Dataset to be processed
├── Dockerfile               # Docker setup and environment specifications
├── final.sh                 # Script to copy outputs from container to host and stop container
├── service-result/          # Directory to store output files after processing
└── README.md                # Project documentation
Dockerfile
The Dockerfile sets up the container environment:

Starts with an Ubuntu base.
Installs necessary packages (Python3, pip, and Python libraries).
Copies the dataset to the container at /home/doc-bd-a1/.
Opens the bash shell on startup.
Instructions
Clone or Setup the Directory
Create a directory named bd-a1/, download the dataset (e.g., iris.csv), and place it in this directory.

Create Docker Image
Build the Docker image with the following command:

bash
Copy code
docker build -t bd-a1-image .
Run Docker Container
Start the container with:

bash
Copy code
docker run -it --name bd-a1-container bd-a1-image
This will launch an interactive session in the container.

Inside the Container
Inside the container, run the following command to initiate the pipeline, replacing <dataset-name>.csv with your dataset name:

bash
Copy code
python3 load.py <dataset-name>.csv
Pipeline Steps
The pipeline executes the following steps in sequence:

load.py: Loads the dataset into a DataFrame.
dpre.py: Cleans, transforms, reduces, and discretizes the data, saving it as res_dpre.csv.
eda.py: Performs EDA and saves insights in eda-in-1.txt, eda-in-2.txt, and eda-in-3.txt.
vis.py: Creates a scatter plot and saves it as vis.png.
model.py: Performs K-means clustering and saves cluster counts in k.txt.
Transfer Outputs to Local Machine
Run the final.sh script on your local machine to copy the output files from the container to bd-a1/service-result/:

bash
Copy code
./final.sh
View Results
Output files are saved in the bd-a1/service-result/ directory, including:

eda-in-1.txt, eda-in-2.txt, eda-in-3.txt: Text files with EDA insights.
vis.png: Scatter plot visualization.
k.txt: Cluster counts from K-means.
Docker Commands Summary
Build the Docker Image

bash
Copy code
docker build -t bd-a1-image .
Run the Docker Container

bash
Copy code
docker run -it --name bd-a1-container bd-a1-image
Execute Pipeline
Inside the container:

bash
Copy code
python3 load.py <dataset-name>.csv
Copy Outputs and Stop Container
Run this on your local machine:

bash
Copy code
./final.sh
Additional Notes
Ensure all Python files (load.py, dpre.py, eda.py, vis.py, model.py) are created inside the container, in /home/doc-bd-a1/, before executing load.py. This pipeline generates output files automatically and transfers them from the container to your local system for easy access.

