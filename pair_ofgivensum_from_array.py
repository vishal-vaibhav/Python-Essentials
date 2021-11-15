"""
Program to find out pair of number for given sum, from the array
input: arr=[5,7,3,2,5,8,19,21,23,22,9,1,10,16,12]
sum=17

output:
value of pair are 1 & 16
value of pair are 5 & 12
value of pair are 7 & 10
value of pair are 8 & 9
Press any key to continue . . .

"""

def two_sum(arr,sum):
	arr.sort()
	left= 0
	right = len(arr) -1
	while(left<=right):
		if(arr[left]+arr[right]>sum):
			right=right-1

		elif(arr[left]+arr[right]<sum):
			left=left+1
		elif(arr[left]+arr[right]==sum):
			print("value of pair are",arr[left], "&", arr[right])
			right=right-1
			left=left+1

arr=[5,7,3,2,5,8,19,21,23,22,9,1,10,16,12]
sum=17
two_sum(arr,sum)