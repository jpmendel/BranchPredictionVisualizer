from Instruction import *
from Processor import *


class InstructionTypeI(Instruction):
    def __init__(self, instruction):
        super().__init__(instruction)

    def get_rs(self):
        return self.rs

    def get_rt(self):
        return self.rt

    def get_immediate(self):
        return self.immediate

    def __repr__(self):
        representation = NAME_FROM_OPCODE[self.opcode]
        representation += ' '
        representation += NAME_FROM_REGISTER[self.rt]
        representation += ' '
        representation += NAME_FROM_REGISTER[self.rs]
        representation += ' '
        representation += "0x%X" % self.immediate

        return representation
