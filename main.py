import time
text = open("test.txt", "rb").read()
# Input text
#text="00101010101010000111110101010101010101010"
#reverese text
#text=text[::-1]
# Print the input text
print("Input sequence:  " + text)
print ("Encoding input sequence")

# Get time
delta0 = time.time()

# Encoding by giving an index _ Factorizing #
index = 0
cnt=0
database = []

while index < len(text):
    length = 0
    temp = -1
    count = -1
    not_found_flag = 1
    cnt=cnt+1
    for i in range(index, len(text)):
        count = text.rfind(text[index:index + length + 1], 0, index)
        if count >= 0:
            length += 1
            temp = count
            not_found_flag = 0

    if not_found_flag:
        print ("{0:10}".format("(0,0)") + "{0:5}".format(text[index]) + text[0:index] + "[" + text[index] + "]" + text[index + 1:])
        database.append([0, 0, text[index]])
        index += 1
    else:
        if index + length < len(text):
            print ("{0:10}".format("(" + str(index - temp) + "," + str(length) + ")") + "{0:5}".format(text[index + length]) + \
                   text[0:temp] + "[" + text[temp:temp + length] + "]" + text[temp + length:index] + "[" + \
                   text[index:index + length] + "]" + text[index + length:])
            database.append([index - temp, length, text[index + length]])
            index += length + 1
        else:
            print ("{0:10}".format("(" + str(index - temp) + "," + str(length - 1) + ")") + "{0:5}".format(text[index + length - 1]) + \
                   text[0:temp] + "[" + text[temp:temp + length - 1] + "]" + text[temp + length - 1:index] + "[" + \
                   text[index:index + length - 1] + "]" + text[index + length - 1:])
            database.append([index - temp, length - 1, text[index + length - 1]])
            break
# End of encoding_output the factors #
file1=open("test.txt","w")
file1.writelines(str(database))
file1.close()

print ("Decoding stored sequence")

# Decoding #
new_text = ""
for i in range(0, len(database)):
   
    if database[i][0] == 0 and database[i][1] == 0:
        new_text = new_text + database[i][2]
        print ("{0:10}".format("(0,0)") + "{0:5}".format(database[i][2]) + new_text)
    else:
        index = database[i][0]
        length = database[i][1]
        new_text = new_text + new_text[len(new_text) - index: len(new_text) - index + length] + database[i][2]
        print ("{0:10}".format("(" + str(index) + "," + str(length) + ")") + "{0:5}".format(database[i][2]) + new_text)
# End of Decoding #
delta1 = time.time()

print ("Old text: " + text)
print ("New text: " + new_text)
print ("New text == Old text: " + str(new_text == text))
print ("Compressed file size: " + "{:.2f}".format(3 * float(len(database)) / len(text) * 100) + "%")
print ("Elapsed time: " + "{:.5f}".format((delta1 - delta0)*100) + "ms")

print(cnt)


text=text[::-1]
# Print the input text
print("Input sequence:  " + text)
print ("Encoding input sequence")

# Get time
delta0 = time.time()

# Encoding by giving an index _ Factorizing #
index = 0

database = []
cnt2=0
while index < len(text):
    length = 0
    temp = -1
    count = -1
    not_found_flag = 1
   
    for i in range(index, len(text)):
        count = text.rfind(text[index:index + length + 1], 0, index)
        if count >= 0:
            length += 1
            temp = count
            not_found_flag = 0

    if not_found_flag:
        print ("{0:10}".format("(0,0)") + "{0:5}".format(text[index]) + text[0:index] + "[" + text[index] + "]" + text[index + 1:])
        database.append([0, 0, text[index]])
        index += 1
    else:
        if index + length < len(text):
            print ("{0:10}".format("(" + str(index - temp) + "," + str(length) + ")") + "{0:5}".format(text[index + length]) + \
                   text[0:temp] + "[" + text[temp:temp + length] + "]" + text[temp + length:index] + "[" + \
                   text[index:index + length] + "]" + text[index + length:])
            database.append([index - temp, length, text[index + length]])
            index += length + 1
        else:
            print ("{0:10}".format("(" + str(index - temp) + "," + str(length - 1) + ")") + "{0:5}".format(text[index + length - 1]) + \
                   text[0:temp] + "[" + text[temp:temp + length - 1] + "]" + text[temp + length - 1:index] + "[" + \
                   text[index:index + length - 1] + "]" + text[index + length - 1:])
            database.append([index - temp, length - 1, text[index + length - 1]])
            break
# End of encoding_output the factors #


# Decoding #
new_text = ""
for i in range(0, len(database)):
    cnt2=cnt2+1
    if database[i][0] == 0 and database[i][1] == 0:
        new_text = new_text + database[i][2]
        print ("{0:10}".format("(0,0)") + "{0:5}".format(database[i][2]) + new_text)
    else:
        index = database[i][0]
        length = database[i][1]
        new_text = new_text + new_text[len(new_text) - index: len(new_text) - index + length] + database[i][2]
        print ("{0:10}".format("(" + str(index) + "," + str(length) + ")") + "{0:5}".format(database[i][2]) + new_text)
# End of Decoding #
delta1 = time.time()

print ("Old text: " + text)
print ("New text: " + new_text)
print ("New text == Old text: " + str(new_text == text))
print ("Compressed file size: " + "{:.2f}".format(3 * float(len(database)) / len(text) * 100) + "%")
print ("Elapsed time: " + "{:.5f}".format((delta1 - delta0)*100) + "ms")

print(cnt)
print(cnt2)

