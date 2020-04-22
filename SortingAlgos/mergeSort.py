def merge(arr,p,q,r):
	#Create two arrays namely Left and Right
	left_elements=arr[p:q+1]
	right_elments=arr[q+1:r+1]
	#K is pointer for arr
	k=p
	#i is pointer for left elements
	i=0
	#j is pointer for right elements
	j=0
	while(i<len(left_elements) and j<len(right_elments)):
		if(left_elements[i]>right_elments[j]):
			arr[k]=right_elments[j]
			j+=1
		else:
			arr[k]=left_elements[i]
			i+=1
		k+=1

	while(i<len(left_elements)):
		arr[k]=left_elements[i]
		i+=1
		k+=1

	while(j<len(right_elments)):
		arr[k]=right_elments[j]
		j+=1
		k+=1

def mergeSort(arr,p,r):
	if(p<r):
		mid=int((p+r-1)/2)
		mergeSort(arr,p,mid)
		mergeSort(arr,mid+1,r)
		merge(arr,p,mid,r)

if __name__=='__main__':
	arr=[10,9,8,7,6,5,4,3,2,1]
	mergeSort(arr,0,len(arr))
	print("Sorted Array using merge sort is ",arr)