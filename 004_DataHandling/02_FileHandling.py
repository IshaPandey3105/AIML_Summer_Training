# 📄 FILE HANDLING IN PYTHON: BASIC TO ADVANCE

# 1️⃣ OPENING FILES
# Syntax: open(filename, mode)
# Modes: 
# "r" → read (default)
# "w" → write (creates new or overwrites)
# "a" → append (adds to existing file)
# "x" → create new file, error if exists
# "b" → binary mode (rb, wb etc.)
# "t" → text mode (default)

# Example: Open file for writing
file = open("sample.txt", "w")
file.write("Hello, this is my first file first line.\n")
file.write("Hello, this is my first file second line.\n")
file.close()  # Always close to save changes


# 2️⃣ READING FILES

# Read entire content
file = open("sample.txt", "r")
content = file.read()
print("Content:\n", content)
file.close()

# Read line by line
file = open("sample.txt", "r")
for line in file:
    print("Line:", line.strip())
file.close()

# Read only first line
file = open("sample.txt", "r")
first_line = file.readline()
print("First Line:", first_line)
file.close()


# 3️⃣ USING WITH STATEMENT (Best Practice 🚀)
# It auto-closes the file after use

with open("sample.txt", "r") as f:
    print("Using with:", f.read())


# 4️⃣ WRITING FILES

# "w" mode → overwrite
with open("sample.txt", "w") as f:
    f.write("This is overwritten content.\n")

# "a" mode → append
with open("sample.txt", "a") as f:
    f.write("This line is added later.\n")

with open("sample.txt", "r") as f:
    print("Now content:", f.read())


# 5️⃣ WORKING WITH LIST OF LINES

# Writing multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("lines.txt", "w") as f:
    f.writelines(lines)

# Reading lines into list
with open("lines.txt", "r") as f:
    all_lines = f.readlines()
    print("Lines as List:", all_lines)


# 6️⃣ FILE POINTERS (Tell & Seek)

with open("sample.txt", "r") as f:
    print("Current Position:", f.tell())  # shows pointer position
    print("First 5 chars:", f.read(5))
    print("Position After Read:", f.tell())
    f.seek(0)  # move pointer back to start
    print("After Seek(0):", f.read())
    f.seek(1)  # move pointer to 1st char
    print("After Seek(1):", f.read())


# 7️⃣ EXCEPTION HANDLING WITH FILES

try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found. Please check the name.")
except Exception as e:
    print("An error occurred:", e)


# 8️⃣ HANDLING BINARY FILES (Images, Audio etc.)

# Writing binary
with open("image.jpg", "rb") as f:
    binary_data = f.read()

with open("copy_image.jpg", "wb") as f:
    f.write(binary_data)

# (This will copy image.jpg to copy_image.jpg)


# 9️⃣ OS MODULE FOR FILE MANAGEMENT (Advanced)

import os

# Check if file exists
if os.path.exists("sample.txt"):
    print("sample.txt exists")
else:
    print("File does not exist")

# Rename file
os.rename("sample.txt", "_sample.txt")

# Delete file
# os.remove("_sample.txt")   # Uncomment to actually delete


# 10️⃣ CHECKING FILE OR DIRECTORY

print("Is file:", os.path.isfile("lines.txt")) # True becuz it's a file
print("Is directory:", os.path.isdir("lines.txt")) # False becuz it's not a directory

#################### END ####################