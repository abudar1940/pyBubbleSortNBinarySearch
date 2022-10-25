#Developed by Abubakr Dar (Starting from 14/10/2022)
#This will be a simple bubble sort designed for use on integer values.
#A binary search system will also be added as well


sampleList = [] #This is a list used for this sort/search
intHolder = 0  #'Holder' is normally a suffix I use for variables that store non-integral/miscellaneous information     
stHolder = ""
intStrt = 0
intMid = 0      #These variables will be used for the binary search mechanism at the end of the program
intEnd = 0
intSrch = "placeholder"     #The desired input for this is any integer value, so the string "placeholder" is used while it is not an integer
boolFound = False

print(f"List Length = {len(sampleList)}")    #This confirms the length is 0 at the start

while stHolder.lower() != "end":        #This loops while stHolder is not equal to "end" once all letters in the string have been converted to lowercase
    stHolder = str(input("Enter an integer value to add to the list. Type 'end' to stop adding values:    "))
    try:        #A try command is used to confirm an integer value has been input
        sampleList.append(int(stHolder))
    except:
        if stHolder.lower() == "end" and len(sampleList) <= 1:      #This section will ensure more than one value is input
            stHolder = ""
            print("There must be more than one integer. Please try again.")
            continue
        elif stHolder.lower() == "end": #This 'elif' will end the while loop
            continue
        else:               #This makes the program repeat if any other invalid input is received
            stHolder = ""
            print("Invalid input received, please try again")
            continue

print(f"List Length = {len(sampleList)}")

print(sampleList)   #This prints out the original list

for i in range(0, len(sampleList)):  #This is a nested for loop, it will help cycle through each element in the list
    for j in range(0, len(sampleList)): #This loop will check if the element currently selected is more than or less than the next element
        if j == len(sampleList) - 1:
            pass
        elif sampleList[j] > sampleList[j + 1]:
            intHolder = sampleList[j]
            sampleList[j] = sampleList[j + 1]
            sampleList[j+1] = intHolder
        else:
            pass
    
print(sampleList)   #This will print out the sorted list

while intSrch == "placeholder":         #This loop will ensure a correct value is input into the variable 'intSrch'
    try: 
        intSrch = int(input("Enter the number you would wish to search for:    "))
    except:
        intSrch = "placeholder"
        print("Inavlid Input")

intEnd = len(sampleList) - 1        #Variable is assigned a value here

while intEnd < intStrt or boolFound == False:       #This is the binary search. It will end once intEnd becomes less than intStrt or until boolFound becomes true
    intMid = (intEnd - intStrt) // 2        #DIV is used here to make sure an integer value is received for intMid
    if intSrch > sampleList[intMid]:
        intStrt = intMid + 1        #This statement occurs if the value is larger than the middle of the list
    elif intSrch > sampleList[intMid]:
        intEnd = intMid - 1         #This statement occurs if the value is smaller than the middle of the list
    elif intSrch == sampleList[intMid]:
        boolFound = True            #This statement occurs if the value is equal to the middle of the list
        continue

if boolFound == True:
    print(f"The integer value {intSrch} was found in the list.")        #Displays if value is found
else:
    print(f"The integer value {intSrch} was not found in the list.")       #Displays if value is not found

input("")       #Makes sure program doesn't immediately end, allowing user to read the final output message