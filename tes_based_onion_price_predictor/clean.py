import sys
import re
import fileinput

file_name = sys.argv[1]

print(f"Cleaning in progress for {file_name}")

pattern = r">([^<]*)<"

with open(f"{file_name}.txt", "r+") as file:
    text_data = file.read()

matches = re.findall(pattern, text_data, re.MULTILINE)

with open(f"{file_name}_updated.txt", "w+") as file:
    for item in matches:
        file.write(item + "\n")


def process_file(file_name_new):
    
    with open(f"{file_name}_updated.txt", "r") as file:
        data = file.readlines()

    processed_data = ",".join([line.strip() for line in data])

    with open(f"{file_name}_updated.txt", "w") as file:
        file.write(processed_data)

process_file(file_name)


def replace_text(file_name):
    
    with open(f"{file_name}_updated.txt", "r") as file:
        data = file.readline()

    processed_data = re.sub(r'",,",', '\n', data)

    with open(f"{file_name}.csv", "w+") as file:
        file.write(processed_data)

replace_text(file_name)


print(f"Cleaning complete for {file_name}.txt")
print(f"Cleaned file is saved as {file_name}.csv")