print("Введите числа через пробел:")
n = [int(x) for x in input().split()]
def Bubble(n):
    for i in range(0, len(n) - 1):
        for j in range(len(n) - 1):
            if (n[j] > n[j + 1]):
                temp = n[j]
                n[j] = n[j + 1]
                n[j + 1] = temp
    return n
while True:
    answer = int(input("Выберете направление сортировки:\n1 - По возрастанию\n2 - По убыванию\n"))
    if (answer > 2 or answer < 0):
        print("Вы выбрали несуществующее направление. Попробуйте ещё раз")
    elif (answer == 1):
        print("Полученный отсортированный список методом пузырька по возрастанию:", Bubble(n))
    elif (answer == 2):
        rev = list(reversed(Bubble(n)))
        print("Полученный отсортированный список методом пузырька по убыванию:", rev)
    break;