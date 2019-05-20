import random,sys
__auth__='12end'
string='12end'

dic={}
r=range(33,127)
for i in r:
    for j in r:
        m=chr(i)
        n=chr(j)
        tar=chr(i^j)
        if(ord(tar) in r):
            if(tar in dic):
                dic[tar]+=m+n
            else:
                dic[tar]=m+n

def solve(string):
    a=''
    b=''
    for i in string:
        num=random.randrange(0,len(dic[i]),2)-1
        a+=dic[i][num]
        b+=dic[i][num-1]
    print(a)
    print(b)

if __name__=='__main__':
    string=sys.argv[1]
    while(input('"q" to quit,other to random:')!='q'):
        solve(string)