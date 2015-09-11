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

'''

#def mixedtypelist():    


mixedlist = [1,2,"glove","hat",15,"tomato"] # here's my mixed-type list
#print(mixedlist)                           # just checking - it prints
intlist=0                       #starts at zero then a gets added to it each time through the for loop
strlist=("")                    #i want a string that starts with nothing
for a in (mixedlist):                       # for loop
    #print(type(a))
    if type(a) == int:                      #--if it's an int
        #print("integer")                    #--just checking
        intlist=a+intlist           #  1st integer + 0, then that gets added to next integer, etc.
        #print (intlist)
    elif type(a) == str:                    #--if it's a str
        #print("string")                    #--just checking
        strlist=(strlist+a+" ") # blank string added to first string added to next etc. but it's a long string, not a list!!
    else:
        continue
print(intlist)
print(strlist)                  #now how do i convert this string into a list???



'''
#print (mixedlist[1])
x=0
for a in mixedlist[x]:
    print (a) 
    x+1
    #print (a[0,1])
   
               
#mixedtypelist()   


'''





