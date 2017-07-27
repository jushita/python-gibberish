import itertools


class practiceProg():
    #Write code to check a String is palindrome or not?
    def isPallindrom (self, string):
        reversed_string = string [::-1]
        if not string:
            print ("ERROR. Please Enter a string and try again")
        elif (string==reversed_string):
            print ("Pallindrom")
        else:
            print ("Not Pallindrom")

    #Write a method which will remove any given character from a String?

    def removeChar(self, string, char):
        newString = list()
        if not string:
            print ("ERROR. Please Enter a string and try again")
        elif not char:
            print ("ERROR. Try again")
        string = list(string)
        for i, each in enumerate(string):
            if char != string[i]:
                ns = string[i]
                newString.append(ns)

        newString=''.join(newString)
        print(newString)

#How to find first non repeated character of a given String?

    def nonRepChar(self, string):
        string = string.lower()
        result =''
        dict_string = dict()
        if not string:
            print("Error")
        list_of_string = list(string)

        for i, each in enumerate(list_of_string):
            dict_string[each] = 0

        for key, value in dict_string.items():
            for i, each in enumerate(list_of_string):
                if list_of_string[i] == key:
                    value += 1
            dict_string[key] = value
        for key, value in dict_string.items():
            if value == 1:
                print (key)
                break

#How to count occurrence of a given character in a String?

    def countOcc(self, string):
        string = string.lower()
        result =''
        dict_string = dict()
        if not string:
            print("Error")
        list_of_string = list(string)

        for i, each in enumerate(list_of_string):
            dict_string[each] = 0
        for key, value in dict_string.items():
            for i, each in enumerate(list_of_string):
                if list_of_string[i] == key:
                    value += 1
            dict_string[key] = value
        for key, value in dict_string.items():
            print (key, value)

#How to check if two String are Anagram?

    def anargram(self, string1, string2):
        string1 = string1.lower()
        string2 = string2.lower()
        if not (string1 or string2):
            print("Error")

        string1 = sorted(string1)
        string2 = sorted(string2)

        if string1 == string2:
            print ("Anagram")
        else:
            print ("Not Anagram")

#In an array 1-100 numbers are stored, one number is missing how do you find it?

    def findNum(self, given):
        sumOfnums = sum(range(1,11))
        sumOfgiven = 0
        if given == []:
            print("error")
        for i, each in enumerate(given):
            sumOfgiven += given[i]
        result = sumOfnums - sumOfgiven

        print(result)

#In an array 1-100 multiple numbers are duplicates, how do you find it?

    def countDupli(self, array):
        d = dict()
        for i, each in enumerate(array):
            d[each] = 0
        for key, value in d.items():
            for i, each in enumerate(array):
                if key == array[i]:
                    value += 1
                    d[each] = value
            if value == 2:
                print(key)

#Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.

    def matchArray(self, array1,array2):
        d1 = dict()
        d2 = dict()
        if not (array1 or array2):
            print ("ERROR")
        for i, each in enumerate(array1):
            d1[each]=0
        for j, _each in enumerate(array2):
            d2[_each]=0
        for key1, value1 in d1.items():
            for key2, value2 in d2.items():
                if key1 == key2:
                    value1 +=1
                    d1[key1]=value1
            if value1 == 0:
                print(key1)


# How do you find second highest number in an integer array?
    def secondHighest(self, array):
        array = sorted(array)
        print (array[len(array)-2])

#How to find all pairs in array of integers whose sum is equal to given number?
    def findPairEqualToSum(self, array, num):
        if not array:
            print ("ERROR")
        if not num:
            print ("ERROR")
        res1 = list()
        res2 = ''
        for i, each in enumerate(array):
            for j, each in enumerate(array):
                sumoftwo = array[i]+array[j]
                if sumoftwo == num:
                    res1.append(str(array[i]))
                    res1.append(str(array[j]))
                    res1.append("\n")
        #print (res1)

        for i, each in enumerate(res1):
            res2='\t'.join(res1[0:i+3])
            #res2=''.join("\n")
        print (res2)

# How to remove duplicate elements from array
    def removeDupli(self, array):
        result_array = list()
        dict_array = dict()
        for i, each in enumerate(array):
            dict_array[each] = 0
        for key, value in dict_array.items():
            result_array.append(key)
        print(result_array)

#How to find largest and smallest number in array?
    def findNums(self, array):
        array = sorted(array)
        print(array)
        for i, each in enumerate(array):
            smallest = array[0]
            largest = array[len(array)-1]

        print(smallest, largest)

#How to find top two maximum number in array?

    def findTwoLargestNums(self, array):
        array = sorted(array)
        print(array)
        for i, each in enumerate(array):
            smallest = array[len(array)-2]
            largest = array[len(array)-1]

        print(smallest, largest)
