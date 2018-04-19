from .instruction import Instruction
from .constants import Constants


class InstructionR(Instruction):
    def __init__(self, instruction):
        super().__init__(instruction)

    def get_rs(self):
        return self.rs

    def get_rt(self):
        return self.rt

    def get_rd(self):
        return self.rd

    def get_shamt(self):
        return self.shamt

    def get_funct(self):
        return self.funct

    def __repr__(self):
        representation = Constants.NAME_FROM_FUNCT[self.funct]
        representation += ' '
        representation += Constants.NAME_FROM_REGISTER[self.rd]
        representation += ' '
        representation += Constants.NAME_FROM_REGISTER[self.rs]
        representation += ' '
        representation += Constants.NAME_FROM_REGISTER[self.rt]

        return representation
