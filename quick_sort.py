def partition(nums, start, end):
    i = start - 1 # Less
    j = start # Greater 
    
    pivot = end # It was ending one step early
    
    # We are checking to see if j is lesser than pivot
    # If so then we increment up
    
    # If j is less than pivot, i increments and then 
    # the values at i and j swap
    j = start
    
    while j <= end :
        if nums[j] < nums[pivot] :
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
        j += 1
    # I stops at the last lowest place of pivot... so pivot should rest at 1 next
    i += 1 
    nums[pivot], nums[i] = nums[i], nums[pivot] # Value at pivot
  
    return i

def quick_sort(nums, start, end) :
    if end <= start :
        return
    
    pivot = partition(nums, start, end)
    quick_sort(nums, start, pivot - 1)
    quick_sort(nums, pivot + 1, end)
        

def main() :
    nums = [8, 2, 4, 7, 1, 3, 9, 6, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
    
main()