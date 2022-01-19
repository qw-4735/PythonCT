from audioop import reverse

n, k = map(int, input().split())

for i in range(n) :
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
 
sum_list = sum(a)

print(sum_list)