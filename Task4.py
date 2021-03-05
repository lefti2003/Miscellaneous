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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
start = time.time()
out_calls_list = []
incoming_calls_list = []
for row_c in range(len(calls)):
    out_calls_list.append(calls[row_c][0])
    incoming_calls_list.append(calls[row_c][1])

# get a set of all the outgoing calls
out_calls_set = set(out_calls_list)
# get a set of all the incoming calls
incoming_calls_set = set(incoming_calls_list)

out_texts_list = []
incoming_texts_list = []
for row_t in range(len(texts)):
    out_texts_list.append(texts[row_t][0])
    incoming_texts_list.append(texts[row_t][1])

# get a set of all the outgoing texts
out_texts_set = set(out_texts_list)
# get a set of all the incoming texts
incoming_texts_set = set(incoming_texts_list)

# possible telemarketers
tele_mark_num = []
for call in out_calls_set:
    if call not in incoming_calls_set and call not in incoming_texts_set and \
            call not in out_texts_set:
        tele_mark_num.append(call)

tele_mark_num_sorted = sorted(tele_mark_num)
print("These numbers could be telemarketers: ")

time.sleep(1)
end = time.time()
#print(f"Runtime of the program is {end - start}") 1.0252931118011475 or 25ms

for tele_num in tele_mark_num_sorted:
    print(tele_num)
