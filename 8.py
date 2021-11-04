L=[1,2,3,4,5,6,7,8,9]
L1=[]
L2=[]
L3=[]
for i in range(3):
    L1.append(L[i])
L1 = L1[::-1]
print(L1)
for i in range(3,6):
    L2.append(L[i])
L2=L2[::-1]
print(L2)
for i in range(6,len(L)):
    L3.append(L[i])
L3=L3[::-1]
print(L3)








