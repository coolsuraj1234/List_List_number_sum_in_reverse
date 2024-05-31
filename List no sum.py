number1 = input("please enter the first number: ") # to get the first number
output1 = []
for i in number1:
    output1.append(int(i))
output1.reverse()

number2 = input("please enter the second number: ")  # to get the second number
output2 = []
for p in number2:
    output2.append(int(p))
output2.reverse()

output = [] # to store the final output

len1 = len(output1)
len2 = len(output2)

largest = max(len1, len2) # finding the largest of em so that the loop may run that many times

common = int(0)

for i in range(0 , largest):
    if i < len1:
        x1 = output1[i]
    else:
        x1 = 0

    if i < len2:
        x2 = output2[i]
    else:
        x2 = 0

    sum = int(x1) + int(x2) + common
    common = 0

    if sum > 9:
        y = str(sum)
        output.append(int(y[1]))
        common = int(y[0])
        if i == largest - 1:
            output.append(common)
    else:
        output.append(sum)

print("The sum is ", output)

