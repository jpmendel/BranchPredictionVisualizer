class Instruction(object):
    def __init__(self, instruction):
        self.instruction = instruction
        self.opcode = (instruction >> 26) & 63
        self.rs = (instruction >> 21) & 31
        self.rt = (instruction >> 16) & 31
        self.rd = (instruction >> 11) & 31
        self.shamt = (instruction >> 6) & 31
        self.funct = instruction & 63
        self.immediate = instruction & 65535
        self.jump_address = instruction & 67108863

    def get_opcode(self):
        return self.opcode

    def is_nop(self):
        return self.instruction == 0

    def is_syscall(self):
        return self.instruction == 12

    def __repr__(self):
        if self.instruction == 0:
            return 'nop'
        if self.instruction == 12:
            return 'syscall'

        return 'UNKNOWN INSTRUCTION'
