# James Jhong
# 10/2/2023
# Max Heap

''' A heap is a complete binary tree where every row is complete except the very last one '''



# MHP : Max heap value of i <= value of parent (TOP IS BIGGEST)
# Min heap value of i => value of parent

# Root is set to 1, not zero for easier calculations
# Left(i) = 2 * i
# Right(i) = 2 * i + 1
# Parent(i) = floor(i/2)

# Max heapify assumes that branches below node i are already HEAPS !
# Max heapify takes 3 inputs
# An array(a), size of heap n, and index i (for the node it is on)

def max_heapify(a, n, i) :
    # Retrieve the left and right child 
    left = 2*i
    right = 2*i + 1
    
    largest = i
    
    # Comparing to verify heap property
    if left < n and a[left] > a[i] :
        largest = left
    if right < n and a[right] > a[largest] :
        largest = right
        
    # Swapping in case of violations of the heap property
    if largest != i :
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)
        
    # A main function that calls max_heapify
    
    # Leaves are heaps technically so we start build max heap at the leaf, working our way up to the root
    
def build_max_heap(a) :
    heap_size = len(a)
    
    for i in range(heap_size//2, 0, -1):
        max_heapify(a, heap_size,i)
        
def main():
    # root is at index 1
    # it can be at index zero but see here: https://www.quora.com/Why-do-indexes-for-heaps-start-at-1
    # and: https://stackoverflow.com/questions/22900388/why-in-a-heap-implemented-by-array-the-index-0-is-left-unused

    a = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    build_max_heap(a)

    # print heap starting with the root at index 1
    print(f'Heap: {a[1:]}')


main()