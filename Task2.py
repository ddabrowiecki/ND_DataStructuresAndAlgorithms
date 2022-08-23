"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Get dictionary of unique keys
count_map = {}

def create_unique_phone_numbers_dict(call_list):
    for records in call_list:
        count_map[records[0]] = 1
        count_map[records[1]] = 1

def phone_number_with_most_rows(call_list):
    highest_number_rows = 0
    # Count number of rows that the phone numbers appear in 
    for rows in call_list:
        if rows[0] in count_map.keys():
            count_map[rows[0]] += 1
        elif rows[0] in count_map.keys():
            count_map[rows[1]] += 1
    # Determine highest number of rows
    for number, row_count in count_map.items():
        if row_count >= highest_number_rows:
            highest_number_rows = row_count
    # Find key of highest number
    for key in count_map:
        if count_map[key] == highest_number_rows:
            return key
    
create_unique_phone_numbers_dict(calls)
number = phone_number_with_most_rows(calls)
# number = "(080)62164823"

def add_phone_number_seconds(call_list):
    seconds_count = 0
    for rows in call_list:
        if rows[0] == number or rows[1] == number:
            seconds_count += int(rows[3])
    return seconds_count

total_seconds = add_phone_number_seconds(calls)


print(f"{number} spent the longest time, {total_seconds} seconds, on the phone during September 2016.")
