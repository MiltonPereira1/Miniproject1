'''
#Pattern A: nested for loop using range() function

for a in range(1,2):  #a is row 1 
    print("*")      #row 1 has one *
    for b in range(1,2):  #b is row 2
        print("**")     #row 2 has two *
        for c in range(1,2):  #c is row 3
            print("***")    #row 3 has three *
            for d in range(1,2):  #d is row 4
                print("****")   #row 4 has four *
                for e in range(1,2):   #e is row 5
                    print("*****")  #row 5 has five *
                    for f in range(1,2):  #f is row 6
                        print("****")   #row 6 has four *
                        for g in range(1,2):  #g is row 7
                            print("***")    #row 7 has three *
                            for h in range(1,2):  #h is row 8
                                print("**")     #row 8 has two *
                                for i in range(1,2):  #i is row 9
                                    print("*")      #row 9 has one *


#Pattern B: Zig-zag pattern through the use of a function, a list and if statements

def pattern_function():   #this line is used for creating a function called pattern_function
    L1=[0,1,2,3,4,5,6,7,8,9]   #this line describes a list, L1, of ten elements starting from 0 and ending to 9
    for n in L1:   #this for loop is used to print the pattern over L1 indexes
        if n==1 or n==8:
            print(" *")    #these two lines indicate that if n is 1 or 8, the * moves forward in position by 1 space
            continue       #the continue keyword is used to tell the program to move to the next iteration of the loop
        if n==2 or n==7:
            print("  *")   #these two lines indicate that if n is 2 or 7, the * moves forward in position by 2 spaces
            continue       #the continue keyword is used to tell the program to move to the next iteration of the loop
        if n==3 or n==6:
            print("   *")  #these two lines indicate that if n is 3 or 6, the * moves forward in position by 3 spaces
            continue       #the continue keyword is used to tell the program to move to the next iteration of the loop
        if n==4:
            continue       #these two lines indicate that if n is 4, the program is to move the next iteration of the loop
        if n==5:
            print("    *") #these two line indicate that if n is 5, the * moves forward in position by 4 spaces
            continue       #the continue keyword is used to tell the program to move to the next iteration of the loop
        print("*")         #this line is used to indicate that n is 0 and 9, one * is printed on the left side of the code


pattern_function()
pattern_function()
pattern_function()         #these three lines are used to call the function pattern_function three times and print a zig-zag pattern

'''
