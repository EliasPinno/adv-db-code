# Take in input
inputString = input("Give me the actual input: ")
splitInput = inputString.split(";")
numTransactions = int(input("Give me how many transactions there are: "))
print()
# Create header
for i in range(1,numTransactions+1):
    print("t"+str(i), end="\t|")
print()
# Create table
for item in splitInput:
    if item == "" or item == " ":
        continue
    for i in range(1,numTransactions+1):
        if(int(item[1]) == i):
            print(item, end="\t|")
        else:
            print("  ", end="\t|")
    print()
