"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.

Own Notes

Inputs: Call list and text list

Outputs: Lexographic order list of telemarketer numbers

Approach: 
- Get list of numbers which never receive incoming calls
- Check against text list to see if those numbers receive or send texts
- Exclude any numbers that do, return the remaining numbers

"""


def check_numbers_making_only_outgoing_calls(call_list):
    outgoing_calls = []
    incoming_calls = []
    telemarketer_set = set()
    for row in call_list:
        outgoing_calls.append(row[0])
        incoming_calls.append(row[1])
    for number in outgoing_calls:
        if number not in incoming_calls:
            telemarketer_set.add(number)
    return telemarketer_set


telemarketers = check_numbers_making_only_outgoing_calls(calls)


def check_telemarketer_set_against_text_list(telemarketer_set, text_list):
    for row in text_list:
        if row[0] in telemarketer_set:
            telemarketer_set.remove(row[0])
        elif row[1] in telemarketer_set:
            telemarketer_set.remove(row[1])
    return telemarketer_set


result = check_telemarketer_set_against_text_list(telemarketers, texts)
sorted_result = sorted(result)

print(f"These numbers could be telemarketers:")
[print(line) for line in sorted_result]
