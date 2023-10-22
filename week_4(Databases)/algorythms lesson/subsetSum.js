// SUBSET SUM
//
// Given a list of numbers and a target, write a function to determine if the target can be calculated by summing together any 2 numbers in the list.
// 1) The function should return True if the target can be calculated and False if not.
// 2) For ease of analysis and to see whats going on, we will also print True and the 2 numbers, or False.
// Notes:
// – The list is of arbitrary length.
// – The list is unsorted.
// – The list may contain both positive and negative integers.
// – There may be duplicated numbers.
nums = [12, -7, 20, 1, 4, -10, -1]





subsetsum(nums, 1) // False
subsetsum(nums, 2) // True: 12,  -10
subsetsum(nums, 3) // True: 4,  -1
subsetsum(nums, 4) // False
// Example:
// nums = [12, -7, 20, 1, 4, -10, -1]

// subsetsum(nums, 1) # False
// subsetsum(nums, 2) # True: 12,  -10
// subsetsum(nums, 3) # True: 4,  -1
// subsetsum(nums, 4) # False