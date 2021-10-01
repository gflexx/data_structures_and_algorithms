class Node():
    '''
	Node stores data(d) and contains
	next_node and previous_node to create 
	a linked list
    '''
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
        
    def __str__(self):
        return ('('+ str(self.data) + ')')
    
class LinkedList():
    '''
 	contains a root value that holds a node
	the node takes a next node value and data
	size holds the number of values in the
	linked list
    '''
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
        
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None
    
    def print_list(self):
        this_node = self.root
        size = self.size
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
            size -= 1
        if size == 0:
            print(' 0 ')