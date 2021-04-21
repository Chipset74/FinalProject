import random

state = {}
def rnd():
    random.setstate((3,tuple(state),None)) #sets the state to itself
    for states in range(len(state)):
        if states == len(state)-1: break
        choice = random.randint(0,1)
        if choice == 1: state[states]=state[states]+random.randint(0,10)
        elif choice == 0: state[states]=state[states]-random.randint(0,10)
    random.setstate((3,tuple(state),None))
    return random.randint(0,10)

for x in range(10):
    print(state)
    print(rnd())