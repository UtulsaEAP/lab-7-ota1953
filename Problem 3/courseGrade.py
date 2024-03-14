def courseGrade():
    # TODO: Declare any necessary variables here. 
    ave = []
    letter_grade = "" 
    
    # TODO: Read a file name from the user and read the tsv file here. 
    input_file = input()
    open_file = open(input_file)
    read_file = open_file.readlines()
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    for val in read_file:
        if isinstance(val, int):
            ave.append(val)
            print(ave)


    return

if __name__ == "__main__":
    courseGrade()
    
    