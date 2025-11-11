from pathlib import Path

def file_content(filename):
    file_content_read=''
    current_script_dir = Path(filename).parent
    absolute_file_path = f'{current_script_dir}/{filename}'
    print(f"Reading file from  -->>> '{absolute_file_path}'")
    try:
        # Open the file in read mode ('r') using a 'with' statement
        with open(absolute_file_path, 'r') as f:
            # Read the entire content of the file and store it in a variable
            file_content_read = f.read()
        return file_content_read
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
