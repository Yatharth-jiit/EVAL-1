string = "DeveLopMent of EffecTive StrateGIES"
def func(string):
    uppercase = []
    lowercase = []
    for i in range(len(string)):
        ch = string[i]
        if ch==' ' :
            continue
        count = 1
        for j in range (i+1,len(string)):
            if (string[i]==string[j]):
                count+=1
        if (count==1):
            if (ch>='a' and ch<='z'):
                lowercase.append(ch)
            else :
                uppercase.append(ch)
    print("UPPERCASE: ",uppercase)
    print("Lowercase: ",lowercase)
func(string)