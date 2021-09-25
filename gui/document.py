from typing import Final

LINESEP: Final[str] = "\n"

class Document:
    def __init__(self, text):
        self.lines = text.split(LINESEP)
        self.tags = []

    @property
    def text(self):
        return str.join(LINESEP, self.lines)
