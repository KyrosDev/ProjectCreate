from .Types import ProjectType as types
from enum import Enum
import os

class File:

    NODE = types.Node.value
    VUE = types.Vue.value
    FLUTTER = types.Flutter.value
    DART = types.Dart.value
    PYTHON = types.Python.value

    MAIN_FILE_NAME = "main"

    def __init__(self, project: list):
        self.project_name = project[0]
        self.project_type = project[1]
        self.add_to_repo = False
        self.data = {}
        self.__getData__()

    def __createExecutableProjects__(self, script: str):
        os.system(script)
        return

    def __getData__(self):
        for _type in types:
            _type = _type.value
            if _type["type"] == self.project_type:
                self.data = {
                    "name": _type["name"],
                    "type": _type["type"],
                    "extension": _type["extension"],
                    "create_script": _type["create_script"],
                    "initial_code": _type["initial_code"],
                }
        return

    def create(self):
        data = self.data
        extension = data["extension"]
        file_name = f"{self.MAIN_FILE_NAME}{extension}"
        create_script = data["create_script"]

        if create_script is False:
            os.mkdir(self.project_name)
            os.chdir(self.project_name)
            if self.add_to_repo:
                os.system("git init")
            with open(file_name, "x") as main:
                if data["initial_code"] is not False:
                    main.write(data["initial_code"])
        else:
            os.system(f"{create_script} {self.project_name}")
