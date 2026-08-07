import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_directory_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_path, file_path))

        # Make sure the target is inside the working directory
        if os.path.commonpath([working_directory_path, target_file_path]) != working_directory_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check that the target is an existing regular file
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # Check that it is a python file
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # Build the command
        command = ["python", target_file_path]
        if args:
            command.extend(args)

        # Run the command
        result = subprocess.run(
            command,
            cwd=working_directory_path,
            capture_output=True,
            text=True,
            timeout=30,
        )

        # Build the output
        output = []

        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        if not output:
            return "No output produced"

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file with optional command-line arguments and returns the output (stdout, stderr, and exit code)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of command-line arguments to pass to the Python file",
                },
            },
            "required": ["file_path"],
        },
    },
}