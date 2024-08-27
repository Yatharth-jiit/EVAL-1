def repWord(string):
    mydict={}
    string = string.strip()
    i=0
    while i<len(string):
        instr =""
        while (string[i]!=' '):
            instr=instr+string[i]
            i+=1
        i+=1
        if instr not in mydict:
            mydict[instr]=0
        else:
            mydict[instr]+=1
    print(mydict)

def repAlpha(string):
    maxcnt = 1
    for i in range(len(string)):
        ch = string[i]
        cnt=1
        
        for j in range(i+1,len(string)):
            if (ch==string[j]):
                cnt+=1
        if cnt>maxcnt:
            maxcnt=cnt
            alphabet = ch
    print(alphabet,"-",maxcnt)


string = "can you can a can as a canner can can a can"
repAlpha(string)