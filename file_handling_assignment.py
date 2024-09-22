# file_handling_assignment.py

def create_file():
    """Creates a new text file and writes initial content."""
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("The second line contains the number: 42\n")
            file.write("Finally, this is the third line.\n")
        print("File 'my_file.txt' created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    """Reads the contents of the text file and displays them."""
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("\nContents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    """Appends additional content to the text file."""
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending the fourth line.\n")
            file.write("The fifth line has the number: 100.\n")
            file.write("Lastly, this is the sixth line.\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied to append to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    """Main function to execute file handling tasks."""
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to show the appended content

if __name__ == "__main__":
    main()
