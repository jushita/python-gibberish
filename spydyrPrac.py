# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 13:30:57 2017

@author: Jrahman
"""

def Permute(string):
    if len(string) == 0:
        return ['ERROR']
    prevList = Permute(string[1:len(string)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList

#print(Permute("abc"))
'''
def palindromes(text):
    text = text.lower()
    results = []

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]
            if chunk == chunk[::-1]:
                results.append(chunk)
    return results[text.index(max(results, key=len))]


print(palindromes("adsgeegeegkkjjhdd"))

def palindromes(text):
    text = text.lower()
    if not text:
        print ("ERROR")
    results = []
    x = []
    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i+1]
            if chunk == chunk[::-1]:
                results.append(chunk)
    for i, each in enumerate(results):
        if len(results[i])>len(results[i-1]):
            final_result_length = len(results[i])
            final_result = results[i]
    return final_result, final_result_length
print (palindromes("adsgeegeegkkjjhdd"))

#How to find first non repeated character of a given String?
#s,w,i,s,s

def nonRepChar(string):
    string = string.lower()
    result =''
    if not string:
        print("Error")
    list_of_string = list(string)
    for i, each in enumerate(list_of_string):
        if list_of_string[i] == each:
            continue
        elif list_of_string != each:
            result.append(each)
            print(result)
    return result

print (nonRepChar("swiss"))
'''
def firstDupliLowestIndex(a):
    a=[2,3,3,1,4,2]
    for i, each in enumerate(a):
        print (a[i])
