
def main():
    
    listofstrings = []
    listofints = []
    
    inputlist = (input('Enter a list of strings and integers separated by commas: '))      # ask user for list
    newlist=(inputlist).split(', ')                                   # make the input a list (of strings)
#    print(newlist)                                                   #print the list - just checking
    numberofitems = len(newlist)                                     # how many items in the list - i'll need that in the for loop
#    print (numberofitems)                      # just checking

    # make 2 separate lists - one string list and one int list.
    # try to make item an int. if it fails, append it to the string list. if it passes, append it to the int list
    totalints = 0
    n = 0
    for n in range(0,(numberofitems)):
        try:
            int(newlist[n])
            listofints.append(newlist[n])
            n=n+1
        except:
            listofstrings.append(newlist[n])
            n=n+1
    print("The list of all the strings is " + str(listofstrings))
#    print(listofints)                      # just checking
 
    x = [int(i) for i in listofints]
    x=sum(x)  
    print("The sum of all the integers is " + str(x))

main()
