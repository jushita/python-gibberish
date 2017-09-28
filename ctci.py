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
