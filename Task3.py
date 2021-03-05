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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
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

def checkreceivingcall(incall):
    if incall.startswith('('):
        area_code = get_codes(incall)
        return area_code
    elif incall.startswith('140'):
        return '140'
    elif incall.startswith('7') or incall.startswith('8') or incall.startswith('9'):
        return incall[0:4]


def get_codes(phone_number):
    i = 0
    area_code = ''

    while i < len(phone_number):
        if phone_number[i] == '(':
            while phone_number[i] != ')':
                i += 1
                if phone_number[i] == ')':
                    break
                else:
                    area_code += phone_number[i]
        i += 1

    return area_code

start = time.time()

out_code_list = []
received_code_list = []
for row in range(len(calls)):
    out_call = calls[row][0]
    received_call = calls[row][1]
    if out_call.startswith('(080)'):
        received_code_list.append(checkreceivingcall(received_call))


unique_code_list = sorted(set(received_code_list))

area_code_list = []

print("The numbers called by people in Bangalore have codes:")
for num in unique_code_list:
    print(num)


# Part B

out_calls_080_list = []
received_calls_080_list = []
for row in range(len(calls)):
    out_call = calls[row][0]
    received_call = calls[row][1]
    if out_call.startswith('(080)'):
        out_calls_080_list.append(out_call)
    if out_call.startswith('(080)') and received_call.startswith('(080)'):
        received_calls_080_list.append(received_call)


time.sleep(1)
end = time.time()
num_out_080 = len(out_calls_080_list)
num_received_080 = len(received_calls_080_list)
percent_080 = (num_received_080/num_out_080)*100


print("{0:1.2f} percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.".format(percent_080))

#print(f"Runtime of the program is {end - start}") 1.0111842155456543


