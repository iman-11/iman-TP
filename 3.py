def nbr(N):
    if N==0:
        return 0
    else:
        return 1+nbr(N//10)
N=int(input("enter un nombre:"))
print(nbr(N))





