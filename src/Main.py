from InstructionTypeI import *
from InstructionTypeJ import *
from InstructionTypeR import *

if __name__ == '__main__':
    with open('instructions.txt', 'r') as file:
        instructions = []

        for line in file.readlines():
            instruction = int(line, 16)

            # Handle nop and syscall, respectively.
            if instruction == 0 or instruction == 12:
                instructions.append(Instruction(instruction))
                continue

            opcode = (instruction >> 26) & 63

            if opcode == 0:
                instructions.append(InstructionTypeR(instruction))
            elif opcode == 2 or opcode == 3:
                instructions.append(InstructionTypeJ(instruction))
            else:
                instructions.append(InstructionTypeI(instruction))

    Processor().process(instructions)
