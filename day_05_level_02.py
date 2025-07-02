#1

#punto1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
v=ages .sort()
print(v)
#punto2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages .insert(1,19)
ages .insert(11,26)
ages .sort()
print(ages)
#punto3
x= len(ages) / 2 #5
p=int(x)
position=ages[p]
print(position , ages[p+1])
#punto4
operation= sum(ages) / len(ages)
print(operation)
#punto5
q=ages .sort(reverse=True)
print(q)
#punto6
