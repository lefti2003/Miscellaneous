"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import time
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

start = time.time()
sending_call_number_list = []
# Get the total phone #'s from calls
for row in range(len(calls)):
    sending_call_number_list.append(calls[row][0])
    sending_call_number_list.append(calls[row][1])

# Get the total phone #'s from texts
for row_t in range(len(texts)):
    sending_call_number_list.append(texts[row_t][0])
    sending_call_number_list.append((texts[row_t][1]))

unique_phone_num = set(sending_call_number_list)

count = len(unique_phone_num)
time.sleep(1)
end = time.time()
print(f"There are {count} different telephone numbers in the records.")


