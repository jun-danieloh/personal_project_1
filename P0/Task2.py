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
spendTimeOnPhone = {}

for call in calls:
    if spendTimeOnPhone.get(call[0]) == None:
        spendTimeOnPhone[call[0]] = int(call[3])
    else:
        spendTimeOnPhone[call[0]] += int(call[3])
    
    if spendTimeOnPhone.get(call[1]) == None:
        spendTimeOnPhone[call[1]] = int(call[3])
    else:
        spendTimeOnPhone[call[1]] += int(call[3])

#maxTime = 0
#maxCallNum = ''
##spendTimeOnPhone
##print(spendTimeOnPhone)
#
#for call in spendTimeOnPhone:
#    if spendTimeOnPhone[call] > maxTime:
#        maxTime = spendTimeOnPhone[call]
#        maxCallNum = call

#print(spendTimeOnPhone)

longest_duration = max(spendTimeOnPhone.items(), key=lambda x: x[1])

#print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxCallNum, maxTime))
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*longest_duration))

