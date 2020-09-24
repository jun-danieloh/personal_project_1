"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

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

# First, figure out numbers that make outgoing calls BUT never send texts
numberCallOutgoingCall = set()
for call in calls:
    numberCallOutgoingCall.add(call[0])

numberSendText = set()
for text in texts:
    numberSendText.add(text[0])

numberCallOutgoingCallButNoText = set()
for num in numberCallOutgoingCall:
    if num not in numberSendText:
        numberCallOutgoingCallButNoText.add(num)

#print(numberCallOutgoingCallButNoText)

# Second, never receive texts       
numberCallOutgoingCallButNoTextNoReceiveText = set()
numberReceivingTexts = set()

for text in texts:
    numberReceivingTexts.add(text[1])

for num in numberCallOutgoingCallButNoText:
    if num not in numberReceivingTexts:
        numberCallOutgoingCallButNoTextNoReceiveText.add(num)

#print(numberCallOutgoingCallButNoTextNoReceiveText)


# Third, never receive incoming calls
numberCallOutgoingCallButNoTextNoReceiveTextNoReceiveCall = set()
numberIncomingCalls = set()

for call in calls:
    numberIncomingCalls.add(call[1])

for num in numberCallOutgoingCallButNoTextNoReceiveText:
    if num not in numberIncomingCalls:
        numberCallOutgoingCallButNoTextNoReceiveTextNoReceiveCall.add(num)

numberFinal = sorted(list(numberCallOutgoingCallButNoTextNoReceiveTextNoReceiveCall))

print("These numbers could be telemarketers: ")
for num in numberFinal:
    print(num)

