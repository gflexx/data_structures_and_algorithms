from collections import deque

class Queue():
    ''' 
	Implementing a Queue using python's double ended queue
    '''
    def __init__(self):
        self.queue = deque()
        
    def push(self, item):
        self.queue.append(item)
        
    def push_to_first(self, item):
        self.queue.appendleft(item)
        
    def pop_first(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
        
    def pop_last(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return None
        
    def length(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)