def somme(N):
    F=1
    S=0
    for i in range(1,N+1):
        F=F*i
        S=S+(F/i)
    return S
N=5
print("la somme est:",somme(N))


