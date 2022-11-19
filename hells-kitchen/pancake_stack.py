'''
This is an interpreter for the Pancake Stack esolang. To use it, pass a file containing a valid Pancake Stack program as the first command line argument.

Source: https://ideone.com/7sFFo0
'''
import re
import sys
 
def push(match):
    global stack
    stack.append(len(match.group(1)))
def eat():
    global stack
    stack.pop()
def combine_pancakes():
    global stack
    a, b = stack.pop(), stack.pop()
    stack.append(a + b)
def give_pancake():
    global stack
    stack.append(int(input()))
def give_hotcake():
    global stack
    stack.append(ord(sys.stdin.read(1)))
def show_pancake():
    global stack
    print(chr(stack[-1]), end='')
def take_from_pancakes():
    global stack
    a, b = stack.pop(), stack.pop()
    stack.append(a - b)
def flip_pancakes():
    global stack
    stack[-1], stack[-2] = stack[-2], stack[-1]
def put_another_pancake():
    global stack
    stack.append(stack[-1])
def label(match):
    global labels
    global stack
    label = match.group(1)
    if label in labels:
        return
    labels[label] = stack[-1] - 1
def not_tasty(match):
    global labels
    global stack
    global line
    if not stack[-1]:
        line = labels[match.group(1)]
def is_tasty():
    global labels
    global stack
    global line
    if stack[-1]:
        line = labels[match.group(1)]
def put_syrup():
    global stack
    for i in range(len(stack)): stack[i] += 1
def put_butter():
    global stack
    stack[-1] += 1
def remove_syrup():
    global stack
    for i in range(len(stack)): stack[i] -= 1
def remove_butter():
    global stack
    stack[-1] -= 1
def eat_all():
    global stack
    sys.exit(0)
 
program = []

# load program from first command line argument
try:
    file = sys.argv[1]
    with open(file, "r") as f:
        program = f.readlines()
except:
    print("ERROR: Failed to load program file", file=sys.stderr)
    exit()
 
commands = {
    r'Put this ([^ ]*?) pancake on top!': push,
    r'Eat the pancake on top!': eat,
    r'Put the top pancakes together!': combine_pancakes,
    r'Give me a pancake!': give_pancake,
    r'How about a hotcake?': give_hotcake,
    r'Show me a pancake!': show_pancake,
    r'Take from the top pancakes!': take_from_pancakes,
    r'Flip the pancakes on top!': flip_pancakes,
    r'Put another pancake on top!': put_another_pancake,
    r'\[(.*)\]': label,
    r'If the pancake isn\'t tasty, go over to "(.*)".': not_tasty,
    r'If the pancake is tasty, go over to "(.*)".': is_tasty,
    r'Put syrup on the pancakes!': put_syrup,
    r'Put butter on the pancakes': put_butter,
    r'Take off the syrup!': remove_syrup,
    r'Take off the butter!': remove_butter,
    r'Eat all of the pancakes!': eat_all
}
labels = dict()
line = 0
stack = []
while program[line] != 'Eat all of the pancakes!':
    #print("%i:%s:%s"%(line,program[line],stack)) #for debug purposes
    for command in commands.keys():
        match = re.match(command, program[line])
        if match:
            try: commands[command](match)
            except TypeError: commands[command]()
            break
    else:
        print('Line %i is not a valid command'%line, file=sys.stderr)
        sys.exit(1)
    line += 1