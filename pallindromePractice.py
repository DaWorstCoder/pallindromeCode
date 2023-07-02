def flip(input):
    input_str = str(input)
    output_str = ""
    for digit in input_str:
        output_str = digit + output_str
    return int(output_str)

def pallin(input, count):
    count += 1
    if input == flip(input):
        return (input, count)
    else:
        try:
            return(pallin(input + flip(input), count))
        except:
            return ("too big", count) #if the number is too big, we print out garbage

max = 10000 
arr = [[0 for x in range(3)] for y in range (max)]
num = 10
for row in range(len(arr)):
    output, count = pallin(num, -1)
    arr[row][0] = num
    arr[row][1] = output
    arr[row][2] = count
    num += 1

def output_arr(output_method):
    if output_method == "print":
        for row in range(len(arr)):
            print(arr[row])

    elif output_method == "write":
        file = open("C:/Users/helio/pallindromeCode/textfile.txt", "w")
        for row in range(len(arr)):
            file.write(str(arr[row][0]) + ", " + str(arr[row][1]) + ", " + str(arr[row][2]) + "\n")
        file.close()
        print("Done.")

output_arr("write")
