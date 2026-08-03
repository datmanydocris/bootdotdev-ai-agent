import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_path, file_path))

        # Check to make sure the file is inside the working directory
        if os.path.commonpath([working_directory_path, target_file_path]) != working_directory_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check that the target is a file
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read up to MAX_CHARS
        with open(target_file_path, "r") as f:
            content = f.read(MAX_CHARS)

            # Check if the files is longer than MAX_CHARS
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {str(e)}"