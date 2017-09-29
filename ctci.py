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
    
