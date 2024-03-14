"""
Name: Owen Anderson
Lab Time: THUR 2:00 - 3:15
"""
def wordInRange():
    file_input = input()
    word1 = input()
    word2 = input()
    file_object = open(str(file_input))
    read_file = file_object.readlines()


    for line in read_file:
        line = line.strip('\n')
        if word1 <= line and word2 >= line:
            print(line +" - in range")
        else:
            print(line + " - not in range")

    file_object.close()
if __name__ == '__main__':
    wordInRange()