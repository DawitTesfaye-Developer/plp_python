# file_read_write.py
def process_file():
    try:
        # Read from input.txt
        with open("input.txt", "r", encoding="utf-8") as infile:
            content = infile.readlines()

        # Modify the content (example: make everything uppercase)
        modified_content = [line.upper() for line in content]

        # Write to output.txt
        with open("output.txt", "w", encoding="utf-8") as outfile:
            outfile.writelines(modified_content)

        print("✅ Success! The file has been processed and saved as output.txt")

    except FileNotFoundError:
        print("❌ input.txt not found. Please make sure the file exists.")

process_file()

# error_handling_lab.py

def safe_file_read():
    filename = input("📂 Enter the filename to read: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        print("✅ File read successfully!")
        print("📄 File content:\n", content)

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

safe_file_read()
