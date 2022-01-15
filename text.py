from rope import Rope


class Text:

    def __init__(self, string=None):
        self.rope = Rope()
        self.cut_rope = None
        if string != None:
            self.append(string)
    
    def append(self, string):
        self.rope.extend(string)
    
    def insert(self, index, string):
        for i, char in zip(range(index, index + len(string)), string):
            self.rope.insert(i, char)
    
    def subtext(self, start, stop):
        return self.rope.substring(start, stop)
    
    def cut(self, start, stop):
        temp_rope = self.rope.slice(start, stop)
        self.cut_rope = temp_rope
    
    def paste(self, index):
        if self.cut_rope != None:
            self.rope.join(index, self.cut_rope)

    def remove(self, start, stop):
        temp_rope = self.rope.slice(start, stop)
        del temp_rope
    
    def __str__(self):
        return self.subtext(0, self.rope.get_nNodes())
        