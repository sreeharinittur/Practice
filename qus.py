class Queue:
    def __init__(self):
        self.stack=[]
    def enqueue(self,x):
        self.stack.append(x)
    def dequeue(self):
        i=self.stack.remove(self.stack[0])
    def display(self):
        print(self.stack)
q=Queue()
q.enqueue(5)
q.enqueue(4)
q.enqueue(6)
q.display()
q.dequeue()
q.dequeue()
q.display()