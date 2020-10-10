string=input("enter a string:")
dict={}
for ch in string:
        if (ch not in dict):
            dict[ch]=1
        else:
            dict[ch]+=1
data=""
for k,v in dict.items():
    data+=str(v)+k
print(data)


