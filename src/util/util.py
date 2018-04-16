class Util(object):
    @staticmethod
    def logical_right_shift(val, n):
        return (val % 0x100000000) >> n

    @staticmethod
    def sign_extend(value, bits):
        sign_bit = 1 << (bits - 1)
        return (value & (sign_bit - 1)) - (value & sign_bit)