'''
Created on Sep 10, 2015

@author: PC-43
'''
from builtins import int
'''
INTRUCTIONS:
given a list of mixed types (ints and strings only),
1. give the sum of ints in the list.
2. create a new list of all the strings
3. EXTRA - have the user input the list 

PLAN:
create list called mixedlist
extract all ints from mixedlist into a new list called intslist
add all list elements to make sumints
extract all strings from mixedlist into a new list called stringslist

NEXT
ask user to input a list of only integers and/or strings, separated by commas
if other than an int or str is input, print error and ask again - else go on to for loop
user list then becomes mixedlist
the rest should work from there.

'''

def mixedtypelist():    


    mixedlist = [1,2,"glove","hat",15,"tomato"] # here's my mixed-type list
    #print(mixedlist)                           # just checking - it prints
    intlist=0                       #starts at zero then a gets added to it each time through the for loop
    strlist=[]                    #i want to start with an empty list, then add each string that the for loop finds
    for a in (mixedlist):                       # for loop
        #print(type(a))                        # just testing
        if type(a) == int:                      #--if it's an int...
            intlist=a+intlist           #  1st integer + 0, then that gets added to next integer, etc.
        elif type(a) == str:                    #--if it's a str...
            strlist.append(a)        #if it's a string, add it to strlist
        else:
            continue
    print("The sum of all the integers is " + str(intlist))
    print("The list of all the strings is " + str(strlist))

mixedtypelist() 

'''
#print (mixedlist[1])
x=0
for a in mixedlist[x]:
    print (a) 
    x+1
    #print (a[0,1])
   
               
#mixedtypelist()   


'''





