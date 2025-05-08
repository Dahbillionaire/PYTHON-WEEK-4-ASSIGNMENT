def read_and_modify_file():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, 'r') as infile:
            lines = infile.readlines()

        # Modify each line (example: convert to uppercase)
        modified_lines = [line.upper() for line in lines]

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"✅ Modified content written to '{new_filename}' successfully.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to read '{filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()

