class Stack:
  def __init__(self):
    self.stack = []

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    if (not len(self.stack)):
      print('stack is empty')
    else:
      self.stack.pop()

  def peek(self):
    return self.stack[-1]

  def list(self):
    return self.stack

s = Stack()

print(s.push(1),
s.push(2),
s.push(3),
s.pop(),
s.peek(),
s.list())