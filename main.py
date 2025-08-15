import numpy as np
'''
Mini Challenge
You have this list:

data = [5, 8, 12, 20]
Change the second element (8) to 10.

Add the number 25 at the end.

Print the length of the list.
'''
print("---------------Array-------------------")
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
print("---------------Conditional Statements-------------------")
scores = [80, 45, 67, 90, 55]

for score in scores:
    if score >= 60:
        print("Pass")
    else:
        print("Fail")


'''
Mini Challenge

Given:

data = np.array([[5, 8, 10],
                 [3, 6, 9],
                 [4, 7, 11],
                 [2, 5, 8]])


Do the following:

Print the second row.

Print the first column.

Print the sub-array containing rows 1–2 and columns 1–2.
'''
print("---------------Numpy array-------------------")
data = np.array([[5, 8, 10],
                 [3, 6, 9],
                 [4, 7, 11],
                 [2, 5, 8]])

print(data[1])
print(data[:, 0])
print(data[1:3, 1:3])
