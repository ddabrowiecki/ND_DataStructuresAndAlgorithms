"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
Own Notes: Part A

Input: Call list

Outputs: lexicographically sorted list of area codes called from Bangalore phones
- Area codes from fixed lines inside the parens e.g. (987) --> 987
- First four numbers from mobile numbers starting with 7,8 or 9 with space in middle
- 140 if number starts with those 3 numbers (telemarketers)

Own Notes: Part B

Input: Call List with only calls from Bangalore, broken up into 2 count variables: 
  - Calls within the same area code 
  - Calls to another area code 

Outputs: Percentage of calls from Bangalore to Bangalore

"""

# Helper function to slice the area codes
def slice_area_codes(number):
    if " " in number:
        return number[slice(4)]
    elif number[0:3] == "140":
        return "140"
    elif "(" in number:
        match = re.search("\(([0-9]*)\)", number)
        if match:
            return match.group(1)


# Create set of area codes called from, but not in, Bangalore
# and a set of numbers in Bangalore called from the same location for part B
call_recipients_not_in_bangalore_codes = set()
count1 = 0
count2 = 0


def filter_by_area_code(call_list):
    bangalore_area_code = "(080)"
    global count1
    global count2
    for rows in call_list:
        if bangalore_area_code in rows[0] and bangalore_area_code not in rows[1]:
            sliced_code = slice_area_codes(rows[1])
            call_recipients_not_in_bangalore_codes.add(sliced_code)
            count1 += 1
        elif bangalore_area_code in rows[0] and bangalore_area_code in rows[1]:
            count2 += 1


# Part A
filter_by_area_code(calls)
unique_area_codes = sorted(call_recipients_not_in_bangalore_codes)
print(f"The numbers called by people in Bangalore have codes:")
[print(line) for line in unique_area_codes]

# Part B
same_area_percentage = count2 / (count1 + count2) * 100
print(
    f"\n {same_area_percentage:.2f} percent of calls from fixed lines in Bangalore are calls"
    " to other fixed lines in Bangalore."
)
