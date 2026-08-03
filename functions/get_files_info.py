import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        # Get the absolute path of the working directory
        working_directory_path = os.path.abspath(working_directory)

        # Build the full target path
        target_directory_path = os.path.normpath(os.path.join(working_directory_path, directory))

        # Check if the target is still inside the working directory
        if os.path.commonpath([working_directory_path, target_directory_path]) != working_directory_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check that target it is a directory
        if not os.path.isdir(target_directory_path):
            return f'Error "{directory}" is not a directory'

        # Path is valid
        return f'Success: "{directory}" is within the working directory'

    except Exception as e:
        return f"Error: {str(e)}"
