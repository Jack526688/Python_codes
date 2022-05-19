pos = -1
def search(list, n):
    i = 0
    while i < len(list):
        if list[i]==n:
            globals()['pos'] = i
            return True
        i += 1
    return False
list = [5, 6, 7, 8, 9, 4]
n = 5
if search(list, n):
    print('found ', pos+1)
else:
    print('not found')