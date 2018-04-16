from data.instruction import NAME_FROM_OPCODE
from data.instruction_r import NAME_FROM_FUNCT
from util.util import *

HI, LO = 0, 0

NAME_FROM_REGISTER = [
    'zero', 'at', 'v0', 'v1', 'a0', 'a1', 'a2', 'a3',
    't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7',
    's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7',
    't8', 't9', 'k0', 'k1', 'gp', 'sp', 's8', 'ra'
]

REGISTERS = {key: 0 for key in NAME_FROM_REGISTER}  # TODO: May need to clear the values later.

START_PC = 0x00100008


class Processor(object):
    @staticmethod
    def process(instructions):
        i = 0

        while i < len(instructions):
            instruction = instructions[i]

            print('PC:', i, '  Instruction:', instruction)

            if instruction.is_nop():
                i += 1
                continue

            if instruction.is_syscall():
                if REGISTERS['v0'] == 1:  # Print Integer
                    print('SYSCALL - Print Integer:', REGISTERS['a0'])
                elif REGISTERS['v0'] == 10:  # Exit Program
                    print('SYSCALL - Exit Program')
                    return

                i += 1
                continue

            opcode = instruction.get_opcode()

            if opcode == 0x02:  # Jump
                i = instruction.get_jump_address() - START_PC
                continue

            if opcode == 0x03:  # Jump and Link
                REGISTERS['ra'] = i + 2
                i = instruction.get_jump_address() - START_PC
                continue

            rs = NAME_FROM_REGISTER[instruction.get_rs()]
            rt = NAME_FROM_REGISTER[instruction.get_rt()]

            if opcode == 0x00:  # R-Type
                name = NAME_FROM_FUNCT[instruction.get_funct()]
                rd = NAME_FROM_REGISTER[instruction.get_rd()]
                shamt = instruction.get_shamt()

                if name == 'add' or name == 'addu':
                    REGISTERS[rd] = REGISTERS[rs] + REGISTERS[rt]
                elif name == 'and':
                    REGISTERS[rd] = REGISTERS[rs] & REGISTERS[rt]
                elif name == 'div' or name == 'divu':
                    Processor.LO = REGISTERS[rs] / REGISTERS[rt]
                    Processor.HI = REGISTERS[rs] % REGISTERS[rt]
                elif name == 'jr':
                    i = REGISTERS[rs]
                    continue
                elif name == 'mfhi':
                    REGISTERS[rd] = Processor.HI
                elif name == 'mflo':
                    REGISTERS[rd] = Processor.LO
                elif name == 'mult' or name == 'multu':
                    product = REGISTERS[rs] * REGISTERS[rt]

                    Processor.HI = (product >> 32) & ((2 ** 32) - 1)
                    Processor.LO = product & ((2 ** 32) - 1)
                elif name == 'nor':
                    REGISTERS[rd] = ~(REGISTERS[rs] | REGISTERS[rt])
                elif name == 'or':
                    REGISTERS[rd] = REGISTERS[rs] | REGISTERS[rt]
                elif name == 'slt' or name == 'sltu':
                    REGISTERS[rd] = 1 if REGISTERS[rs] < REGISTERS[rt] else 0
                elif name == 'sll':
                    REGISTERS[rd] = REGISTERS[rt] << shamt
                elif name == 'sra':
                    REGISTERS[rd] = REGISTERS[rt] >> shamt
                elif name == 'srl':
                    pass  # TODO: Implement logical right shift.
                elif name == 'sub' or name == 'subu':
                    REGISTERS[rd] = REGISTERS[rs] - REGISTERS[rt]
            else:  # I-Type
                name = NAME_FROM_OPCODE[opcode]
                immediate = instruction.get_immediate()

                if name == 'addi' or name == 'addiu':
                    REGISTERS[rt] = REGISTERS[rs] + immediate
                elif name == 'andi':
                    REGISTERS[rt] = REGISTERS[rs] & immediate  # TODO: Zero-extend immediate
                elif name == 'beq':
                    if REGISTERS[rs] == REGISTERS[rt]:
                        i += Util.sign_extend(immediate, 15)
                        continue
                elif name == 'bne':
                    if REGISTERS[rs] != REGISTERS[rt]:
                        i += Util.sign_extend(immediate, 15)
                        continue
                elif name == 'lui':
                    REGISTERS[rt] = immediate << 16
                elif name == 'ori':
                    REGISTERS[rt] = REGISTERS[rs] | immediate  # TODO: Zero-extend immediate
                elif name == 'slti' or name == 'sltiu':
                    REGISTERS[rt] = 1 if REGISTERS[rs] < immediate else 0

            print('Registers:', REGISTERS)

            i += 1
