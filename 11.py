def cle(list,dict):
    l=[]
    l.extend(dict.values())
    new_list=[]
    for i in list:
        for j in l:
            if i==j:
                new_list.append(i)
    return new_list

l=[47,64,69,37,76,83,95,97]
dict1={'yassine':47,'Mouna':69,'mohamed':76,'imane':97}
print(cle(l,dict1))








