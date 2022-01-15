from rope import Rope


class Text:

    def __init__(self, string=None):
        self.rope = Rope()
        self.undo_stack = []
        self.redo_stack = []
        self.cut_rope = None
        if string != None:
            self.append(string)
    
    def append(self, string):
        self.rope.extend(string)
        self.undo_stack.append(("append", string))
    
    def insert(self, index, string):
        for i in range(index, index + len(string)):
            self.insert(i, string[i])
        self.undo_stack.append(("insert", index, string))
    
    def subtext(self, start, stop):
        return self.rope.substring(start, stop)
    
    def cut(self, start, stop):
        temp_rope = self.rope.slice(start, stop)
        self.cut_rope = temp_rope
        self.undo_stack.append(('cut', start, stop, temp_rope))
    
    def paste(self, index):
        if self.cut_rope != None:
            self.undo_stack.append(('paste', index, self.cut_rope.get_nNodes()))
            self.rope.join(index, self.cut_rope)

    def remove(self, start, stop):
        temp_rope = self.rope.slice(start, stop)
        self.undo_stack.append(('remove', start, stop, temp_rope))

    def undo(self):
        if len(self.undo_stack) == 0:
            return
        operation = self.undo_stack.pop()
        if operation[0] == "append":
            self.undo_append(operation[1])
        elif operation[0] == "insert":
            self.undo_insert()
        elif operation[0] == "cut":
            self.undo_cut()
        elif operation[0] == "paste":
            self.undo_paste()
        elif operation[0] == "remove":
            self.undo_remove()
    
    def undo_append(self, string):
        self.remove
