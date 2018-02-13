def countUnset(num):
    f_value=complete_binary(num)
    unset=0
    cont=0
    while (cont<len(f_value)):
        if(f_value[cont]=="0"):
            unset+=1
        cont+=1
    return unset

def complete_binary(num):
    bin=len((convert(num)))
    if(bin%4==0):
        value=str(convert(num))
    elif(bin%4 ==2):
        value="00"+str(convert(num))
    elif(bin%4==1):
        value="000"+str(convert(num))
    elif(bin%4==3):
        value="0"+str(convert(num))
    return value

def convert(num):
    if num==0:
        return ""
    else:
        return str(convert(num//2))+str(num % 2)

print countUnset(65535)
print countUnset(12547)
print countUnset(37)
print countUnset(13450)

