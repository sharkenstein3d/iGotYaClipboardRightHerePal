import os
import pyperclip

def get_file_extension(path):
    _, ext = os.path.splitext(path)
    return ext.lower()

def calculate_relative_import(from_path, to_path):
    from_path = os.path.abspath(from_path)
    to_path = os.path.abspath(to_path)

    from_dir, from_file = os.path.split(from_path)
    to_dir, to_file = os.path.split(to_path)

    relative_path = os.path.relpath(to_dir, start=from_dir)

    return relative_path, to_file

def check_path_depth(relative_path):
    depth = len(relative_path.split(os.sep)) - 1
    if depth >= 5:
        return "Jimmy Hoffa might be lurkin' back here."
    elif depth >= 3:
        return "Whoa, who's this guy tryin' ta hide from?"
    return ""

def generate_import_statement(from_path, to_path):
    relative_path, to_file = calculate_relative_import(from_path, to_path)
    from_ext = get_file_extension(from_path)
    to_ext = get_file_extension(to_path)

    import_name = os.path.splitext(to_file)[0]  # Removing file extension for import name

    depth_message = check_path_depth(relative_path)

    if from_ext == '.tsx' and to_ext == '.svg':
        return f"{depth_message}\nimport {import_name} from '{os.path.join(relative_path, to_file)}';"
    elif from_ext == '.tsx' and to_ext == '.scss':
        return f"{depth_message}\nimport styles from '{os.path.join(relative_path, to_file)}';"
    elif from_ext == '.tsx' and to_ext == '.tsx':
        return f"{depth_message}\nimport {import_name} from '{os.path.join(relative_path, import_name)}';"

    return f"{depth_message}\n// Yo, I ain't got logic for .{to_ext} in .{from_ext} files yet."

def main():
    print("Yo, let's see what we got on the clipboard...")
    paths = pyperclip.paste().strip().split('\n')

    if len(paths) != 2:
        print("Ay, you gotta copy exactly two file paths, each on its own line, capisce?")
        return

    from_path, to_path = paths

    if not (os.path.exists(from_path) and os.path.exists(to_path)):
        print("Whoa there, one or both paths are no good. Double-check 'em, will ya?")
        return

    import_statement = generate_import_statement(from_path, to_path)
    print(import_statement)
    pyperclip.copy(import_statement)
    print("Boom! Import statement's on your clipboard. On to the next thing!")

if __name__ == '__main__':
    main()
