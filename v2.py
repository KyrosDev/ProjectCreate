import sys
import time
import os
from utils.File import File
from utils.Types import ProjectType

PROJECTS_PATH = str("E:\\Documents\\Projects")

PROJECTS_TYPES = list([
    "flutter",
    "node",
    "vue",
    "python",
    "dart"
])

COLORS = dict({
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "black": "\u001b[30m",
    "yellow": "\u001b[33m",
    "reset": "\u001b[0m",
    "white": "\u001b[37m",
    "cyan": "\u001b[36m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35;1m",
})

TYPES = dict({
    "bold": "\u001b[1m",
    "underline": "\u001b[4m",
    "reversed": "\u001b[7m",
})

PROJECT_TYPE_INPUT_STRING = str("Select type: ")
PROJECT_NAME_INPUT_STRING = str("{} - Insert your project name: {}".format(
    COLORS["magenta"], COLORS["reset"]))


def main():
    os.system("cls")
    print(str("{}{}{}CREATE PROJECT".format(
        COLORS["green"], TYPES["reversed"], TYPES["bold"])))
    print(str("{}Create a project in few seconds with just one command!!!".format(
        COLORS["reset"])))
    print(str(
        "{} - Select your project type: {}".format(COLORS["magenta"], COLORS["reset"])))
    print(str("""    - [0] Flutter App
    - [1] NodeJS Server
    - [2] VueJS WebApp
    - [3] Python Module
    - [4] Dart Module
"""))
    number = int(input(PROJECT_TYPE_INPUT_STRING))
    if (number > len(PROJECTS_TYPES)):
        print("Select a project in range 0 - 4")
        number = int(input(PROJECT_TYPE_INPUT_STRING))
    project_type = PROJECTS_TYPES[number]
    project_name = str(input(PROJECT_NAME_INPUT_STRING))
    while (len(project_name) == 0):
        project_name = str(input(PROJECT_NAME_INPUT_STRING))
    project = list([project_name, project_type])
    file = File(project)
    os.chdir(PROJECTS_PATH)
    file.create()
    path = str(PROJECTS_PATH.replace("\\", "/"))
    print(str(
        f"\n{COLORS['green']}{TYPES['underline']}You can find your project in: {path}/{project_name}\n"))


if __name__ == "__main__":
    main()
    print(COLORS["reset"], end="")
