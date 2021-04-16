#Brianna Bretana
#Program creates a .txt file adds data and appends data in file
#Week 12 Assignment 2

def text_one():
    infile=open('cartoon.txt','r')
    file_content=infile.read()
    infile.close()
    print(file_content)

def text_two():
    infile=open('cartoon.txt','r')
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    infile.close()

    print(line1,end='')
    print(line2,end='')
    print(line3,end='')

text_one()
text_two()    
