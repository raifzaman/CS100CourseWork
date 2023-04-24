'''
Raif Zaman
CS 100
HW 06
'''
'''
#NOTES FROM POWERPOINT PRESENTATION
def areaOfRectangle(a,b):
    area = a*b
    print(area)

areaOfRectangle(3,4)

def hello(name):
    line = 'Welcome, ' + name + ', to the world of Python'
    print(line)


numList = [4,0,1,-2]
def oddCount(numList):
'For every function you write, it is important to leave a description of what the function does, so the developer can understand it'
    result = 0
    for i in numList:
        if i % 2 == 1:
            result += 1
            print(result)

'''

#Question 1

def hasFinalLetter(strList,letters):
    '''Function creates and returns a list of all the strings in strList that end with letter in letters without duplication.'''
    list = []
    for string in strList:
        if string[-1] in letters and string[-1] not in list: #If statement to look at last chaacter in each element and check to see if character is in string.
            list.append(string) #As the list is sorted through and if statment holds true, the string from list is added in to the empty 'list' in second line of function
    return list

#Test Case 1
list1 = ["to", "be", "or", "not", "to", "be"]
string1 = "aeiouAIEOU"
result1 = hasFinalLetter(list1,string1)
print(result1)

#Test Case 2
list2 = ["tomorrow", "and", "tomorrow", "and", "tomorrow"]
string2 = "wxyz"
result2 = hasFinalLetter(list2,string2)
print(result2)

#Test Case 3
list3 = ["friends", "romans", "countrymen," "lend", "me", "your", "ears"]
string3 = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
result3 = hasFinalLetter(list3,string3)
print(result3)


#Question 2

def isDivisible(maxInt,twoInts):
    numList = []
    for i in range(0, maxInt):
        if i % twoInts[0] == 0 and i % twoInts[1] ==0:
            numList.append(i)
    return numList

#Test Case 1

test_int1 = 100
test_tup1 = (2,5)
test_result1 = isDivisible(test_int1,test_tup1)
print(test_result1)

#Test Case 2

test_int2 = 42
test_tup2 = (2,3)
test_result2 = isDivisible(test_int2,test_tup2)
print(test_result2)

#Test Case 3
test_int3 = 100
test_tup3 = (1,100)
test_result3 = isDivisible(test_int3,test_tup3)
print(test_result3)