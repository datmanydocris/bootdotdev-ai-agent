from functions.get_files_info import get_files_info

def main():
    # Should succeed - target within working directory
    print(get_files_info("calculator", "."))

    # Should fail - target outside of working directory
    print(get_files_info("calculator", "/bin"))

    # Should fail - tries to go up a level outside of working directory
    print(get_files_info("calculator", "../"))

    # Should fail – target not a directory
    print(get_files_info("calculator", "main.py"))

if __name__ == "__main__":
    main()
