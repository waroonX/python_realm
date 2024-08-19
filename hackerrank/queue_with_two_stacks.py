"""

link: From Hackerrank grid Challenge
level: intermediate
score: 0


"""

class StackQueue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, val: int):
        if not (self.stack1 or self.stack2):
            self.stack1.append(val)
        else:
            self.stack2.append(val)
            
    def dequeue(self):
        if not self.stack1:
            self.move()
        return self.stack1.pop()
    
    def print_front(self):
        if not self.stack1:
            self.move()
        print(self.stack1[-1])
    
    def move(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
    
if __name__ == "__main__":
    stack_queue = StackQueue()
    
    for _ in range(int(input())):
        command = input()
        if command[0] == "1":
            val = int(command.split()[-1])
            stack_queue.enqueue(val)
        elif command[0] == "2":
            stack_queue.dequeue()
        elif command[0] == "3":
            stack_queue.print_front()