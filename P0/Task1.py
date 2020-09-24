"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
num_of_telNums = set()

for text in texts:
    num_of_telNums.add(text[0])
    num_of_telNums.add(text[1])

for call in calls:
    num_of_telNums.add(call[0])
    num_of_telNums.add(call[1])

print("There are {} different telephone numbers in the records.".format(len(num_of_telNums)))

