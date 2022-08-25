"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
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

# Get dictionary of unique keys, keys as phone numbers, values as minutes on the phone
count_map = {}


def create_unique_phone_numbers_dict(call_list):
    for record in call_list:
        if record[0] in count_map.keys():
            count_map[record[0]] += int(record[3])
        else:
            count_map[record[0]] = int(record[3])
    for record in call_list:
        if record[1] in count_map.keys():
            count_map[record[1]] += int(record[3])
        else:
            count_map[record[1]] = int(record[3])


def get_number_with_maximum_seconds():
    max_seconds = max(count_map.values())
    # Find key of maximum seconds
    for key in count_map:
        if count_map[key] == max_seconds:
            return key, max_seconds


create_unique_phone_numbers_dict(calls)
number, max_seconds = get_number_with_maximum_seconds()

print(
    f"{number} spent the longest time, {max_seconds} seconds, on the phone during September 2016."
)
