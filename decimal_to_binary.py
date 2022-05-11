#recursive way to convert decimal number to binary
def recursive_dectobin(num):
    if num > 1:
        recursive_dectobin(int(num // 2)) # recursively apply floor division of 2 until the quotient is 0
    print(num % 2, end = "")                # print the remainder

decimal = int(input("Enter a decimal number: "))
recursive_dectobin(decimal)
print()


#iterative way to convert decimal number to binary using a while loop
decimal = int(input("Enter a decimal number: "))
def iterative_dectobin():
    binary = 0
    counter = 0
    temp = decimal #copy of decimal 

    #add the the product of remainder and its positional value
    while(temp > 0):
        binary = ((temp % 2) * (10 ** counter)) + binary
        temp = int(temp/2)
        counter += 1 

    print("Binary of ",decimal, "is", binary)

iterative_dectobin()


#converting decimal number to binary number using bin() function
def dectobin(n):
    binary = str(bin(n))
    print(binary[2:])

decimal = int(input("Enter a binary number: "))
dectobin(decimal)
