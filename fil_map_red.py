from functools import reduce

nums = [1, 2, 3, 57, 89, 7, 79, 7, 10, 112]
even = list(filter(lambda n: n % 2 == 0, nums))
print('-------- 1',even)
double = list(map(lambda n: n+2, even))
print('--------2',double)
sum = reduce(lambda a, b: a+b, double)
print(sum)
