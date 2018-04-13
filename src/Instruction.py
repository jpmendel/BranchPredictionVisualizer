from InstructionType import *


class Instruction:

    def __init__(self, instruction):
        self.opcode = (instruction >> 26) & 31
        self.type = self.get_instruction_type()
        self.rs = (instruction >> 21) & 15
        self.rt = (instruction >> 16) & 15
        self.rd = (instruction >> 11) & 15
        self.shamt = (instruction >> 6) & 15
        self.funct = instruction & 31
        self.immediate = instruction & 32767
        self.jump_address = instruction & 33554431

    def get_instruction_type(self):
        return {
            0: InstructionType.R_TYPE,
            2: InstructionType.J_TYPE,
            3: InstructionType.J_TYPE
        }.get(self.opcode, InstructionType.I_TYPE)

    def get_opcode(self):
        return self.opcode

    def get_rs(self):
        if self.type == InstructionType.J_TYPE:
            raise AssertionError('J_TYPE instructions have no rs!')
        return self.rs

    def get_rt(self):
        if self.type == InstructionType.J_TYPE:
            raise AssertionError('J_TYPE instructions have no rt!')
        return self.rt

    def get_rd(self):
        if self.type == InstructionType.I_TYPE:
            raise AssertionError('I_TYPE instructions have no rd!')
        elif self.type == InstructionType.J_TYPE:
            raise AssertionError("J_TYPE instructions have no rd!")
        return self.rd

    def get_shamt(self):
        if self.type == InstructionType.I_TYPE:
            raise AssertionError('I_TYPE instructions have no shamt!')
        elif self.type == InstructionType.J_TYPE:
            raise AssertionError("J_TYPE instructions have no shamt!")
        return self.shamt

    def get_funct(self):
        if self.type == InstructionType.I_TYPE:
            raise AssertionError('I_TYPE instructions have no funct!')
        elif self.type == InstructionType.J_TYPE:
            raise AssertionError("J_TYPE instructions have no funct!")
        return self.funct

    def get_immediate(self):
        if self.type == InstructionType.R_TYPE:
            raise AssertionError('R_TYPE instructions have no immediate!')
        elif self.type == InstructionType.J_TYPE:
            raise AssertionError("J_TYPE instructions have no immediate!")
        return self.immediate

    def get_jump_address(self):
        if self.type == InstructionType.R_TYPE:
            raise AssertionError('R_TYPE instructions have no jump address!')
        elif self.type == InstructionType.I_TYPE:
            raise AssertionError("I_TYPE instructions have no jump address!")
        return self.jump_address

    def __repr__(self):
        return 'Instruction: [opcode: ' + hex(self.opcode) + \
               ', type: ' + self.type.__str__() + \
               ', rs: ' + hex(self.rs) + \
               ', rt: ' + hex(self.rt) + \
               ', rd: ' + hex(self.rd) + \
               ', shamt: ' + hex(self.shamt) + \
               ', funct: ' + hex(self.funct) + \
               ', immediate: ' + hex(self.immediate) + \
               ', jump address: ' + hex(self.jump_address) + ']'
