filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as infile:
        contents = infile.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' could not be read.")
else:
    modified_contents = contents.upper()
    new_filename = f"modified_{filename}"
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_contents)
        print(f"Modified file written to '{new_filename}'.")
    except IOError:
        print(f"Error: Could not write to '{new_filename}'.")