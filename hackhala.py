import string
j=list(string.ascii_lowercase)
d="diablo"
n="\n"
with open("diablo.txt", "w") as f:
    for i in j:
        a=(d+i)
        b=(i+d)
        for i in j:
            c=(a+i+n)
            e=(i+b+n)
            g=(b+i+n)
            f.write(c)
            f.write(e)
            f.write(g)