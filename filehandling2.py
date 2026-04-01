import os

# File path (define once to avoid repetition)
file_path = r"C:\Users\Avinash\OneDrive\Attachments\Documents\Akash Programs\SEM 2\demofile.txt"

# 1. Read full file
print("Reading Full File...")
with open(file_path, "r") as f:
    print(f.read())

# 2. Read only first 10 characters
print("\nReading First 10 Characters...")
with open(file_path, "r") as f:
    print(f.read(10))

# 3. Read line by line
print("\nReading Line by Line...")
with open(file_path, "r") as f:
    print(f.readline())

# 4. Append data
print("\nAppending Data...")
with open(file_path, "a") as f:
    f.write("\nNow the file has more content!")

with open(file_path, "r") as f:
    print(f.read())

# 5. Overwrite file
print("\nOverwriting File...")
with open(file_path, "w") as f:
    f.write("Oops! I have deleted the content!")

with open(file_path, "r") as f:
    print(f.read())

# 6. Create new file
print("\nCreating New File...")
try:
    with open("myfile.txt", "x") as f:
        f.write("This is a new file created using Python.")
    print("myfile.txt created successfully")
except FileExistsError:
    print("myfile.txt already exists")

# 7. Delete file
print("\nDeleting File...")
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("myfile.txt deleted successfully")
else:
    print("File does not exist")

# 8. Create and delete folder
print("\nFolder Operations...")
if not os.path.exists("myfolder"):
    os.mkdir("myfolder")
    print("Folder created")

if os.path.exists("myfolder"):
    os.rmdir("myfolder")
    print("Folder deleted")