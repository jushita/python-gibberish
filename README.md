# python-gibberish

Different data stuctures and algorithms implemented in python.

## practiceProg.py

Includes problems for interview practices. Collected from Codefights, Javarevisted, Hackerrank.

### List of Practiced problems:

1. Write code to check a String is palindrome or not?
2. Write a method which will remove any given character from a String?
3. How to find first non repeated character of a given String?
4. How to count occurrence of a given character in a String?
5. How to check if two String are Anagram?
6. In an array 1-100 numbers are stored, one number is missing how do you find it?
7. In an array 1-100 multiple numbers are duplicates, how do you find it?
8. Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.
9. How do you find second highest number in an integer array?
10. How to find all pairs in array of integers whose sum is equal to given number?
11. How to remove duplicate elements from array
12. How to find top two maximum number in array?
13. Find duplicate in an array.
```
Input:  [2,3,3,4,5,2]
Output: 3
Explanation: Because the second index of 3 is less than the second index of 2.
```
14. Reverse a string.
15. Check if number is binary or not.
16. the sky is blue --> blue is sky
17. Reverse a string
18. Rotate a string
19. Given two strings delete all characters to make it anagrams.
20. Ransom Note (Hacker rank Cracking the coding interview)
21. Find all the index where you can find the target element in the given string
22. Find odd numbers
23. Write a program that will accept names as input compute average length of names and output
24. Find the lonely Integers
25. Some hackerrank problem
26. Find how many words there are in a camel cased string.
```
Input: myNameIsJushita
Output: 4
```
27. Find balanced parenthesis
28. Map Cavity problem
29. Twitter Interview Online Test
    Alice and Bob are avid Twitter users and tweet to each other every day. One day, Alice decides to send Bob a secret message by encrypting it and tweeting it publicly to Bob. They had anticipated a scenario like this, and exchanged a shared secret key some time in the past. Unfortunately, Alice isn’t very familiar with encryption algorithms, so she decides to make her own. Her encryption algorithm works as follows:
    1. Choose a key entirely composed of digits 0 - 9, for example: 12345.
    2. Iterate each letter of the plaintext message and rotate the letter forward a number of times equal to the corresponding digit in the key. If the rotation of the letter passes Z, start back at A.
    3. If the message is longer than the key, loop back to the first digit of the key again, as many times as needed.
    4. If a non-alphabetical character is encountered, leave it as it is and don’t move to the next digit in the key.
    5. Characters should maintain their upper or lowercase orientation after rotation.
    Here is an example message and its encrypted output using Alice’s algorithm:
    ```
    Original message: Hi, this is an example
    Example Key: 4071321
    Encrypted message: Li, ailu jw facntll
    Where H was rotated forward 4 letters to L, i rotated 0 to i, t rotated forward 7 letters to a, etc.
    ```
    Satisfied with the security of her algorithm, Alice tweets the following ciphertext to Bob:
    Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg
    Uh oh! Unfortunately for Alice and Bob, you are “Eve”, the world’s greatest hacker. You’ve been intercepting Alice’s messages for some time now, and know she always ends her messages with the signature “-Your friend, Alice”. You job is now as follows:
    Determine the key Alice is using.
    Using this key, write a function to decrypt any future communications from Alice. This method should take the encrypted string as an input and return the original unencrypted string.
30. Given a string split it to individual words.
```
Input: bedbathandbeyond
Output: bed bath and beyond
```
31. Remove occurance from a string
32. Find the shortest substring
33. Count consecutive characters.
```
Input: aabbbaaacd 
output: a2b3a3c1d1
```
34. Write a program that will accept names as input and compute average length of names as output

## leetcode.py

Problems from leetcode

### List of Problems

1. Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
## ctci.py

Cracking the Coding Interview Pythonic Solutions

### Chapter 1: Array and String
1.1 Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
