from functions.run_python_file import run_python_file

def main():
    print("=== main.py (no args) ===")
    print(run_python_file("calculator", "main.py"))
    print()

    print("=== main.py with args ['3 + 5'] ===")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print()

    print("=== tests.py ===")
    print(run_python_file("calculator", "tests.py"))
    print()

    print("=== ../main.py (should fail) ===")
    print(run_python_file("calculator", "../main.py"))
    print()

    print("=== nonexistent.py (should fail) ===")
    print(run_python_file("calculator", "nonexistent.py"))
    print()

    print("=== lorem.txt (should fail) ===")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    main()