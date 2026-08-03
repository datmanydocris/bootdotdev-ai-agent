from functions.get_file_content import get_file_content

def main():
    # Test that it truncates properly
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print()

    # Normal files, should succeed
    print("=== main.py ===")
    print(get_file_content("calculator", "main.py"))
    print()

    print("=== pkg/calculator.py ===")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    # Error cases, should fail
    print("=== /bin/cat ===")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print("=== pkg/does_not_exist.py ===")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()