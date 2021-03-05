"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
start = time.time()
sending_call_number_list = []

for row in range(len(calls)):

    sending_call_number_list.append(calls[row][0])
    sending_call_number_list.append(calls[row][1])

unique_phone_num = set(sending_call_number_list)
call_duration_list = []

for num in unique_phone_num:
    duration_sum = 0
    for call in calls:
        if num in call:
            duration_sum += int(call[3])

    call_duration_list.append([num, duration_sum])

max_call_duration = 0
i = 0
for tel in call_duration_list:
    if tel[1] > max_call_duration:
        max_call_duration = tel[1]
        max_call_num = tel[0]
    i += 1

time.sleep(1)
end = time.time()

print(f" {max_call_num} spent the longest time, {max_call_duration} seconds, on the phone during \
September 2016.")
#print(f"Runtime of the program is {end - start}") 1.3385775089263916