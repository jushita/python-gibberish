import itertools
import re
from collections import Counter, OrderedDict
from itertools import cycle, groupby
import time



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
        a = list(a)
        print(a[n:]+ a[:n])
    #Given two strings delete all chanractrs to make it anargrams.
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
        str1 = ''.join((each) for each in res1)
        for k2,v2 in dict2.items():
            if v2 == 1:
                res2.append(k2)
        str2 = ''.join((each) for each in res2)
        for k1,v1 in dict1.items():
            if v1 == 0:
                del_str1.append(k1)

        del1 = ''.join((each) for each in del_str1)
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

    # Find all the index where you can find the target element in the given string
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

    def diagonal(self, a):
        sum = 0
        for i, each1 in enumerate(a):
            for j, each2 in enumerate(each1):
                sum = sum + abs(each1[i])
                break
        print(sum)

    def hackerrank(self, a):
        a = list(a)
        b= "hackerrank"
        dict_b = dict()
        for each in b:
            dict_b[each] = 0
        for k, v in dict_b.items():
            for i, each in enumerate(a):
                if k == a[i]:
                    v = v + 1
                    dict_b[k] = v
        res = all(value >= 1 for value in dict_b.values())
        if res == True:
            print("YES")
        else:
            print("NO")

    def camelCase1(self, s):
        s_lower = s.lower()
        count = 0
        uppers = [l for l in s if l.isupper()]
        print(len(uppers)+1)

    def mapCavity(self, arr, n):
        for i in range(1, n-1):
            for j in range(1, n-1):
                if arr[i-1][j] != 'X' and int(arr[i-1][j]) < int(arr[i][j]) and \
                    arr[i+1][j] != 'X' and int(arr[i+1][j]) < int(arr[i][j]) and \
                    arr[i][j-1] != 'X' and int(arr[i][j-1]) < int(arr[i][j]) and \
                    arr[i][j+1] != 'X' and int(arr[i][j+1]) < int(arr[i][j]):
                        arr[i][j] = 'X'
        n = input()
        arr = []
        for k in range(n):
            line = list(raw_input())
            arr.append(line)
        mapCavity(arr, n)
        for line in arr:
            print (''.join(line))

    def number_needed(self, a, b):
        temp_dict_a = dict()
        temp_dict_b = dict()
        del_count = 0

        for char in sorted(a):
            if char in temp_dict_a:
                temp_dict_a[char] += 1
            else:
                temp_dict_a[char] = 1

        for char in sorted(b):
            if char in temp_dict_b:
                temp_dict_b[char] += 1
            else:
                temp_dict_b[char] = 1

        if len(temp_dict_a) > len(temp_dict_b):
            for key, value in temp_dict_a.items():
                if key in temp_dict_b:
                    del_count += abs(value - temp_dict_b[key])
                else:
                    del_count += value

            for key, value in temp_dict_b.items():
                if key not in temp_dict_a:
                    del_count += value
        else:
            for key, value in temp_dict_b.items():
                if key in temp_dict_a:
                    del_count += abs(value - temp_dict_a[key])
                else:
                    del_count += value

            for key, value in temp_dict_a.items():
                if key not in temp_dict_b:
                    del_count += value

        print (del_count)
        """"
a = input().strip()
b = input().strip()

print(number_needed(a, b))
aaaaa
bbbbbbbb
"""
    def ransom_note(self, magazine, ransom):
        a = (Counter(ransom.split(" ")))
        b = (Counter(magazine.split(" ")))
        print(b-a == {})
        '''
        dict_magazine = dict()
        dict_ransom = dict()
        ans = " "

        for each in sorted(magazine.split(" ")):
            if each in dict_magazine:
                dict_magazine[each] += 1
            else:
                dict_magazine[each] = 1
        print(dict_magazine)

        for each in sorted(ransom.split(" ")):
            if each in dict_ransom:
                dict_ransom[each] += 1
            else:
                dict_ransom[each] = 1
        print(dict_ransom)

        for key, value in dict_ransom.items():
            if key not in dict_magazine:
                print("No")
                break

            if key in dict_magazine:
                res = dict_magazine[key]-value
                if res >= 0:
                    ans = "Yes"

                else:
                    ans ="No"
        print(ans)
        '''
    def super_reduced_string(self, s):
        a = Counter(s)
        result = []
        s = " "
        for k, v in a.items():
            if v%2 == 1:
                result.append(k)
        s = "".join(result)
        if not s:
            print("Empty String")
        print(s)
    def test(self, message):
        encryptedMessage = re.sub('[^A-Za-z0-9]+', '', "Atvt hrqgse, Cnikg")
        decryptedMessage = re.sub('[^A-Za-z0-9]+', '', "Your friend, Alice")

        #print(encryptedMessage)
        fkey = list()
        mkey = list()
        key = list()
        lmessage = list()

        # find difference between encrypted and decrypted letters
        for i, each in enumerate(encryptedMessage):
            p = ord(encryptedMessage[i])-ord(decryptedMessage[i])
            fkey.append(p)

        # fix negative numbers
        for index, each in enumerate(fkey):
            if each < 0:
                fkey[index] = fkey[index] + 26

        #find real key

        i = fkey.index(0)
        for j, each in enumerate(fkey):
            while j>i and j<=fkey.index(0, i+1):
                key.append(each)
                break

        #split message
        temp_msg_list = list(message)
        print(temp_msg_list)

        counter = 0
        is_upper = False

        for index, char in enumerate(temp_msg_list):
            if counter >= len(key):
                counter = 0

            if re.match(r'[!.?\-",]+', char) or char == " ":
                lmessage.append(char)
                continue

            hold = char
            if char.isupper():
                hold = char.lower()
                is_upper = True

            hold = ord(hold) - key[counter]

            if hold < 97:
                hold += 26

            hold = chr(hold)

            if is_upper:
                is_upper = False
                hold = hold.upper()

            lmessage.append(hold)

            counter += 1

        return("".join(lmessage))

    def virus(self, a0,b0,c0):
        matrix = [a0][b0][c0]
        print(matrix)

    def createStr(self, a):
        dictionary = ["bed","okay", "bath", "and", "beyond", "this", "is"]
        res = list()
        for each in dictionary:
            if each in a:
                res.append(each)
        print(" ".join(each for each in res))

    def deleteWords(self, a, b):
        a = a.split(" ")
        b = b.split(" ")
        result = " "
        _list = list()
        Res = set(a)-set(b)
        for each in Res:
            _list.append(each)
        result = ' '.join(_list)
        print(result)

    def removeOcurance(self, a, b):
        a = a.split(" ")
        b = b.split(" ")
        _list = list()
        for i, each in enumerate(a):
            for j, each2 in enumerate(b):
                if each == each2:
                    a[i] = ""
                    b.remove(b[j])
        for each in a:
            if each == "" or each == " ":
                a.remove(each)

        result = ' '.join(a)
        print(result)

    def shortestSubstring(self, a):
        a = list(a)
        print(a)
        for i, each in enumerate(a):
            if a[i] != a[i-1]:
                pass

    def consecutiveCount(self, word):
        count=1
        length=""
        for i in range(1,len(word)):
            if word[i-1]==word[i]:
               count+=1
            else :
                length += word[i-1]+str(count)
                count=1
        length += (word[i]+str(count))
        print (length)

    def consecutiveCount1(self, a):
        groups = groupby(a)
        result = [(label, sum(1 for each in group)) for label, group in groups]
        print (result)
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

    #write an algorithm to reverse a string not in-built one
    def reverseAlgo(self, a):
        a = list(a)
        result = ""
        if not a:
            print("Error")
        while len(a) != 0:
            result += a.pop()
        print(result)

    #Create a diamond
    def diamond(self, a):
        for each in range(int((a-1)/2), 0, -1): #if a= 7; you want the first half to have 7-1/2=3 lines
            space = each
            star = a - 2*space
            print(" "*space +"*"*star+" "*space )
        for each in range(int((a-1)/2)+1): #if a = 7; you want the second have to have 7-1/2 + 1 lines
            space = each
            star = a - 2*space
            print(" "*space +"*"*star+" "*space )

    def fibonacci(self, a):
        first = 0
        second = 1
        fseries = [first, second]
        for each in range(a):
            sum = first + second
            first = second
            second = sum
            fseries.append(sum)
        print(fseries)

    def multiplicationTable(self, timestable, upto):
        for each in range(0, upto+1):
            print(str(timestable) + " X " + str(each) + " = " + str(timestable*each))
            print("%d X %d = %d" % (timestable, each, timestable*each))

    #Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.
    def absent(self, a,b):
        print(set(a)-set(b))

    #find the longest pallindrom substring
    def longestPal(self, s):
    # Declare local variable for the length of s.
        l = len(s)
        list_s = list()
        _reverse = list()
        count = 0
        # Here I chose range over xrange for python version compatibility.
        for end in range(l,0,-1):
            for i in range(l-end+1):
                list_s.append(s[i:i+end] )
        print(list_s)
        for each in list_s:
            _reverse.append(each[::-1])
        #print(_reverse)
        for i, each in enumerate(list_s):
            if each == _reverse[i]:
                count += 1
        print(count)


    def isBin(self, a):
        print(all((k == '0' or k == '1') for k in str(a)))

    def diaPrac(self, a):
        for i in range(int((a-1)/2),0,-1):
            spaces = i
            stars = a - 2*spaces
            print(" "*spaces + str(i*2+1)*stars + " "*spaces)
        for i in range(int((a-1)/2)+1):
            spaces = i
            stars = a - 2*spaces
            print(" "*spaces + str(i*2+1)*stars + " "*spaces)

    def Fibo(self, n):
        if n == 0: return(0)
        elif n == 1: return(1)
        else: return( Fibo(n-1)+Fibo(n-2))

    def twoStringsPerm(self, a, b):
        res = "YES"
        a = sorted(a)
        b = sorted(b)
        if a == b:
            print("YES")
        else:
            print("NO")
