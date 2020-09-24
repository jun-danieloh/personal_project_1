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

# calls.csv structure
# calling telephone number(string), receiving telephone number(string), start timestamp of telephone call(string), duration of telephone call in seconds(string)

# List of calls by Bangalore
listOfCallsByBangalore = set()

#  Find all of the area codes and mobile prefixes called by people in Bangalore.
for call in calls:
    #print(call)
    if call[0][:5] == '(080)':    
        # 1: Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0.
        if call[1][1] == '0':
            #print(call[1][1])
            for i, v in enumerate(call[1]):
                #print(i)
                #print(v)
                if v == ')':
                    #print(v)
                    listOfCallsByBangalore.add(call[1][:i+1])
        
        # 2: Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. 
        # The prefix of a mobile number is its first four digits, and they always start with 7, 8 or 9.
        elif " " in call[1]:
            listOfCallsByBangalore.add(call[1][:4])
        
        # 3: Telemarketers' numbers have no parentheses or space, but they start with the area code 140.
        elif call[1][:3] == '140':
            listOfCallsByBangalore.add(call[1]['140'])

#print(listOfCallsByBangalore)
code_list = list(listOfCallsByBangalore)

print("The numbers called by people in Bangalore have codes:")

for areaCode in code_list:
    print(areaCode)


#Part B: What percentage of calls from fixed lines in Bangalore are made
#to fixed lines also in Bangalore? In other words, of all the calls made
#from a number starting with "(080)", what percentage of these calls
#were made to a number also starting with "(080)"?
#
#Print the answer as a part of a message::
#"<percentage> percent of calls from fixed lines in Bangalore are calls
#to other fixed lines in Bangalore."
#The percentage should have 2 decimal digits
callFromBangToBang = 0
callFromBangToAny = 0

for call in calls:
    if call[0][:5] == '(080)':
        callFromBangToBang += 1
        callFromBangToAny += 1
    else:
        callFromBangToAny += 1

percentage = (callFromBangToBang / callFromBangToAny)*100

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))
