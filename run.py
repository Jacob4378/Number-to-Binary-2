userInput = int(input("Enter a number from 0-255: "))
if userInput > 255:
    print("Number is too big.")
elif userInput < 0:
    print("Number is too small.")
else:
    binaryNumber = ""
    for x in range (1,9):
        if userInput >= (256 / 2**x):
            binaryNumber = binaryNumber + "1"
            userInput = userInput - (256 / 2**x)
        else:
            binaryNumber = binaryNumber + "0"
        if x == 4:
            binaryNumber = binaryNumber + " "
    print(binaryNumber)