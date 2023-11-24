s=[]
with open ('out.csv') as f:
    for line in f:
        s.append(line)
sl={}
for i in range (len(s)):
    t=s[i].split(',')
    t2=t[2]
    m=t2.find('@')
    t1=t[m+1:]
    t1=str(t1)
    if t1 not in sl:
        sl[t1]=1
    else:
        sl[t1]+=1
print(sl)
