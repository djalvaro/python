'''
Created on Sep 8, 2015

@author: PC-43
'''
'''
def main():
    
    a=5.0/9.0
    b=5.0/9
    c=5/9.0
    d=5/9
    e=9.0/5.0
    f=9.0/5
    g=9/5.0
    h=9/5
    biglist= (a, b, c, d, e, f, g, h)
    print (biglist)
       

    
    
main()
'''

def main():
    tempC = input("What is the temperature in Celsius?")
    tempC = (int(tempC))
    # multiply by 1.8 (or 9/5) and add 32
    tempF = (tempC * 1.8 + 32) 
    print (tempF)
    
 main()   
    
    
    
    
'''
a=input("First")
b=input("Second")
c=a/b
print(c)

main()