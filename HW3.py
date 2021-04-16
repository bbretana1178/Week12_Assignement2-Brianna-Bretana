#Brianna Bretana
#Program opens previously created .txt file and reads the full thing in one function and only 3 lines in 
#the second function
#Week 12 Assignment 2

#Created the first function
def text_one():
#Opens the cartoon file to read mode
    infile=open('cartoon.txt','r')
#Creates variable for the read commpand
    file_content=infile.read()
#Close file and print the variable/file contents
    infile.close()
    print(file_content)

#Second function
def text_two():
#Opens with read mode
    infile=open('cartoon.txt','r')
#Reads the first three lines from the file and creates variables for the lines
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
#Close file
    infile.close()

#Prints the lines supressing the newline commands
    print(line1,end='')
    print(line2,end='')
    print(line3,end='')

text_one()
text_two()    
