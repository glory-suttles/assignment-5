# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    return max(frequency, key = frequency.get)

numbers_example = [1,3,2,3,4,1,3]
print(most_frequent(numbers_example))

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) only goes through the data once and has low amount of data, there is only one maximum value
- Worst-case: O(n) the data could be long without repetention increasing the time and there would multiple answers depending on the 
amount of numbers implemented since there are no duplicates. 
- Average-case:O(n) there are multiple maximum values and the data size is larger (not necesarily small or long just more data than the example given)
- Space complexity: O(n), it increases linearly which allows for there to be as much data needed as possible. It only requires the data to be put  
into a dictionary once therefore the amount of lists is limited to one. 
- Why this approach? This is the best possible approach because the data can increase which O(n) accounts for 
- Could it be optimized? Based on the Big O Notations and examples, this data could not be optimized to the knowledge that I have. The code itself  
is shorter and is as time and storage efficient as possible. 
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    duplicates = set()
    result = []
    for numbers in nums:
        if numbers not in duplicates:
            result.append(numbers)
            duplicates.add(numbers)
    print(result)

nums = [4,5,4,6,5,7]
remove_duplicates(nums)
"""
Time and Space Analysis for problem 2:
- Best-case: O(n) There is only one set of duplicate, resulting in a small output and less memory being stored
- Worst-case:O(n) There are no duplicates and the amount of memory being stored equal the amount of inputs in the data. The amount of data 
stored would increase the memory which does not work the best with O(n)
- Average-case:O(n) There are a few duplicates and the data is on the longer side but the memory does is not stretched to a lengthy amount. 
- Space complexity: The amount of data that can be implemented is infinite which there expands the memory of the data. The time in which it takes
to analyze the code and give results is all dependent on the amount of data inputed. The time and memory may lengthen overtime but the does
not diminish the code itself.
- Why this approach? I chose this approach because it goes through the data only one time which is that is needed to decide the amount and what 
the duplicates are. By having both a set and list, they work together to get rid of the duplicates but also keep the data in order. A seperate
clean dictionary is created through the list and add function. This is most efficient and applicable direction for the code based on what I've 
learned. 
- Could it be optimized? To my knowledge I do not believe that this could be optimized. It creates both a set and list per the instructions but 
if a list was not needed that could shorten the code. However, based on the instructions this is a vital step. The list also keeps a seperate 
clean result for the data give. O(n) allows the data to only be gone through once but the amount of data is not limited. 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return list(pairs)


nums = [1,2,3,4]
target = 5
print(find_pairs(nums,target))


"""
Time and Space Analysis for problem 3:
- Best-case:O(n) The data is small and all pairs can be arranged to add up to the target set. 
- Worst-case:O(n2) The data is larger and there are some pairs that do not add up to the selected target. There are multiple sets due to the wide
range of numbers. The data is looped through twice because of the Big O operation being used. 
- Average-case:O(n) There is a decent amount of data given and most all of the numbers can be paired up to meet the needs to the target sum. 
- Space complexity: Uses a set in order to check set compatability and complements. It also only stores the resulting pairs. There is only a single
loop to analyze the code. 
- Why this approach? This code is the most efficient when it comes to both time and space complexity. The data is only gone through once and 
the sets create a simple system of pairing the complement numbers that add up to the target. 
- Could it be optimized? This could not be optimized in my opinion because it is the fastest approach of only going through the data once. While 
there could another way of using O(n2) that would be a slower concept and would slow down the code the larger the data got. The O(n2) process requires
the data to be gone through twice in order for the pairs to be made. 
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    items = []

    for i in range(n):
        if size == capacity:
            print(f"Resizing: capacity {capacity} → {capacity * 2}")
            capacity *= 2
        items.append(i)
        size += 1
        print(f"Added {i}: size={size}, capacity={capacity}")

    return items


add_n_items(6)

    

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When an array runs out of space then resizes have to occur so in the case of this code when the capacity is multiplied
by 2 and the size increases by one its resized. The append function ensures adds more to the memory. 
- What is the worst-case for a single append? O(n) this is more costly and has to allocate all of the memory, copy all of the data already in 
the memory and then it can add new data. It's a longer process than O(1).
- What is the amortized time per append overall? O(1) is the amortized timed per append. 
- Space complexity: O(n) it can hold more data even if there is a limit which is linear.  
- Why does doubling reduce the cost overall? It is quicker and increases the rarity of resizes. With the appends it keeps the amortized cost constant. 
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    current_sum = 0
    for num in nums:
        current_sum += num
        totals.append(current_sum)
    return totals

nums = [1,2,3,4]
result = running_total(nums)
print(result)

"""
def running_total(nums):
    if not nums:
        return []
    rest = running_total(nums[:-1])
    last_sum = (rest[-1] if rest else 0) + nums[-1]
    return rest + [last_sum]
- This was optimized with the use of O(n2) which can be fast for smaller sets since the input size doesn't really impact the performace.
 It can use less of the memory and have less overhead of extra data structures. 

"""
"""Time and Space Analysis for problem 5:
- Best-case:O(n) There is a small amount of data with easy operations occuring.
- Worst-case:O(n2) would have to be used because O(n) would not be able to process the data due to the large volume of data that could be presented.
O(n2) would slow the process down as it would have to go through a loop of the data twice in order to achieve the correct results. 
- Average-case:O(n2) The amount of data presented is relatively large which requires the O(n2) to be used slowing the process down. 
- Space complexity:O(n2) This operation would be able to handle the size of the data as O(n) would not be capable of doing so in a correct manner. 
- Why this approach? I chose this approach becuse it only requires the code to go through the data once. The set collects the data into one place and 
is only asking for a small amount of data. There is a constant addition and append action taking place to have efficient results. 
- Could it be optimized? This could be optimized depending on the size if an O(n2) operation was used because O(n2) requires the data to be 
looped through twice where O(n) only goes through it once. However, if it was large then O(n) could not be applied. 
"""
