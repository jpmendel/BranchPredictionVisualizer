from .component import Component
from .instruction_table import InstructionTable
from .text_button import TextButton
from src.data.instruction import Instruction
from src.data.instruction_r import InstructionR
from src.data.instruction_i import InstructionI
from src.data.instruction_j import InstructionJ
from src.data.rgb_color import RGBColor
from src.util.util import Util
from src.data.constants import Constants


class Processor(Component):
    START_PC = 0x00100008

    def __init__(self, window, instruction_file):
        super(Processor, self).__init__(window, 0, 0, 1000, 600)
        self.instructions = self.read_instruction_file(instruction_file)
        self.current_pc = 0
        self.registers = { key: 0 for key in Constants.NAME_FROM_REGISTER }
        self.memory = {}
        self.hi = 0
        self.lo = 0
        self.play = False
        self.play_counter = 0
        self.instruction_table = InstructionTable(self.window, 100, 100, self.instructions)
        self.back_button = TextButton(
            self.window,
            self.instruction_table.x + 30, 450,
            60, 30,
            text="<",
            color=RGBColor(0x22, 0x66, 0xDD),
            on_click=self.on_back_button_click)
        self.play_button = TextButton(
            self.window,
            self.instruction_table.x + self.instruction_table.width / 2 - 30, 450,
            60, 30,
            text="Play",
            color=RGBColor(0x22, 0x66, 0xDD),
            on_click=self.on_play_button_click)
        self.forward_button = TextButton(
            self.window,
            self.instruction_table.x + self.instruction_table.width - 90, 450,
            60, 30,
            text=">",
            color=RGBColor(0x22, 0x66, 0xDD),
            on_click=self.on_forward_button_click)

    def update(self):
        if self.play:
            self.animate_play()
        self.play_button.update()
        self.forward_button.update()
        self.back_button.update()

    def render(self):
        self.instruction_table.render()
        self.play_button.render()
        self.forward_button.render()
        self.back_button.render()

    def play_pause_processor(self):
        self.play = not self.play
        self.play_button.text = "Pause" if self.play else "Play"
        self.play_counter = 0

    def play_processor(self):
        self.play = True
        self.play_button.text = "Pause"
        self.play_counter = 0

    def pause_processor(self):
        self.play = False
        self.play_button.text = "Play"
        self.play_counter = 0

    def next_instruction(self):
        if self.current_pc < len(self.instructions) - 1:
            jump = self.process(self.instructions[self.current_pc])
            if not jump:
                self.current_pc += 1
            self.instruction_table.current_pc = self.current_pc

    def previous_instruction(self):
        if self.current_pc > 0:
            self.current_pc -= 1
            self.instruction_table.current_pc = self.current_pc

    def jump_to_instruction(self, target):
        self.current_pc = target
        self.instruction_table.current_pc = self.current_pc

    def click_events(self, event):
        self.play_button.listen(event)
        self.forward_button.listen(event)
        self.back_button.listen(event)

    def on_play_button_click(self):
        self.play_pause_processor()

    def on_forward_button_click(self):
        self.pause_processor()
        self.next_instruction()

    def on_back_button_click(self):
        self.pause_processor()
        self.previous_instruction()

    def animate_play(self):
        self.play_counter += 1
        if self.play_counter == 2:
            self.next_instruction()
            self.play_counter = 0
            if self.current_pc == len(self.instructions) - 1:
                self.pause_processor()

    def read_instruction_file(self, instruction_file):
        with open(instruction_file) as file:
            instructions = []

            for line in file.readlines():
                instruction = int(line, 16)

                # Handle nop and syscall, respectively.
                if instruction == 0 or instruction == 12:
                    instructions.append(Instruction(instruction))
                    continue

                opcode = (instruction >> 26) & 63

                if opcode == 0:
                    instructions.append(InstructionR(instruction))
                elif opcode == 2 or opcode == 3:
                    instructions.append(InstructionJ(instruction))
                else:
                    instructions.append(InstructionI(instruction))
            return instructions

    def process(self, instruction):
        print('PC:', self.current_pc, '  Instruction:', instruction)

        if instruction.is_nop():
            return

        if instruction.is_syscall():
            if self.registers['v0'] == 1:  # Print Integer
                print('SYSCALL - Print Integer:', self.registers['a0'])
            elif self.registers['v0'] == 10:  # Exit Program
                print('SYSCALL - Exit Program')
                self.pause_processor()
                return True
            return

        opcode = instruction.get_opcode()

        if opcode == 0x02:  # Jump
            self.current_pc = instruction.get_jump_address() - self.START_PC
            return True

        if opcode == 0x03:  # Jump and Link
            self.registers['ra'] = self.current_pc + 2
            self.current_pc = instruction.get_jump_address() - self.START_PC
            return True

        rs = Constants.NAME_FROM_REGISTER[instruction.get_rs()]
        rt = Constants.NAME_FROM_REGISTER[instruction.get_rt()]

        if opcode == 0x00:  # R-Type
            name = Constants.NAME_FROM_FUNCT[instruction.get_funct()]
            rd = Constants.NAME_FROM_REGISTER[instruction.get_rd()]
            shamt = instruction.get_shamt()

            if name == 'add' or name == 'addu':
                self.registers[rd] = self.registers[rs] + self.registers[rt]
            elif name == 'and':
                self.registers[rd] = self.registers[rs] & self.registers[rt]
            elif name == 'div' or name == 'divu':
                self.lo = self.registers[rs] / self.registers[rt]
                self.hi = self.registers[rs] % self.registers[rt]
            elif name == 'jr':
                self.current_pc = self.registers[rs]
                return True
            elif name == 'mfhi':
                self.registers[rd] = self.hi
            elif name == 'mflo':
                self.registers[rd] = self.lo
            elif name == 'mult' or name == 'multu':
                product = self.registers[rs] * self.registers[rt]
                self.hi = (product >> 32) & ((2 ** 32) - 1)
                self.lo = product & ((2 ** 32) - 1)
            elif name == 'nor':
                self.registers[rd] = ~(self.registers[rs] | self.registers[rt])
            elif name == 'or':
                self.registers[rd] = self.registers[rs] | self.registers[rt]
            elif name == 'slt' or name == 'sltu':
                self.registers[rd] = 1 if self.registers[rs] < self.registers[rt] else 0
            elif name == 'sll':
                self.registers[rd] = self.registers[rt] << shamt
            elif name == 'sra':
                self.registers[rd] = self.registers[rt] >> shamt
            elif name == 'srl':
                self.registers[rd] = Util.logical_right_shift(self.registers[rt], shamt)
            elif name == 'sub' or name == 'subu':
                self.registers[rd] = self.registers[rs] - self.registers[rt]
        else:  # I-Type
            name = Constants.NAME_FROM_OPCODE[opcode]
            immediate = instruction.get_immediate()
            sign_extended_immediate = Util.sign_extend(immediate, 15)

            if name == 'addi' or name == 'addiu':
                self.registers[rt] = self.registers[rs] + sign_extended_immediate
            elif name == 'andi':
                self.registers[rt] = self.registers[rs] & immediate
            elif name == 'beq':
                if self.registers[rs] == self.registers[rt]:
                    self.current_pc += sign_extended_immediate + 1
                    return True
            elif name == 'bne':
                if self.registers[rs] != self.registers[rt]:
                    self.current_pc += sign_extended_immediate + 1
                    return True
            elif name == 'lbu':
                self.registers[rt] = (self.memory[self.registers[rs] + sign_extended_immediate]) & 255
            elif name == 'lhu':
                self.registers[rt] = (self.memory[self.registers[rs] + sign_extended_immediate] & 65535)
            elif name == 'lui':
                self.registers[rt] = immediate << 16
            elif name == 'll' or name == 'lw':
                self.registers[rt] = self.memory[self.registers[rs] + sign_extended_immediate]
            elif name == 'ori':
                self.registers[rt] = self.registers[rs] | immediate
            elif name == 'sb':
                value = self.memory[self.registers[rs] + sign_extended_immediate]
                value &= ~0xFF
                value |= (self.registers[rt] & 255)
                self.memory[self.registers[rs] + sign_extended_immediate] = value
            elif name == 'sh':
                value = self.memory[self.registers[rs] + sign_extended_immediate]
                value &= ~0xFFFF
                value |= (self.registers[rt] & 65535)
                self.memory[self.registers[rs] + sign_extended_immediate] = value
            elif name == 'slti' or name == 'sltiu':
                self.registers[rt] = 1 if self.registers[rs] < sign_extended_immediate else 0
            elif name == 'sw':
                self.memory[self.registers[rs] + sign_extended_immediate] = self.registers[rt]

            print('\tRegisters:', self.registers)
            print('\tMemory:', self.memory)
