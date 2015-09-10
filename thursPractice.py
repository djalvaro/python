'''
Created on Sep 10, 2015

@author: PC-43
'''
'''
    
def samplelist():    
    
    sampleList = [1,2,3,4,5,6,7,8]
    for a in samplelist:
        print (a)
    
samplelist()   
'''

'''
def alist():
    mylist = [1,2,3,4,5,6,7,8]
    print (mylist[1:5])
    mylist.insert(2,777)
    print (mylist)
    
alist()


'''
'''  
def alist():
    mylist = [5,7,9, "Bob", "Apple", 11, 15.0]
    for a in mylist:
        print(a)
        
    mylist.reverse()
    print("") #-------here's a space
    for a in mylist:
        print(a)
    
    mylist.pop() 
    print("") #-------here's a space
    for a in mylist:
        print(a)
    #print (mylist[1:5])
    #mylist.insert(2,777)
    #print (mylist)
    
alist()

'''
'''
myTuple = (1,2,3)     # tuple
myList = list(myTuple)  # turn it into a list
myList.append(4)   #append
print (myList)      

myTuple2 = tuple(myList)
print (myTuple2)

'''

def exceptioncontrol():
    yoursmart=False
    while(yoursmart==False):
        try:
            a=int(input("Tell me your age"))
            print("You were born in the year ",2015-a)
            yoursmart=True
        except:
            print("You gave me a string")

    
exceptioncontrol()
 
    
    
    
    
    