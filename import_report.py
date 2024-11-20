import csv

input_file_path = "/mnt/d/Transfered/MICCAI Challenge/UNICORN_morsel/UNICORN/task-19-anonymization/task-20-anonymization/input.txt"
output_file_path = "/mnt/c/Users/imadh/Desktop/output.csv"

with open(input_file_path, 'r') as file:
    text = file.read()

#formatting
text = text.replace('\n', ' ')
word_list = text.split(' ')

#output CSV file in rows of 9
with open(output_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for i in range(0, len(word_list), 9):
        row = word_list[i:i+9]
        csv_writer.writerow(row)
        csv_writer.writerow([])  
        csv_writer.writerow([])

print(len(word_list), 'words in file')
print("CSV output created")