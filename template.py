import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "classifier"

list_files = [
    "config/config.yaml",
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for i in list_files:
    
    i = Path(i)    # To convert the path from Linux format to Windows format.
    file_dir, file_name = os.path.split(i)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file {file_name}")
    
    if (not os.path.exists(i)) or (os.path.getsize(i) == 0):
        with open(i, "w") as f:
            pass
            
            logging.info(f"Creating empty file: {i}")
    
    else:
        logging.info(f"{file_name} Already exist")
