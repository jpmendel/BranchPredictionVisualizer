from Instruction import *

if __name__ == '__main__':
    with open('data/instructions.txt', 'r') as file:
        instructions = [Instruction(int(x, 16)) for x in file.readlines()]

    print(instructions)