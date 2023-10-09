# James Jhong
# 10/7/2023
# Insertion sort


# Insertion sort happens in place
# Uses a key to look at specific index and does continuous pairwise swaps down
def insertion_sort(nums) :
 
    for i in range(len(nums) - 1) : # Right up until the last
        key = i + 1
        prev = key - 1
        while nums[key] < nums[prev] and prev >= 0: # If 5 is greater than 2
            nums[key], nums[prev] = nums[prev], nums[key] # Swapped a pair
            key -= 1
            prev -= 1
        print("Nums status at iter ", i, ": ", nums)
    
# def b_insertion_sort(nums) :

    
def main() :
    nums = [5, 2, 4, 6, 1, 8, 7]   
    insertion_sort(nums)
    print("Result of insertion sort: ", nums)

main()