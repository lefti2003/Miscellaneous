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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
start = time.time()

sending_text_number = texts[0][0]
receiving_text_number = texts[0][1]
text_date_time = texts[0][2].split()
text_date = text_date_time[0]
text_time = text_date_time[1]

print(f"First record of texts, {sending_text_number} texts {receiving_text_number} at time {text_time}")


last_call = calls[-1]

sending_call_number = last_call[0]

receiving_call_number = last_call[1]

call_date_time = last_call[2].split()

call_date = call_date_time[0]
call_time = call_date_time[1]
call_duration = last_call[3]

time.sleep(1)

end = time.time()

print(f"Last record of calls, {sending_call_number} calls {receiving_call_number}\
 at time {call_time}, lasting {call_duration} seconds")
