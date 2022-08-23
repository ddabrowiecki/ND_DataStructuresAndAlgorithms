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

# Implement set to save only unique values
unique_numbers = set()

def create_unique_number_set(comms_list):
    for records in comms_list:
        unique_numbers.add(records[0])
        unique_numbers.add(records[1])

def count_unique_numbers():
    create_unique_number_set(calls)
    create_unique_number_set(texts)
    print(f"There are {len(unique_numbers)} different telephone numbers in the records.")

count_unique_numbers()