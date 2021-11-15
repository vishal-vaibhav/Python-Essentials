"""
Program to find: given 'n' non-negative integers representing 
an elevation map where the width of each bar is 1. 
the amount of water that is trapped between these bars after 
raining.

A = [1,0,2,0,1,0,3,1,0,2]

Algo:
1) Build an array left of size 'n' where lift[i] represents maximum
height bar that is left to it including i th bar.
2) Build an array right of size 'n' where right[i] represents max height bar
that is right to it including i th bar
3) sum=0;
repeat for every i th bar (0<i<n)
sum = sum + min (left[i], right[i]) - height[i]
"""

def rain_trap(arr):
	size=len(arr)
	water = 0

	left = size *[0]
	right = size *[0]
	left[0] = arr[0]

	max_so_far_left=arr[0]
	for index in range(0,size):
		if(max_so_far_left < arr[index]):
			max_so_far_left = arr[index]
			left[index] = max_so_far_left
		else:
			left[index] = max_so_far_left

	max_so_far_right = arr[-1]
	for index in range(size-1, -1, -1):
		if(max_so_far_right < arr[index]):
			max_so_far_right = arr[index]
			right[index] = max_so_far_right
		else:
			right[index] = max_so_far_right

	#print(left)
	#print(right)
	for index in range(0,size):
		water = water + min(left[index],right[index]) - arr[index]
	return water

A = [1,0,2,0,1,0,3,1,0,2]
#rain_trap(A)

print(rain_trap(A)) #output 9



