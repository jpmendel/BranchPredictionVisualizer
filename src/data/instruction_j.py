from data.instruction import Instruction
from data.instruction import NAME_FROM_OPCODE


class InstructionJ(Instruction):
    def __init__(self, instruction):
        super().__init__(instruction)

    def get_jump_address(self):
        return self.jump_address

    def __repr__(self):
        representation = NAME_FROM_OPCODE[self.opcode]
        representation += ' '
        representation += "0x%X" % self.jump_address

        return representation
