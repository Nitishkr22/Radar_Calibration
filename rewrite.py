import os
import fileinput

# Define the folder path containing the text files
folder_path = '/media/radar/00cb8602-b2ed-4b7e-8a79-cc67689c6748/suzuki_data(new)/data/images & labels/val/labels'

# List all files in the folder
file_list = os.listdir(folder_path)

# Iterate through each file in the folder
for filename in file_list:
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a text file (you can customize the file extension)
    if file_path.endswith('.txt'):
        # Open the file in read mode and also in place edit mode
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                # Check if the line is not empty and has at least 2 characters
                if len(line) >= 2:
                    first_two_chars = line[:2]
                    try:
                        # Convert the first two characters to an integer
                        num = int(first_two_chars)
                        # Check if the integer is between 20 and 26
                        if 20 <= num <= 26:
                            # Decrement the integer by 1 and print it back
                            print(str(num - 1) + line[2:], end='')
                        else:
                            # If not in the range, print the original line
                            print(line, end='')
                    except ValueError:
                        # If the first two characters are not integers, print the original line
                        print(line, end='')
                else:
                    # If the line doesn't have at least 2 characters, print it as is
                    print(line, end='')
