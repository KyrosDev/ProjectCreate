import sys
import time
import os
from ..utils.File import ProjectType
from ..utils.File import File
from termcolor import colored

PROJECTS_PATH = "E:\\Documents\\Projects"

def main():
    print(colored("hello world", "green"))
    print("""
        - [0] Flutter
        - [1] Node
        - [2] Vue
        - [3] Python
        - [4] Dart
    """)
    project_type = input("Project type: ")