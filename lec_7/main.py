while True:
    try:
        file_name = input("Enter the name of a text file: ")

        try:
            with open(file_name, 'r') as file:
                content = file.read()
                print("File content:")
                print(content)
                
            write_option = input("Do you want to append to this file? (yes/no): ").lower()

            if write_option == 'yes':
                with open(file_name, 'a') as file:
                    new_content = input("Enter the content you want to add: ")
                    file.write(new_content + '\n')
                    print("Content has been appended to the file.")
            elif write_option == 'no':
                new_file_name = input("Enter a new filename for writing: ")
                try:
                    with open(new_file_name, 'w') as new_file:
                        new_content = input("Enter the content you want to write: ")
                        new_file.write(new_content)
                        print("Content has been written to the new file.")
                except FileNotFoundError:
                    print("Error: Could not create the new file.")
            else:
                print("Invalid input. Please enter 'yes' or 'no.")

        except FileNotFoundError:
            print("Error: The file doesn't exist. Please enter a valid filename.")
    
    except ValueError:
        print("Error: Invalid input. Please enter a valid filename.")
    else:
        print("Writing successful.")
    finally:
        print("File has been closed.")

