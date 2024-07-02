import os
from pathlib import Path
import logging#need to login all informatiom

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')#format is asctime and message

#my project name
project_name = "TextSummarizer"
#list of file i need in this project
list_of_files = [
    ".github/workflows/.gitkeep",#use in deployment 
    f"src/{project_name}/__init__.py",
    #project name and constructor file
    f"src/{project_name}/conponents/__init__.py",
    #inside components need a constructor file
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    #in common will write down all the utility
    f"src/{project_name}/logging/__init__.py",
    #logging folder in which have a constructor file
    f"src/{project_name}/config/__init__.py",
    #config folder in which have a constructor file
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    #contain training and prediction pipline
    f"src/{project_name}/entity/__init__.py",
    #entity contain constructor file
    f"src/{project_name}/constants/__init__.py",
    #these are the core files required
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",#build the docker image in source code used in deployment
    "requirements.txt",#contain all the requirements
    "setup.py",
    "research/trials.ipynb",#contain all the notebook experiments

]

#going through the list
for filepath in list_of_files:
    filepath = Path(filepath)#give me all the path one by one
    filedir, filename = os.path.split(filepath)#need to separate file in the folder

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)#if already have folder then it will not create any folder 
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):#if my file size is 0 it will create file
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")#if file is there then will not create file

