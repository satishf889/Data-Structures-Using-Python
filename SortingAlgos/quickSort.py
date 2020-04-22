#Getting the key for sorted element
def partiton(arr,start,end):
	#pivot Used for getting pivot element
	pivot=arr[end]
	#i is Pointer for keeping count of changed elements
	i=start-1
	for j in range(start,end):
		if(arr[j]<=pivot):
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
	arr[end],arr[i+1]=arr[i+1],pivot
	return i+1

def quickSort(arr,start,end):
	if(start<end):
		q=partiton(arr,start,end)
		quickSort(arr,start,q-1)
		quickSort(arr,q+1,end)

if __name__=="__main__":
	arr=[121,33,343,99,98,1,45,100]
	quickSort(arr,0,len(arr)-1)
	print("Sorted array using quick sort is ",arr)