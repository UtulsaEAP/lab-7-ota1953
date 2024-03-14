def fileNameChange():
    #type your code here
    input_file = input()
    open_file = open(input_file)
    read_file = open_file.readlines()

    for line in read_file:
        line = line.replace('photo.jpg','info.txt')
        print(line)
    open_file.close()


    return

if __name__ == '__main__':
    fileNameChange()