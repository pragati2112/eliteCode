def insertInAMaxHeap(arr, num)
	i = lens(arr)+1
	arr[i] = num
	while i>1:
		parent = i//2
		if arr[parent]<arr[i]:
			arr[parent], arr[i] = arr[i], arr[parent]
			i=parent
		else:
			return	

# heap is a tree data structure
# max heap ----largest elements are on top
# min heap----minimum elemets are on top

# when array starts with 1 index--
# left child index = 2i
# right child index = 2i+1
# parent index = i//2

# when array starts with 0 index--
# left child index = 2i+1
# right child index = 2i+2
# parent index = (i//2)-1
# last node = (n/2)-1


def deleteFromAMaxHeap(arr, idx):
	n = len(arr)
	arr[n], arr[idx] = arr[idx], arr[n]

	while i<n:
		left_c = 2*i
		right_c = 2*i+1

		if arr[left_c]>arr[right_c]:
			largest_idx = 2*i

		if arr[left_c]<arr[right_c]:
			largest_idx = 2*i+1

		if arr[i]<arr[largest_idx]:
			arr[i], arr[largest] = arr[largest], arr[i]
			i = largest_idx
		else:
			return			




# Max-Heap data structure in Python
# Start from the first index of non-leaf node whose index is given by size/2 - 1


def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2 
    
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child
    
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)



def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    
    # swap last element with the element to be deleted
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)


        
    
arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))