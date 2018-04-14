class RGBColor(object):
    def __init__(self, red, green=None, blue=None):
        self.red = red
        self.green = green if green is not None else red
        self.blue = blue if blue is not None else red

    def __repr__(self):
        return "#{:02x}{:02x}{:02x}".format(self.red, self.green, self.blue)

    def __add__(self, other):
        return RGBColor(
            self.red + other.red if self.red + other.red < 255 else 255,
            self.green + other.green if self.green + other.green < 255 else 255,
            self.blue + other.blue if self.blue + other.blue < 255 else 255)

    def __sub__(self, other):
        return RGBColor(
            self.red - other.red if self.red - other.red > 0 else 0,
            self.green - other.green if self.green - other.green > 0 else 0,
            self.blue - other.blue if self.blue - other.blue > 0 else 0)
