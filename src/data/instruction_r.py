from data.instruction import Instruction

NAME_FROM_FUNCT = {
     3: 'sra',
    16: 'mfhi', 18: 'mflo',
    24: 'mult', 25: 'multu',
    26: 'div',  27: 'divu',
    32: 'add',  33: 'addu',
    36: 'and',   8:  'jr',
    39: 'nor',  37: 'or',
    42: 'slt',  43: 'sltu',
    0:  'sll',   2:  'srl',
    34: 'sub',  35: 'subu'
}


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
        from .processor import NAME_FROM_REGISTER

        representation = NAME_FROM_FUNCT[self.funct]
        representation += ' '
        representation += NAME_FROM_REGISTER[self.rd]
        representation += ' '
        representation += NAME_FROM_REGISTER[self.rs]
        representation += ' '
        representation += NAME_FROM_REGISTER[self.rt]

        return representation
