
class Instruction:
    def __init__(self, instruction):
        self.opcode = instruction >> 26
