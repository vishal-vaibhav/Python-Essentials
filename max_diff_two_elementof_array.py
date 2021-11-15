"""
Program to find Mimimum difference between elements of array
Algo:
1) Sort the elements of array
2) Initialise the first difference value to be smallest.
3) compare elements with its adjacent element & keep track of maxmum difference.


"""


def max_diff_ele(arr):
	arr=sorted(arr)
	size =len(arr)
	max_diff = - 999*999

	for i in range(size-1):
		if(arr[i+1] - arr[i] > max_diff):
			max_diff = arr[i+1] - arr[i]
	return max_diff


arr = [5,32,45,4,12,18,25]
print("Maximum difference between elements of an array is", max_diff_ele(arr))# output: 13