# James Jhong
# 10/3/2023
# LC 347 Top K Frequent Elements
# Max Heap approach

# Create a max heap with the counts... and then... remove top node and re_heapify

from heaps import max_heapify
from heaps import build_max_heap
from heaps import pop

def topKFrequent(nums, k):
    count = {}
    result = [0] * k
    # List of the frequencies occuring --> Could be possible using the pairs but I would need to change my implementation of heap to use only blah blah
    for i in nums :
        count[i] = 1 + count.get(i, 0)
        
    keys = count.keys()
    
    freq = [frequency for frequency in count.values()]
    
    build_max_heap(freq)
    
    

def main() :
    k = 2
    nums = [1,1,1,2,2,3]
    topKFrequent(nums, k)
    
main()