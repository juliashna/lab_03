print("Введите числа через пробел:")
n = [int(x) for x in input().split()]
for i in range(0,len(n)-1):
    for j in range(len(n)-1):
        if(n[j]>n[j+1]):
            temp = n[j]
            n[j] = n[j+1]
            n[j+1] = temp
print("Полученный отсортированный список методом пузырька:",n)