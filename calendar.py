'''
Created on Sep 11, 2015

@author: PC-43
'''
'''
--------------------------PRACTICE------------------------------
def main():
    n = int(input("Input the number of days in the month (28-31): "))
    d= int(input("Input the starting day (0=Sun, 1=Mon, ...): "))
    for j in range(d):
        print("  ",end=" ")
    i = 1
    while i <= n:
        if i < 10:
            print (" "+str(i), end=" ")
        else:
            print (i, end=" ")
        if (i+d) % 7 ==0:
            print (" ")
        i = i + 1
        
main()
'''
'''
#--------------------------EXERCISE 1:   8 DAYS/WEEK  - done------------------------------
def main():
    n = int(input("Input the number of days in the month (28-31): "))
    d= int(input("Input the starting day (0=Sun, 1=Mon, ... 7=Funday): "))
    if d>7:
        print("There's only 8 days in the week so input 0-7 please.")
        d= int(input("Input the starting day (0=Sun, 1=Mon, ... 7=Funday): "))
    #else:                

    for j in range(d):
        print("  ",end=" ")
    i = 1
    while i <= n:
        if i < 10:
            print (" "+str(i), end=" ")
        else:
            print (i, end=" ")
        if (i+d) % 8 ==0:
            print (" ")
        i = i + 1
        
main()
'''

'''
#--------------------------EXERCISE 2:   5 CALENDARS - done------------------------------

def main():
        for q in range(0,5):

            if (q>0):
                print ("\n")
            n = int(input("Input the number of days in the month (28-31): "))
            d= int(input("Input the starting day (0=Sun, 1=Mon, ...): "))
            for j in range(d):
                print("  ",end=" ")
            i = 1
            while i <= n:
                if i < 10:
                    print (" "+str(i), end=" ")
                else:
                    print (i, end=" ")
                if (i+d) % 7 ==0:
                    print (" ")
                i = i + 1
        
main()
'''
'''
#--------------------------EXERCISE 3:   LEAP YEAR - done------------------------------

def main():
    
'''
    #get year
    #if year modulus 4 = 0 then it's a leap year
'''

    thisyear = int(input("Hey, what year is it? "))
    if (thisyear%4 == 0):
        print("LEAP YEAR")
    else:
        print("NOT A LEAP YEAR")

        
main()
''' 
 
 #--------------------------LEAP YEAR "CHALLENGE" ------------------------------
 

def main():
    
    '''
 #   IF year modulus 4 = 0 
  #  AND year modulus 100 != 0 
  #  EXCEPT year modulus 400 = 0 
  #  then it's a leap year
  #  
  #  thisyear%4 == 0
  #  thisyear%100 != 0
  #  thisyear%400=0
    
'''

    thisyear = int(input("Hey, what year is it? "))
    if (thisyear%4 == 0 and thisyear%100 != 0):
        if (thisyear%400 == 0):
            print("NOT A LEAP YEAR")
        else:
            print("LEAP YEAR")
    else:
        print("NOT A LEAP YEAR")

        
main()

'''
'''
 #-------------------------- EXERCISE 4  - done ------------------------------
'''
def main():
    ''''''
    user gives number of asterisks
    print out 50 asterisks
    number of asterisks per line = user input
    
    loop to run 100 times range(0,99)
    even number print * (divisible by 2), odd number print space (not divisible by 2)
    if asterisks per line is <8, go to next line
    if asterisks == 50, stop
    
    ''''''
    
    n = int(input("Give me a positive integer... please"))
    i=0
    for i in range(0,100):            #  go thru loop 100 times
        if (i%2==0):                    #if even number, print a star
            print("*", end="")
        else:                           #odd number print a space
            print(" ", end="")
        i=i+1                           #i increases by 1
        if (i%(2*n)==0 and i>0):        #go to new line if i is divisible by 2x inputted number (including spaces) but NOT the first time around
            print("\n")  

            
main()
'''
