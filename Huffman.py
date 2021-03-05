import os
import heapq
import sys


class HuffmanCoding:

    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if other is None:
                return False
            if not isinstance(other, HeapNode):
                return False
            return self.freq == other.freq

    def make_frequency_dict(self, text):
        # Step 1.
        # Create a dictionary frequency, of key=char, value= (number of times
        # letter is used in the text)
        frequency = {}
        for char in text:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1

        return frequency

    def make_heap(self, frequency):
        # Step 2 Creating a priority queue
        # Python Heapq allows to have a minq in which min elements (frequencies)
        # are popped
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_codes(self):
        # Step 3/4
        # 3. pop out 2 nodes with min frequency heapq.heapop method will do this
        # 4. Create a new node with sum of node1 + node2
        # Reinserting merged node back into priority queue using min heap
        if len(self.heap) > 1:
            while len(self.heap) > 1:
                node1 = heapq.heappop(self.heap)
                node2 = heapq.heappop(self.heap)
                sum_freq = node1.freq + node2.freq
                merged = self.HeapNode(None, sum_freq)
                merged.left = node1
                merged.right = node2
                heapq.heappush(self.heap, merged)
        elif len(self.heap) == 1:
            node1 = heapq.heappop(self.heap)
            sum_freq = node1.freq + 0
            merged = self.HeapNode(None, sum_freq)
            merged.left = node1
            heapq.heappush(self.heap, merged)


    def make_codes_helper(self, node, current_code):
        # Steps 5/6
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char

        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")

    def make_codes(self):
        # Step 5/6
        # assign 0 = left child, 1 = right child
        root_node = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root_node, current_code)

    def get_encoded_text(self, text):
        # Ste 7 generate unique binary code for each
        # char of string
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        #    print(encoded_text)

        return encoded_text

    def huffman_encoding(self, text):
        # Step 1
        if text != " ":
            frequency = self.make_frequency_dict(text)
            # Step 2
            self.make_heap(frequency)
            # Step 3/4
            self.merge_codes()
            # Step 5/6
            heap_root = self.make_codes()
            # Step 7
            encoded_text = self.get_encoded_text(text)
            print("Encoded")
            return encoded_text
        else:
            print(" This is an empty string!")
            return " "

    def huffman_decoding(self, data):
        bit_string = ""
        current_code = ""
        decoded_text = ""

        for bit in data:
            current_code += bit
            if current_code in self.reverse_mapping:
                char = self.reverse_mapping[current_code]
                decoded_text += char
                current_code = ""

        print("Decoded")

        return decoded_text


if __name__ == "__main__":

    HC1 = HuffmanCoding('./')

    # Test 1
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = HC1.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = HC1.huffman_decoding(encoded_data)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # The size of the data is: 69
    # The content of the data is: The bird is the word
    # Encoded
    # The size of the encoded data is: 36
    # The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001
    # Decoded
    # The size of the decoded data is: 69
    # The content of the encoded data is: The bird is the word
    #


    # Test 2
    HC2 = HuffmanCoding('./')
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = HC2.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = HC2.huffman_decoding(encoded_data)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The size of the data is: 74
    # The content of the data is: AAAAAAABBBCCCCCCCDDEEEEEE
    # Encoded
    # The size of the encoded data is: 32
    # The content of the encoded data is: 1010101010101000100100111111111111111000000010101010101
    # Decoded
    # The size of the decoded data is: 74
    # The content of the encoded data is: AAAAAAABBBCCCCCCCDDEEEEEE
    #

    # Test 3
    HC3 = HuffmanCoding('./')
    a_great_sentence = " "

    encoded_data = HC3.huffman_encoding(a_great_sentence)


    # This is an empty string!

    # Test 4
    HC4 = HuffmanCoding('./')
    a_great_sentence = "#!Hello this i- a Cipher"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = HC4.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = HC4.huffman_decoding(encoded_data)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # The size of the data is: 73
    #
    # The content of the data is: #!Hello this i- a Cipher
    #
    # Encoded
    # The size of the encoded data is: 40
    #
    # The content of the encoded data is: 111001111111101100110101010101101100011010011001011001111110110101111100000011000101010011000
    #
    # Decoded
    # The size of the decoded data is: 73
    #
    # The content of the encoded data is: #!Hello this i- a Cipher

    # Test 5
    HC5 = HuffmanCoding('./')
    a_great_sentence = "aaaaaaaaaaaa"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = HC5.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = HC5.huffman_decoding(encoded_data)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

# The size of the encoded data is: 24
#
# The content of the encoded data is: 000000000000
#
# Decoded
# The size of the decoded data is: 61
#
# The content of the encoded data is: aaaaaaaaaaaa
