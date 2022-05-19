a=19
print(id(a))

def some():

    a = 10
    x = globals()['a']
    print(id(x))
    print(a)

    globals()['a']=45

some()

print(a)

