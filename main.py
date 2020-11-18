import sys
import time
import os
from utils.Types import ProjectType
from utils.File import File

PROJECTS_PATH = "E:\\Documents\\Projects"

def main():
    try:
        project_type = sys.argv[1]
        project_name = sys.argv[2]
    except IndexError:
        raise ValueError("Plese provide us a name and a type for your project..")
    project = [project_name, project_type]
    file = File(project)
    try:
        if sys.argv[3] == "-git":
            file.add_to_repo = True
    except IndexError:
        pass
    print(f"Creating the {project_type} project...")
    os.chdir(PROJECTS_PATH)
    file.create()
    print("Project Created.")
    path = PROJECTS_PATH.replace("\\", "/")
    print(f"You will find it on: '{path}/{project_name}'")


if __name__ == "__main__":
    main()