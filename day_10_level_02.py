#1
total = 0
for i in range(101):
    total += i
print("The sum of all numbers is", total)
#2
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print("The sum of all evens is", sum_evens)  
print("The sum of all odds is", sum_odds)
      

