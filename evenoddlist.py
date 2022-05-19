def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even, odd

lst=[10,20,30,40,13,7]
e, o=count(lst)
print("even : {} and odd : {}".format(e, o))

