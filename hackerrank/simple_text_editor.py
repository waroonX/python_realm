"""

link: https://www.hackerrank.com/challenges/simple-text-editor/problem
level: Medium
score: 65

"""

class TextEditor:
    def __init__(self) -> None:
        self.s = ""
        self.prev = []
        
    def append(self, W: str):
        self.prev.append(self.s)
        self.s += W
        
    def delete(self, k: int):
        self.prev.append(self.s)
        self.s = self.s[:-k]
        
    def print(self, k: int):
        print(self.s[k-1])
    
    def undo(self):
        if self.prev:
            self.s = self.prev.pop()
        else:
            self.s = ""

if __name__ == "__main__":
    text_editor = TextEditor()
    for _ in range(int(input())):
        command = input().split()
        if command[0] == "1":
            text_editor.append(command[1])
        elif command[0] == "2":
            text_editor.delete(int(command[1]))
        elif command[0] == "3":
            text_editor.print(int(command[1]))
        elif command[0] == "4":
            text_editor.undo()