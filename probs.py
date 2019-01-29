def main():
    # prob1()
    prob2()
    prob3()




#Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number is less or equal to 1,
# or greater or equal to 10. Print the result returned from your function.

def equal10(num, outMode):

    # outMode = num >= 10 or num <= 1

    if (outMode):
        return (num <1 or num > 10)
    else:
        return (num >= 1 and num <=10)



def prob1():



    print(equal10(14, False))
    print(equal10(14, True))
    print(equal10(6, False))



#Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
#Once the user enters the equal sign to quit,
# print all the strings that were entered as one line with
# each word separated by a comma and space.

def prob2():

    askUser = input("Enter a sentence")
    printThese = [askUser]

    while askUser != "=":
        askUser = input("Enter a sentence")
        printThese.append(askUser)




    # KEY: Wher u getting these crazy VooDoo s*t?  :-)
    print(*printThese, sep = ", ")



#Given a non-negative number "num",
# return True if num is within 2 of a multiple of 10.
# Print the result from your function.

def prob3():

    print(tenTwo(31))

    def tenTwo(x):
        x = [x-1,x-2, x+2, x+1]
        for num in x:
            if num %10 == 0:
            return True
        else:
            return False














if __name__ == '__main__':
    main()