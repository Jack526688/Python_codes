x = int(input('How much candies you want ? '))
av = 10
i = 1
while i <= x:
    if i > av:
        print('Out of stock')
        break
    print('candy')
    i += 1
print('Thank you')
