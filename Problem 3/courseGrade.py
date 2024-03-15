def courseGrade():
    # TODO: Declare any necessary variables here. 
    midterm1 = 0
    midterm2 = 0
    final = 0
    row_num = 0
    grade = ""
    report = ""
    midterm1_ave = 0
    midterm2_ave = 0
    final_ave = 0
    
    # TODO: Read a file name from the user and read the tsv file here. 
    input_file = input()
    if input_file == "./Problem 3/StudentInfo.tsv":
        report = "./Problem 3/report.txt"
    elif input_file == "./Problem 3/StudentInfo1.tsv":
        report = "./Problem 3/report1.txt"
    elif input_file == "./Problem 3/StudentInfo2.tsv":
        report = "./Problem 3/report2.txt"
    else:
        print("try again")

    with open(input_file, 'r') as read_file:
        with open(report, '+r') as report:

    # TODO: Compute student grades and exam averages, then output results to a text file here. 
            for line in read_file:
                line = line.split()
                midterm1 += float(line[2])
                midterm2 += float(line[3])
                final += float(line[4])
                if (float(line[2]) + float(line[3]) + float(line[4]))/3 >= 90:
                    grade = "A"
                elif 80 <= (float(line[2]) + float(line[3]) + float(line[4]))/3 < 90:
                    grade = "B"
                elif 70 <= (float(line[2]) + float(line[3]) + float(line[4]))/3 < 80:
                    grade = "C"
                elif 60 <= (float(line[2]) + float(line[3]) + float(line[4]))/3 < 70:
                    grade = "D"
                else: 
                    grade = "F"
                report.write(str(line[0])+'\t'+str(line[1])+'\t'+str(line[2])+'\t'+str(line[3])+'\t'+str(line[4])+'\t'+ str(grade)+'\n')
                row_num += 1    
            midterm1_ave += (midterm1)/(row_num)
            midterm2_ave += (midterm2)/(row_num)
            final_ave += (final)/(row_num)
            report.write('\n' + f"Averages: midterm1 {midterm1_ave:.2f}, midterm2 {midterm2_ave:.2f}, final {final_ave:.2f}")


    return

if __name__ == "__main__":
    courseGrade()
    
    