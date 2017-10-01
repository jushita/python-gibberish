class Ctci():
    def uniqueChar(self, s):
        res = "True"
        uchars = set()
        print(uchars)
        for c in s:
            if c in uchars:
                res = "False"
            uchars.add(c)
        print(uchars)
        print(res)
    #Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)
    def revCstring(self, a):
        #this question is not suitable to be implemented in python
        a = a[:-1]
        a = a[::-1]
        print(a+"0")

    #Design an algorithm and write code to remove the duplicate characters
    #in a string without using any additional buffer. note: One or two additional variables are fine.
    #An extra copy of the array is not.
    #FOLLOW UP
    #Write the test cases for this method.
    def removeDuplicate(self, a):
        if not a:
            print("Empty string")
        res_a = sorted(set(a))
        result = ""
        for each in res_a:
            result += each
        print (result)

    #Write a method to decide if two strings are anagrams or not.
    def anargrams(self, a, b):
        if not a:
            print("Invalid Input")
        elif not b:
            print("Invalid Input")
        elif sorted(a)==sorted(b):
            print("anagram")
        else:
            print("not anargram")

    #Write a method to replace all spaces in a string with ‘%20’.
    def removeSpaces(self, a):
        result = ""
        #using in built function

        #print(a.replace(" ", "%20"))

        #not using in built function
        for i, each in enumerate(a):
            if ord(each) == ord(" "):
                result += '%20'
            else:
                result += each
        print(result)
