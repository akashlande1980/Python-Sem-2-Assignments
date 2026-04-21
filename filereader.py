def read_file():
    
    file_name = input("Enter the filename to open: ")

    try:
        
        with open(file_name, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)

    except FileNotFoundError:
        
        print(f"Error: The file '{file_name}' was not found.")

    except PermissionError:
        
        print(f"Error: You do not have permission to read the file '{file_name}'.")

    except Exception as e:
    
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_file()