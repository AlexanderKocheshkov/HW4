print("Введите значения списка через пробел:", end=" ")
l = list(input().split(" "))

def bubbletime(l):
    n = 1
    while n <= len(l):
        for i in range(len(l)-n):
            if int(l[i]) > int(l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
        n +=1
    return (l)

print(bubbletime(l))
#Т.к. всё, что задаёт нам пользователь input() принимает как string, то при сравнении значений в списке нужно нужно перевести их в числовой тип данных (можно вместо int так же взять float), иначе программа будет работать не так как нужно. Например, если взять списо 2 8 5 3 10, где все даныне типа string, то на выходе мы получим 10 2 3 5 8