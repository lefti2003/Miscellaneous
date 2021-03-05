# Project 3: 
## Problems vs. Algorithms
### Q1: Square Root Of An Integer
For this question I used the binary search. I only consider positive integers or a number >= 0. If the number entered is negative I throw out an error. If the number is 0 or 1 I return that number. The binary search find the midpoint. If the midpoint**2 is equal to the same number it returns the midpoint. If midpoint**2 is less than the number we search the right have. If the midpoint**2 is greater then then number we search the left half. 
### Time and Space Complexity:
#### Time: 
Since we are dividing in splitting the search in half the time complexity is O(logn).
#### Space:
The space complexity is just storing variables, mid, start and end.


### Q2: Search in a Rotated Array
For this problem the data structure used is an array. Binary search is used. An important step is to find the pivot that is the max element. This identifies the point to split the arrays.
#### Time:
Since it employs binary search the time complexity is O(logn)
#### Space:
Since this is a recursive call it is proportional to the max depth of the generated recursive tree. If the depth of the tree is n and each call takes O(m) then in total the complexity is O(mn)

### Q3: Rearrange Array Elements
For this problem I use the merge sort to first sort the array. From here I pick off the maximum and second maximum value in the array. I then place these into the sum result array and repeat this going through the array. This will ensure I get two numbers whose sums are maximum.

#### Time:
The merge sort requires O(nlogn) worst case time. 

#### Space:
The space complexity is the length of the array which is n. Therefore O(n)

### Q4: Dutch National Flag problem
For this problem I use the merge sort algorithm. 

#### Time:
The merge sort takes in worst case O(nlogn).

#### Space:
The space complexity is O(n)

### Q5: Autocomplete with Tries
The data structure used is a Trie. It has an efficient look up. I use a dictionary to store key = char and value = ptr to Node. 

### Time: 
The time to search for a key is O(N), where N is the length of the string.

### Space:
Space complexity is where a trie takes a hit. It is O(RN) where R is the number of keys and N is the size of the array.

### Q6: Max and Min in an Unsorted Array
The data structure used in this question is an unsorted array and the return is a tuple of min and max.

### Time:
Time complexity is O(n). Both min and max are found in one pass. I use pythons built in sys.maxsize to get an upper bound and -float('inf') to get a lower bound ( Thanks to the reviewer for this).

### Space:
The space complexity is just the size of the array O(n). 








