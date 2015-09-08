'''
Created on Sep 8, 2015

@author: PC-43
'''

'''
#--------------------WRITING PYTHON PROGRAMS-------------
def main():
    
    tempF = input("input the temperature in Fahrenheit: ")
   # print(tempF) --- testing one step at a time
    tempF = (int(tempF)) #must convert input number from a string to an int!!
   # print(tempF) -- testing
    
    tempC = ((5.0/9.0)*(tempF - 32.0))
   # print(tempC) --- making sure i get 
    print (tempF, " F = ", tempC, "C")
    
main()
'''




'''
# ---------------------LOOPS-------------------

'''
'''
def main():
    for i in range (10):
        print (i) # no comma makes each on own line
        
    for i in range (10):
    print (i, end=" ") # comma keeps it in one line
   

for i in range (10):
    print (i, "\t", end=" ") #   "\t" is a tab to create columns! 
    print (i**2, "\t", end=" ") # comma keeps them on the same line
    print (i**3)


#for i in range (10):
i = 0
while i**3<500:
    print (i, "\t", end=" ") #   "\t" is a tab to create columns! 
    print (i**2, "\t", end=" ") # comma keeps them on the same line
    print (i**3)
    i=i+1
          
            
main()



    
def main():
    for i in range (10):
        print (i) # no comma makes each on own line
        
    for i in range (10):
    print (i, end=" ") # comma keeps it in one line
    '''
'''
for i in range (10):
    print (i, "\t", end=" ") #   "\t" is a tab to create columns! 
    print (i**2, "\t", end=" ") # comma keeps them on the same line
    print (i**3)
    '''
''' 
#for i in range (10):
i = 0
while i**3<500:
    print (i, "\t", end=" ") #   "\t" is a tab to create columns! 
    print (i**2, "\t", end=" ") # comma keeps them on the same line
    print (i**3)
    i=i+1
           
            
main()    
    
'''   


def main():

    x = input("Input the first integer: ")
    y = input("Input the second integer: ")
    x = (int(x))
    y = (int(y))
    print("The GCD of ", x, " and ", y, " is ", end=" ")
    while y != 0:
        x_prime = y
        y_prime = x % y
        x = x_prime
        y = y_prime
    print (x)
                
main()



