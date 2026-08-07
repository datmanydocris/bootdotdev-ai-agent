import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_path, file_path))

        # Check to make sure file_path is inside the working_directory
        if os.path.commonpath([working_directory_path, target_file_path]) != working_directory_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Check if the file path is a directory
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Create parent directories if they do not exist
        parent_directory = os.path.dirname(target_file_path)
        if parent_directory:
            os.makedirs(parent_directory, exist_ok=True)

        # Write the file
        with open(target_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites content to a specified file relative to the working directory (creates parent directories if needed)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file to write to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write into the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}