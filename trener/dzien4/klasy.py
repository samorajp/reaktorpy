class Kolor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def to_html(self):
        return self.r, self.g, self.b

