# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Doubly Linked List Implementation: 
class Node: 
    def __init__(self, url: str): 
        self.val = url 
        self.prev, self.next = None, None 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.head

    def insert(self, url: str) -> None: 
        # Create a new node from our URL
        new_page = Node(url) 
        # Connect that node to our existing DLL 
        self.current.next = new_page
        new_page.prev = self.current 
        
        # Move our current node pointer forward 
        self.current = new_page
        # Remove any forward pages from the linked list 
        self.current.next = None 

    def visit(self, url: str) -> None:
        self.insert(url) 

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1 
        return self.current.val
        


# List Implementation: 
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage] 
        self.idx = 0 

    def visit(self, url: str) -> None:
        self.history = self.history[:self.idx + 1] 
        self.history.append(url) 
        self.idx = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.history[self.idx]        

    def forward(self, steps: int) -> str:
        self.idx = min(len(self.history) - 1, self.idx + steps)
        return self.history[self.idx]
