import os

def report_code(directory):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    for file_path in python_files:
        print("="*50)
        print(f"File: {file_path}")
        print("="*50)
        with open(file_path, "r") as f:
            print(f.read())
        print("="*50)
        print("\n")

report_code(".")
