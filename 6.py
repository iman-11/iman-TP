def find_position(x):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j] == x:
                return print("la position de cet élement est :", i, j)
    else:
        return print("cet élement n’existe pas.")


l = [[1, 3, 9, 4], [5, 6, 7, 8]]
n = int(input("entrer une valeur :"))
find_position(n)







