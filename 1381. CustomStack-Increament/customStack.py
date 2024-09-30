class CustomStack(object):
    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.customStack = []  # This will be the stack to store elements
        self.head = -1  # Initialize head as -1 to indicate an empty stack
        self.maxSize = maxSize  # Set the max size of the stack
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.head < self.maxSize - 1:  # Check if there is space to add an element
            self.head += 1
            self.customStack.insert(self.head, x)

    def pop(self):
        """
        :rtype: int
        """
        if self.head == -1:  # If head is -1, the stack is empty
            return -1
        element = self.customStack.pop(self.head)  # Remove and return the top element
        self.head -= 1
        return element

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        limit = min(k, self.head + 1)  # Determine the range for incrementing
        for i in range(limit):
            self.customStack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k, val)


