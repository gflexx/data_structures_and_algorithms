class Node():
    '''
        Node object takes data, 
        previous_node
        and next_node
    '''
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
        
    def __str__(self):
        return ('('+ str(self.data) + ')')

class  CircularLinkedList:
    '''
        This class makes a circular linked
        list. The last node always points
        to the root node. A new node is 
        added next to the root node.
    '''
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        
    # add item to node
    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.root.next_node = self.root
        else:
            new_node = Node(data, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1
       
    # loop through list to find item if root return False
    def find(self, data):
        this_node = self.root
        while True:
            if this_node.data == data:
                return data
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node
            
    # remove item by looping through list checking 
    # if found item is removed else return False
    def remove(self, data):
        this_node = self.root
        prev_node = None
        while True:
            # data found 
            if this_node.data == data:
                # swap nodes while checking for root
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True
            
            # data not found
            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node
        
    # print if not none and go to next node
    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node.next_node is not self.root:
            this_node = this_node.next_node
            print(this_node, end='->')
            
# cll = CircularLinkedList()
# for i in range(8):
#     cll.add(i)
# print(cll.print_list())
# print(cll.find(1))
# print(cll.remove(4))
# print(cll.find(99))
