
class ProcessorState:

    def __init__(self, pc, registers, memory):
        self.pc = pc
        self.registers = registers
        self.memory = memory

    def __repr__(self):
        return str(self.pc)

    def get_pc(self):
        return self.pc

    def get_registers(self):
        return self.registers

    def get_memory(self):
        return self.memory
