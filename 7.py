L1=[3,2,0,1,5]
L2=[9,4,8,6,7]
L3=[]
print(L1)
print(L2)
for i in range(len(L1)):
    F=i%2
    if (F!=0):
        L3.append(L1[i])
for i in range(len(L2)):
    F=i%2
    if (F==0):
        L3.append(L2[i])
print(L3)







