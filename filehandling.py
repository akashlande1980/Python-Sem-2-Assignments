import os

def open_and_read():
    try:
        f = open("demofile.txt", "r")
        print("\nFile Content:\n", f.read())
        f.close()
    except FileNotFoundError:
        print("File not found!")

def read_with_path():
    path = input("Enter full file path: ")
    try:
        f = open(path, "r")
        print("\nFile Content:\n", f.read())
        f.close()
    except FileNotFoundError:
        print("File not found!")

def read_with_with():
    try:
        with open("demofile.txt", "r") as f:
            print("\nFile Content:\n", f.read())
    except FileNotFoundError:
        print("File not found!")

def read_partial():
    try:
        with open("demofile.txt", "r") as f:
            n = int(input("Enter number of characters: "))
            print(f.read(n))
    except:
        print("Error reading file!")

def read_lines():
    try:
        with open("demofile.txt", "r") as f:
            print(f.readline())
            print(f.readline())
    except:
        print("Error!")

def loop_file():
    try:
        with open("demofile.txt", "r") as f:
            for line in f:
                print(line, end="")
    except:
        print("Error!")

def append_file():
    text = input("Enter text to append: ")
    with open("demofile.txt", "a") as f:
        f.write(text + "\n")
    print("Content appended successfully!")

def overwrite_file():
    text = input("Enter new content: ")
    with open("demofile.txt", "w") as f:
        f.write(text)
    print("File overwritten successfully!")

def create_file():
    name = input("Enter new file name: ")
    try:
        f = open(name, "x")
        f.close()
        print("File created successfully!")
    except FileExistsError:
        print("File already exists!")

def delete_file():
    name = input("Enter file name to delete: ")
    if os.path.exists(name):
        os.remove(name)
        print("File deleted successfully!")
    else:
        print("File does not exist!")

def delete_folder():
    name = input("Enter folder name to delete: ")
    try:
        os.rmdir(name)
        print("Folder deleted successfully!")
    except:
        print("Error! Folder may not be empty or not exist.")

while True:
    print("\n===== FILE HANDLING MENU =====")
    print("1. Open and Read File")
    print("2. Open File with Path")
    print("3. Read using with statement")
    print("4. Read Specific Characters")
    print("5. Read First Two Lines")
    print("6. Loop Through File")
    print("7. Append to File")
    print("8. Overwrite File")
    print("9. Create New File")
    print("10. Delete File")
    print("11. Delete Folder")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        open_and_read()
    elif choice == "2":
        read_with_path()
    elif choice == "3":
        read_with_with()
    elif choice == "4":
        read_partial()
    elif choice == "5":
        read_lines()
    elif choice == "6":
        loop_file()
    elif choice == "7":
        append_file()
    elif choice == "8":
        overwrite_file()
    elif choice == "9":
        create_file()
    elif choice == "10":
        delete_file()
    elif choice == "11":
        delete_folder()
    elif choice == "12":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")