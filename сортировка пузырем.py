a = list(map(lambda x: int(x),input().split()))
count = 1

for i in range(1,len(a)):
    for j in range(1,len(a)):
        if a[j]<a[j-1]:
            count += 2
            c = a[j-1]
            a[j-1] = a[j]
            a[j] = c
    count += 1  

print(a)
print('Сложность пузырька =',count)

for i in range(1,len(a)):
    for j in range(i):
        print(a[j],end = '')
    print()