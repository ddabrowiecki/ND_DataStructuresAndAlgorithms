# Summary

This text file is a time complexity assessment for the first assignment of the Udacity Data Structures and Algorithms nanodegree.

# The assignment

I was asked to use a large dataset of calls and texts from September 2016 to answer various questions about the data.

The data included:

- A .csv file of text message logs with 3 columns (sending phone number, receiving phone number, timestamp)
- A .csv file of call logs with 4 columns (sending phone number, receiving phone number, timestamp, duration of call in seconds)

### Task 0

Request: Print the first record of texts and the last record of calls.

Worst Case Time Complexity: On + 8 -- **O(1)**.  4 lines of code are executed per function call, and each function is called once for a total of 2 calls.  A change to the scale of inputs to these algorithms does not change the constant order of the outputs.

### Task 1

Request: Print a count of unique phone numbers in the logs.

Worst Case Time Complexity: 2(n+2) + 1 + 1 = 2n + 6 -- **O(n)**.  A for loop with 2 lines was used to iterate through all numbers in the logs twice, for calls and texts.  A set was created on 1 line, and a print statement was executed on 1 line after the for loops completed. This results in the algorithm having linear order.

### Task 2

Request: Print the phone number having the longest total duration of calls (sending and receiving)

Worst Case Time Complexity: (n+2) + (n+2) + (n+1) 1 + 1 + 1 = 5n+9 -- **O(n)**.  Iteration through each number in the call logs was necessary 3 times, with some for loops having 1 operation and others having 2.  A dictionary was created in 1 line, a max_seconds variable was created on one line and a print statement at the end of the file was executed on 1 line.

### Task 3

Request: Print area codes and mobile prefixes of numbers called from area code (080) (Part A).  Print percentage of total calls which were made from sent and received from area code (080) (Part B). 

Worst Case Time Complexity: 

Part A:  (n+1+3) + 3 + n log n + n = 2n + n log n + 7 -- **O(n log n)**. One set and 2 count variables were created on 3 lines, and a for loop with two conditions was necessary, where one of the conditions executed 3 checks (this was the worst case of the conditions).  That condition contains a regex, which can increase complexity if searching through large strings; however, here we have limited amounts of characters per phone number.

Once these operations are complete, we sort the set, with a complexity of **n log n**. To print the result we loop over the set for a complexity of **n**.

Part B: n log n + 1 -- **O(n log n)**.  We use the count variables created in Part A, so that time complexity carries over. A calculation of percentage is done in 1 line.

### Task 4

Request: Print a list of possible telemarketers (phone numbers only making calls, which did not receive calls or send/receive any texts)

Worst Case Time Complexity: (n+2) + (n+1) + (n+2) + 3 + n log n + n = 4n + n log n + 8 -- **O(n log n)**. 3 for loops were necessary, each with varying amounts of operations.  We also create 2 arrays and 1 set on 3 lines.  Once this is completed, we sort a set, and then loop through the results to print all the potential telemarketer numbers.