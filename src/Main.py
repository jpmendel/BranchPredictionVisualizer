from Instruction import *

if __name__ == '__main__':
    instructions = []

    with open('instruction.txt', 'r') as file:
        HEX_INSTRUCTIONS = file.readlines()

        for instruction in HEX_INSTRUCTIONS:
            instructions += Instruction(instruction)
