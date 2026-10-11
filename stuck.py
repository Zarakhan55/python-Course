# stuck=[]
# stuck.append("Hello")
# stuck.append("World")
# stuck.append("!")
# print(stuck)
# remove=stuck.pop(1)
# print(stuck)


# stack = ["Google", "YouTube", "GitHub"]
# stack.append("LinkedIn")
# print(stack)
# print(stack.pop(1))








# actions = []

# actions.append("Write HTML")
# actions.append("Add CSS")
# actions.append("Add JavaScript")

# print("Actions:", actions)

# last_action = actions.pop()

# print("Undo:", last_action)
# print("Remaining:", actions)






class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            return self.items[-1]


# Create a stack
my_stack = Stack()

my_stack.push("HTML")
my_stack.push("CSS")
my_stack.push("JavaScript")

print("Top item:", my_stack.peek())
print("Removed:", my_stack.pop())
print("New top:", my_stack.peek())
