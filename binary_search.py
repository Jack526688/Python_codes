
def binary_search(arr, low, high, x):

	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)
	else:
		return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 2

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")



# pgm2


# pos = -1
# def search(list, n):
#     l = 0
#     u = len(list)-1
#     while l <= u:
#
#         mid = l+u//2
#
#         if list[mid] == n:
#             globals()['pos']=mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid+1
#             else:
#                 u = mid+1
#     return False
#
# list = [1, 46, 55, 66, 77, 81, 99]
# n  =  66
#
# if search(list, n):
#     print('found',pos+1)
# else:
#     print('not found')
