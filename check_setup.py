# Check the Environment

import sys
from config import validate_config

def check_py_vers():
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro

    print(f"Python Version: {major}.{minor}.{micro}")
    return True

def check_imports():
    modules = {
        "telegram": "python-telegram-bot",
        "openai": "openai",
        "dotenv": "python-dotenv",
        "pydantic": "pydantic",
        "loguru": "loguru",
    }
    all_ok = True
    for module, package in modules.items():
        try:
            __import__(module)
            print(f"{package} is imported")
        except ImportError:
            print(f"{package} is not found")
            all_ok = False
    print()
    return all_ok

def check_structure():
    import os

    required_dirs = ["bot", "ai", "utils", "data", "tests"]
    required_files = [".env", ".gitignore", "requirements.txt", "config.py"]

    all_ok = True

    print("Check dirs:")
    for dir_name in required_dirs:
        if os.path.isdir(dir_name):
            print(f"{dir_name} - ok")
        else:
            print(f"Error! {dir_name} isn`t found!")
            all_ok = False

    print("Check files:")
    for file_name in required_files:
        if os.path.isfile(file_name):
            print(f"{file_name} - ok")
        else:
            print(f"Error! {file_name} isn`t found")
            all_ok = False
    print()
    return all_ok

if __name__ == "__main__":
    print("Checking your Environment")
    results = []
    results.append(("Python Version", check_py_vers()))
    results.append(("Project Structure", check_structure()))
    results.append(("Lib Import", check_imports()))
    results.append(("Config", validate_config()))

    print("Result:")
    for name, result in results:
        status = "✅" if result else "❌"
        print(f"   {status} {name}")

    all_ok = all(result for _, result in results)
    print()

    if all_ok:
        print("You ready to work")
    else:
        print("You need to check your project")
