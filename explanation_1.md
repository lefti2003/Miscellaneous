# Project 2: 
## Show Me The Data Structures
### Q1: LRU
For this question I used an Ordered Dictionary. In this way a set operation moves the key, value pair to the end of the dictionary and keeps track of this. The get operation will find the value for the given key and will then place the key, value pair at the end of the dictionary.
### Time and Space Complexity:
#### Time: 
The OrderedDictionary is composed of an array and a HashTable. Each lookup or get operation requires O(1) for the array and O(1) for the HashTable. Thus for the Ordered Dictionary it takes O(1) for the get/set operation. 
#### Space:
The space complexity is O(capacity), where the capacity is the size of the ordered dictionary. In my example it was O(5).


Reference article: https://www.codeproject.com/Articles/18615/OrderedDictionary-T-A-generic-implementation-of-IO

### Q2: File Recursion
For this problem I used the two python modules os, sys. The data structure used was a list. 
#### Time:
Since a for loop was used this requires O(n) and was applied recursively. In addition since an append method was used to add the found files to our list this requires O(1).
#### Space:
Since a list was used Space complexity is O(size) of files list. The more files found the more space required.

### Q3: Huffman Coding
For this problem there are essentially three dictionaries and a list. The three dictionaries store the frequency (freq) of letters used in the text, codes which is storing the 01 binary codes and the reverse_mapping which is storing the letters of the corresponding texts. The reverse_mapping dictionary will make it easier for the decoding step. Pythons heapq is also used to store the Key=letter and the frequency of that letter. Operations such as push and pop can be used 

#### Time:
Each push/pop using the heapq takes O(logn) however there is a while loop and there are n such elements therefore time is O(nlogn) worst case.

#### Space:
As indicated above there are three dictionaries, therefore storage is O(size), where size is of the dictionaries that store the codes.

### Q4: Windows Active Directory
For this problem two lists are used as data structures. Adding a user/group is a simple operation. 

#### Time:
Adding a user/group is O(n). Getting a user/group since it has to check the list of groups and then to see if that user is in that group which is done recursively will take O(n)

#### Space:
It is the size of the user/groups list O(size).

### Q5: Block Chain
The data structure used for this question is a list called MyBlockChain. It uses the python library hashlib. 

### Time: 
Here we are adding things to a list. This is done in O(n)

### Space:
Since it is a list the space is the size of the list thus O(size).

### Q6: Union and Intersection
Here we are passing two linked lists and calculating the union and intersection of these two lists. The union and intersection thus are linked lists in themselves. 

### Time:
For the union you have to traverse the two linked lists and then remove the duplicates. Worst case is O(n)
In the intersection you have two keep track of the two lists in two while loops thus this requires O(n^2)

### Space:
The union of two lists is at most O(2*size) or just O(double) since we do not care about constants we just say O(size), where size is the size of the linked list.
In intersection the largest size is at most the size of the smaller list, thus its space complexity is O(size)







