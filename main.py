'''
Mini Challenge
You have this list:

data = [5, 8, 12, 20]
Change the second element (8) to 10.

Add the number 25 at the end.

Print the length of the list.
'''

data = [5, 8, 12, 20]

data[1] = 10
data.append(25)
print(len(data))



'''
Mini Challenge
You have:


scores = [80, 45, 67, 90, 55]
Task:

Loop through the list.

Print "Pass" if the score is ≥ 60, otherwise print "Fail".

'''

scores = [80, 45, 67, 90, 55]

for score in scores:
    if score >= 60:
        print("Pass")
    else:
        print("Fail")
