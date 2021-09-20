line = {}
res={}

with open("Hub/Python_code/test2.txt","r") as f:
    for i in range(10):
        line[i]=f.readline()
        s=line[i].split('')
        a=int(s[0])
        a=int(s[1])
        res[i]=(a+b)/2
with open("Hub/Python_code/test1.txt","a") as result:
    for i in range(10):
        res[i]=str(res[i])
        result.write(res[i]+"\n")
