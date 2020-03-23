
def enlarge(i):
    return i * 100

#need to remove from global scope in order to import other things from this script
#my_number = float(input("Please input a number:"))
##n = enlarge(8)
#n = enlarge(my_number)
#print("ENLARGING NUMBER..." + str(n))

if __name__ == "__main__":
    # only run this if invoked from command-line
    # not if imported by another file
    #Previous problem was that the test file was importing all the useless stuff below
    my_number = float(input("Please input a number:"))
    #n = enlarge(8)
    n = enlarge(my_number)
    print("ENLARGING NUMBER..." + str(n))

    