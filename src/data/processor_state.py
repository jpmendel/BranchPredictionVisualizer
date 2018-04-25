
class ProcessorState:

    def __init__(self, pc, registers, memory, branch_history, pattern_history,
                 meta_history, global_branch_history, branch_result,
                 taken_taken_count, not_taken_taken_count, taken_not_taken_count,
                 not_taken_not_taken_count):
        self.pc = pc
        self.registers = registers
        self.memory = memory
        self.branch_history = branch_history
        self.pattern_history = pattern_history
        self.meta_history = meta_history
        self.global_branch_history = global_branch_history
        self.branch_result = branch_result
        self.taken_taken_count = taken_taken_count
        self.not_taken_taken_count = not_taken_taken_count
        self.taken_not_taken_count = taken_not_taken_count
        self.not_taken_not_taken_count = not_taken_not_taken_count

    def __repr__(self):
        return str(self.pc)

    def get_pc(self):
        return self.pc

    def get_registers(self):
        return self.registers

    def get_memory(self):
        return self.memory

    def get_branch_history(self):
        return self.branch_history

    def get_pattern_history(self):
        return self.pattern_history

    def get_meta_history(self):
        return self.meta_history

    def get_global_branch_history(self):
        return self.global_branch_history

    def get_branch_result(self):
        return self.branch_result

    def get_taken_taken_count(self):
        return self.taken_taken_count

    def get_not_taken_taken_count(self):
        return self.not_taken_taken_count

    def get_taken_not_taken_count(self):
        return self.taken_not_taken_count

    def get_not_taken_not_taken_count(self):
        return self.not_taken_not_taken_count
