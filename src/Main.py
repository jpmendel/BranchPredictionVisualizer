from data.instruction_r import InstructionR
from data.instruction_i import InstructionI
from data.instruction_j import InstructionJ
from data.instruction import Instruction
from data.processor import Processor

import os


SRC_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    with open(os.path.join(SRC_DIR, '..' + os.sep + 'files' + os.sep + 'instructions.txt'), 'r') as file:
        instructions = []

        for line in file.readlines():
            instruction = int(line, 16)

            # Handle nop and syscall, respectively.
            if instruction == 0 or instruction == 12:
                instructions.append(Instruction(instruction))
                continue

            opcode = (instruction >> 26) & 63

            if opcode == 0:
                instructions.append(InstructionR(instruction))
            elif opcode == 2 or opcode == 3:
                instructions.append(InstructionJ(instruction))
            else:
                instructions.append(InstructionI(instruction))

    Processor().process(instructions)
