from enum import Enum

class ProjectType(Enum):
    Vue = {
        "name": "Web Application",
        "type": "vue",
        "extension": False,
        "create_script": "vue create",
        "initial_code": False
    }
    Node = {
        "name": "JavaScript Server",
        "type": "node",
        "extension": ".js",
        "create_script": False,
        "initial_code":
"""const test = () => {
    console.log("Hello, World")
}

test()
"""
    }
    Flutter = {
        "name": "Mobile Application",
        "type": "flutter",
        "extension": False,
        "create_script": "flutter create",
        "initial_code": False
    }
    Python = {
        "name": "Python CLI",
        "type": "python",
        "extension": ".py",
        "create_script": False,
        "initial_code":
        """def main():
    pass

if __name__ == "__main__":
    main()
"""
    }
    Dart = {
        "name": "Dart CLI",
        "type": "dart",
        "extension": ".dart",
        "create_script": False,
        "initial_code":
        """import "dart:core"

int main():
    return 0
"""
    }
