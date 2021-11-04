def somme(n):
    if n == 0 :
        return 0
    else:
        return (n + somme(n - 1))


n1 = int(input("Enter un nombre :"))
print(somme(n1))



