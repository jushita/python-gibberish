import re

class Homework():
    def aveNameLen(self):
        '''
        Write a program that will accept names as input and compute average length of names as output

        '''
        #initialize an empty list to store names from file
        nlist = list()
        #open file containing list and storing in nlist as a list
        with open("names.txt", "r") as file:
            for eachLine in file:
                eachLine = eachLine.rstrip("\n")
                nlist.append(eachLine)
        #removing number values
        nlist = [item for item in nlist if not item.isdigit()]
        #if input file is empty
        if len(nlist) == 0:
            print("Please input some names!")

        else:
            nstring = " "
            #joining all names as a long string
            nstring = "".join(str(each) for each in nlist)
            #removing spaces between names
            nstring = nstring.replace(" ", "")
            #removing special characters
            nstring = re.sub('[^A-Za-z0-9]+', '', nstring)
            #removing numbers
            nstring = re.sub(r'\d+', '', nstring)
            #if invalid iput is given
            if len(nstring) == 0:
                print("Oops! Enter valid names please!")
            else:
                #printing result
                print ("Average length of all the names of students in the class is:", len(nstring)/len(nlist))
