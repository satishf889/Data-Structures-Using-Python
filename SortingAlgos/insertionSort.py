def insertionSort(arr):
	if(len(arr)==0):
		return "No element to sort"
	if(len(arr)==1):
		return arr
	for j in range(1,len(arr)):
		current_element=arr[j]
		i=j-1
		while(i>=0 and arr[i]>current_element):
			arr[i+1]=arr[i]
			i=i-1

		arr[i+1]=current_element
	return arr

if __name__=='__main__':
	arr=[]
	print("Sorted array is ",insertionSort(arr))