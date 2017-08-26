import itertools
import re

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
##Find duplicate in an array
##example: [2,3,3,4,5,2]
##answer will be 3. because the second index of 3 is less than the second index of 2.

    def firstDupliLowestIndex(self, a):
        new_dict = dict()
        listOfindex = list()
        result_index = 0
        if len(a)==2:
            if a[0]==a[1]:
                print(a[0])
            else:
                print("-1")
        for i, each in enumerate(a):
            new_dict[each] = 0
        for key, value in new_dict.items():
            for i, each in enumerate(a):
                if key == a[i]:
                    value += 1
                    if value == 2:
                        listOfindex.append(i)
            new_dict[key] = value
        for j, _each in enumerate(listOfindex):
            if (listOfindex[j-1]>listOfindex[j]):
                print(a[listOfindex[j]])
        if not listOfindex:
            print("-1")

#reverse a string
    def revInt(self, a):
        a = str (a)
        print (a[::-1])

#check if number is binary or not
    def checkBin(self, a):
        a = str (a)
        a = list (a)
        new_dict = dict()
        for each in a:
            new_dict[each] = 0
        for key, value in new_dict.items():
            if key == '0' or key == '1':
                value = 1
            else:
                value = 2
            new_dict[key] = value
        if all(value == 1 for value in new_dict.values()):
            print ("True")
        else: print ("False")

    def isBinary(self, a):
        a = list(a)
        for i, each in enumerate(a):
            if a[i]==1 or a[i]==0:
                return True
            else:
                return False
                break

    #the sky is blue --> blue is sky

    def revSent(self, a):
        res = " "
        line_split = a.split(" ")
        line_split = line_split[::-1]
        print (line_split)
        res = " ".join(line_split)
        print (res)

    def rotation(self, a, n):
        d=list()
        for i in range(1,a+1):
            d.append(i)
        str1 = ''.join(str(each) for each in d)
        print(str1[n:]+ str1[:n])

    def anargrams(self, a, b):
        a = list(sorted(a))
        b = list(sorted(b))
        dict1 = dict()
        dict2 = dict()
        res1 = list()
        res2 = list()
        del_str1 = list()
        del_str2 = list()
        for each in a:
            dict1[each] = 0
        for each in b:
            dict2[each] = 0
        for k1,v1 in dict1.items():
            for k2, v2 in dict2.items():
                if k1 == k2:
                    v1 = 1
                if k2 == k1:
                    v2 = 1
                dict1[k1] = v1
                dict2[k2] = v2
        for k1,v1 in dict1.items():
            if v1 == 1:
                res1.append(k1)
        str1 = ''.join((each) for each in res1 )
        for k2,v2 in dict2.items():
            if v2 == 1:
                res2.append(k2)
        str2 = ''.join((each) for each in res2 )
        for k1,v1 in dict1.items():
            if v1 == 0:
                del_str1.append(k1)

        del1 = ''.join((each) for each in del_str1 )
        print("To delete from string 1:", del1)

        for k2,v2 in dict2.items():
            if v2 == 0:
                del_str2.append(k2)

        del2 = ''.join((each) for each in del_str2 )
        print("To delete from string 2:",del2)

    def ransomNote(self, a,b, str_a, str_b):
        split_str_a = str_a.split(" ")
        split_str_b = str_b.split(" ")
        print(split_str_a)
        print(split_str_b)
        for j, each2 in enumerate(split_str_b):
            for i, each1 in enumerate(split_str_a):
                if each1==each2:
                    print("YES")
                    break
                else:
                    print("NO")
                    break


        '''
        dict_a = dict()
        dict_b = dict()

        for each in split_str_a:
            dict_a[each] = 0
        for each in split_str_b:
            dict_b[each] = 0
        for ka, va in dict_a.items():
            for kb, vb in dict_b.items():
                if ka == kb:
                    vb += 1
                dict_b[kb] = vb
        print(dict_b)
        for kb, vb in dict_b.items():
            if vb >=1:
                pass
            else:
                pass
        '''


    def findIntk(self, arr, k):
        new_dict= dict()
        for i, each in enumerate(arr):
            if i != 0:
                new_dict[each] = 0
        for key, value in new_dict.items():
            if key == k:
                value = 1
            new_dict[key] = value
        for k, v in new_dict.items():
            if v == 1:
                print("YES")
                break
            else:
                print("NO")
                break

    def  oddNumbers(self, l, r):
        liszt = range(l,r)
        for i in liszt:
            if i%2!=0:
                print (i)

    def upperCase(self, str_a):
        '''
        ab--> Ab, aB, AB, ab--> 00 01 10 11
        abc--> Abc, aBc, abC, ABc, AbC, aBC, ABC, abc
        2^2=4
        2^3=8
        2^4=16

        '''
        new_s = list()
        bin_a = ["".join(seq) for seq in itertools.product("01", repeat=len(str_a))]
        dict_a = dict()
        print([(i) for i in bin_a if i =='00'])

    def aveNameLen(self):
        '''
        Write a prog that will accept names as input compute avg length of names and output

        '''
        nlist = list()
        with open("names.txt", "r") as file:
            for eachLine in file:
                eachLine = eachLine.rstrip("\n")
                nlist.append(eachLine)
        if len(nlist) == 0:
            print("Please input some names!")
        else:
            nstring = " "
            nstring = "".join(str(each) for each in nlist)
            nstring = nstring.replace(" ", "")
            nstring = re.sub('[^A-Za-z0-9]+', '', nstring)
            print ("Average length of all the names of students in the class is:", len(nstring)/len(nlist))


        """"
        Define
        prospect
        usage
        limitation
        what else can be done
        references
        explain neural networks.. new buzz about it bla bla
        """


    def lonelyinteger(self, a):
        answer = 0
        for number in a:
            answer = answer ^ number
        print(answer ^ number)
