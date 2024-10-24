#perfect numbers
my_list = []
for x in range(1, 1000000):
    divisors_sum = 0
    for y in range(1, x):
        if x % y == 0:
                divisors_sum += y
    if divisors_sum == x:
         my_list.append(x)
print(my_list)