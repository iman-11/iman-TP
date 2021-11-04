def chang_dictio(l):
    dic={}
    for i in l :
        y=l.count(i)
        dic[i]=y
    return dic
liste=[11,45,8,11,23,45,23,45,23,45,89]
print(chang_dictio(liste))








