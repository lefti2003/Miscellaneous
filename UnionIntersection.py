# UninonIntersection:
# Takes two lists returns the
# a) The union of the lists with no repeats
# b) The Intersection of the lists, i.e, only elements that are common between
# two lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        if cur_head is not None:
            while cur_head:
                out_string += str(cur_head.value) + " -> "
                cur_head = cur_head.next

            return out_string
        else:
            return "The set is empty"

    def get_prev_node(self, ref_node):
        current = self.head

        while current and current.next != ref_node:
            current = current.next

        return current

    def duplicate(self):

        copy = LinkedList()
        current = self.head
        while current:
            copy.append(current.value)
            current = current.next

        return copy

    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next

        else:
            prev_node.next = node.next

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        value = current1.value
        while current2:
            temp = current2
            current2 = current2.next
            if temp.value == value:
                llist.remove(temp)

        current1 = current1.next


def union(llist_1, llist_2):

    if llist_1.head is None:
        un = llist_2.duplicate()
        remove_duplicates(un)
        return un
    if llist_2.head is None:
        un = llist_1.duplicate()
        remove_duplicates(un)
        return un

    un = llist_1.duplicate()
    last_node = un.head
    while last_node.next is not None:
        last_node = last_node.next
    l2 = llist_2.duplicate()
    last_node.next = l2.head
    remove_duplicates(un)

    return un


def intersection(llist_1, llist_2):
    # Your Solution Here

    z = LinkedList()
    if llist_1.head is None:
        return z

    if llist_2.head is None:
        return z

    l1_node = llist_1.head
    l2_node = llist_2.head

    while l1_node is not None:
        l2_node = llist_2.head
        while l2_node is not None:
            if l2_node.value == l1_node.value:
                z.append(l2_node.value)
                break
            l2_node = l2_node.next
        l1_node = l1_node.next

    remove_duplicates(z)

    return z

# Test case 1


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()


element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]


for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test1")
print(f"The union of two linked lists of lists,\n \
l1 = {element_1} and \n l2 = {element_2}:")
print(union(linked_list_1, linked_list_2))

print("-"*72)
print(f"The intersection of two linked lists of lists,\n \
l1 = {element_1} and \n l2 = {element_2}:")
print(intersection(linked_list_1, linked_list_2))

# Test1
# The union of two linked lists of lists,
#  l1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21] and
#  l2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]:
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
# ------------------------------------------------------------------------
# The intersection of two linked lists of lists,
#  l1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21] and
#  l2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]:
# 4 -> 6 -> 21 ->
#



# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Test2")
print(f"The union of two linked lists of lists,\n \
l1 = {element_1} and \n l2 = {element_2}:")
print(union(linked_list_3, linked_list_4))

print("-"*72)
print(f"The intersection of two linked lists of lists,\n \
l1 = {element_1} and \n l2 = {element_2}:")
print(intersection(linked_list_3, linked_list_4))
# Test2
# The union of two linked lists of lists,
#  l1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23] and
#  l2 = [1, 7, 8, 9, 11, 21, 1]:
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
# ------------------------------------------------------------------------
# The intersection of two linked lists of lists,
#  l1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23] and
#  l2 = [1, 7, 8, 9, 11, 21, 1]:
# The set is empty
#
#

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3, 1, 4]
element_2 = [1, 7, 8]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("Test3")
print(f"The union of two linked lists of lists,\n \
l1 = {element_1} and \n l2 = {element_2}:")
print(union(linked_list_5, linked_list_6))

print("-"*72)
print(f"The intersection of two linked lists of lists,\n \
l1 = {element_1} and \n l2 = {element_2}:")
print(intersection(linked_list_5, linked_list_6))

# Test3
# The union of two linked lists of lists,
#  l1 = [3, 1, 4] and
#  l2 = [1, 7, 8]:
# 3 -> 1 -> 4 -> 7 -> 8 ->
# ------------------------------------------------------------------------
# The intersection of two linked lists of lists,
#  l1 = [3, 1, 4] and
#  l2 = [1, 7, 8]:
# 1 ->
#

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [1, 7, 8]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("Test4")
print(f"The union of two linked lists of lists,\n \
l1 = {element_1} and \n l2 = {element_2}:")
print(union(linked_list_7, linked_list_8))

print("-"*72)
print(f"The intersection of two linked lists of lists,\n \
l1 = {element_1} and \n l2 = {element_2}:")
print(intersection(linked_list_7, linked_list_8))

# Test4
# The union of two linked lists of lists,
#  l1 = [] and
#  l2 = [1, 7, 8]:
# 1 -> 7 -> 8 ->
# ------------------------------------------------------------------------
# The intersection of two linked lists of lists,
#  l1 = [] and
#  l2 = [1, 7, 8]:
# The set is empty
#


