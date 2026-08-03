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
            return f'Error: "{directory}" is not a directory'

        # Path is valid, generate file info
        lines = []
        for item in os.listdir(target_directory_path):
            item_path = os.path.join(target_directory_path, item)
            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path)
            lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(lines)

    except Exception as e:
        return f"Error: {str(e)}"
