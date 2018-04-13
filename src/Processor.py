from Instruction import *
from InstructionTypeR import *

REGISTERS = [0] * 32

NAME_FROM_REGISTER = [
    'zero', 'at', 'v0', 'v1', 'a0', 'a1', 'a2', 'a3',
    't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7',
    's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7',
    't8', 't9', 'k0', 'k1', 'gp', 'sp', 's8', 'ra'
]


class Processor:
    def __init__(self):
        pass

    def process(self, instructions):
        for instruction in instructions:
            if instruction.is_nop() or instruction.is_syscall():
                continue

            if instruction.get_opcode() == 0x00:
                name = NAME_FROM_FUNCT[instruction.get_funct()]

                if name == 'add':
                    REGISTERS[instruction.get_rd()] = REGISTERS[instruction.get_rs()] + REGISTERS[instruction.get_rt()]
            else:
                name = NAME_FROM_OPCODE[instruction.get_opcode()]

                if name == 'addi' or name == 'addiu':
                    REGISTERS[instruction.get_rt()] = REGISTERS[instruction.get_rs()] + instruction.get_immediate()

            print(instruction)
            print(REGISTERS)
