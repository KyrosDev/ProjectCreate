import sys
import time
import os
from utils.File import File
from utils.Types import ProjectType

PROJECTS_PATH = "E:\\Documents\\Projects"

PROJECTS_TYPES = [
    "flutter",
    "node",
    "vue",
    "python",
    "dart"
]

COLORS = {
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "black": "\u001b[30m",
    "yellow": "\u001b[33m",
    "reset": "\u001b[0m",
    "white": "\u001b[37m",
    "cyan": "\u001b[36m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35;1m",
}

TYPES = {
    "bold": "\u001b[1m",
    "underline": "\u001b[4m",
    "reversed": "\u001b[7m",
}

def main():
    os.system("cls")
    print("{}{}{}CREATE PROJECT".format(COLORS["green"], TYPES["reversed"], TYPES["bold"]))
    print("{}Create a project in few seconds with just one command!!!".format(COLORS["reset"]))
    print("{} - Select your project type: {}".format(COLORS["magenta"], COLORS["reset"]))
    print("""    - [0] Flutter App
    - [1] NodeJS Server
    - [2] VueJS WebApp
    - [3] Python Module
    - [4] Dart Module
""")
    number = int(input("Select type: "))
    project_type = PROJECTS_TYPES[number]
    if (number > 4):
        print("Select a project in range 0 - 4")
        main()
    project_name = input("{} - Insert your project name: {}".format(COLORS["magenta"], COLORS["reset"]))
    while (len(project_name) == 0):
        project_name = input("{} - Insert your project name: {}".format(COLORS["magenta"], COLORS["reset"]))
    project = [project_name, project_type]
    file = File(project)
    os.chdir(PROJECTS_PATH)
    file.create()
    path = PROJECTS_PATH.replace("\\", "/")
    print()
    print(f"{COLORS['green']}{TYPES['underline']}You can find your project in: {path}/{project_name}")
    print()

if __name__ == "__main__":
    main()
    print(COLORS["reset"], end="")