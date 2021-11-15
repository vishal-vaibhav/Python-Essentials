"""
Program to find Mimimum difference between elements of array
Algo:
1) Sort the elements of array
2) Initialise the first difference value to be largest.
3) Start comparing the difference of the first element with it.
4) compare elements with its adjacent element & keep track of minimum difference.


"""


def min_diff_ele(arr):
	arr=sorted(arr)
	size =len(arr)
	min_diff = 9999*999

	for i in range(size-1):
		if(arr[i+1] - arr[i] < min_diff):
			min_diff = arr[i+1] - arr[i]
	return min_diff


arr = [5,32,45,4,12,18,25]
print("Minimum difference between elements of an array is", min_diff_ele(arr))