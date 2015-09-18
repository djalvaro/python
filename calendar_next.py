'''
Created on Sep 17, 2015

@author: PC-43
'''

'''


#====================================== LEAP YEAR CHALLENGE ============================
from email._parseaddr import SPACE
def main():
    

#    IF year modulus 4 = 0 
#    AND year modulus 100 != 0 
#    OR year modulus 400 = 0 
#    then it's a leap year
    
#    thisyear%4 ==0
#    thisyear%100 != 0
#    thisyear%400==0
    
    
    thisyear = int(input("Hey, what year is it? "))
    if (thisyear%4 == 0) and (thisyear%100 != 0) or (thisyear%400 == 0): # it was way simpler than i was trying to make it!
            print("LEAP YEAR")
    else:
        print("NOT A LEAP YEAR")   
    

        
main()
'''
'''



#====================================== IF STATEMENT to stop users from using numbers outside the integer scope============================
def main():
    
    while True:                                                         #loop to keep asking
        n = int(input("Input the number of days in the month: "))
        if n>31 or n<28:                                                #to keep numbers 28-31
            print("Months don't have more than 31 days or less than 28. Pay attention.")
        else:
            break                                                       #get out of the month loop
    
    while True:                                                         #loop to keep asking
        d= int(input("Input the starting day (0=Sun, 1=Mon, ...): "))
        if d>6:                                                          #to keep numbers 0-6
            print("There are only 7 days. Please choose 0-6.")
        else:
            break                                                       #get out of the month loop    
            
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

#====================================== TRY/EXCEPT with an IF STATEMENT =============================================
#====================to stop users from using non-integers AS WELL AS numbers outside the integer scope============================
def main():

    while True:
        try:                            # try - is it a float? word? or integer?
            n = (input("Input the number of days in the month: "))
            n = int(n)                  # str to an int. if they input a word or float, it'll go to the "except"
            if n<28 or n>31:            # it's an integer. now see if it is 28-31.
                print("Months have 28-31 days. Try again.")
                print()                 # add a space
            else:
                break
            
        except:
            print("Please enter a number. Try again.")
            print()                      # add a space
            
    while True:
        try:                            # try - is it a float? word? or integer? 
            d= int(input("Input the starting day (0=Sun, 1=Mon, ...): "))
            d = int(d)                  # str to an int. if they input a word or float, it'll go to the "except"
            if d>6:                     # it's an integer. now see if it is 0-6.
                print("Days are numbered 0-6. Try again.")
                print()                 # add a space
            else:
                break
            
        except:
            print("Please enter a number 0-6. Try again.")
            print()                 # add a space
              
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

