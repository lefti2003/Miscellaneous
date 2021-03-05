# Blockchain uses a linked list
# see https://medium.com/@vishnuashok123/building-a-simple-blockchain-using-python-90d27ee50214


import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):

        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):

        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):

        hash_str = str(self.timestamp) + str(" | ") + \
                   str(" | ") + str(self.previous_hash) + \
                   str(" | ") + str(self.hash)

        return hash_str


class BlockChain(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append_block(self, data):

        if data is None or data == "":
            return
        elif self.head is None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            self.tail = self.head
        else:
            self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.hash)
            self.tail = self.tail.next
        return

    def tolist(self):
        out = []
        block = self.head

        while block:
            out.append([block])
            block = block.next
        return out


def main():

    # Test 1
    b1 = BlockChain()
    for i in range(3):
        b1.append_block("Block " + str(i+1))

    bl1 = b1.tolist()
    # prints block chain
    for block in bl1:
        print(block)

    # Test 2
    b2 = BlockChain()
    for i in range(2):
        b2.append_block("")

    bl2 = b2.tolist()
    # prints empty block chain as there was no data passed

    for block2 in bl2:
        print(block2)

    # Test 3
    b3 = BlockChain()
    for i in range(2):
        b3.append_block(None)

    bl3 = b3.tolist()
    # prints empty block chain as there was no data passed

    for block3 in bl3:
        print(block3)


if __name__ == "__main__":

    main()