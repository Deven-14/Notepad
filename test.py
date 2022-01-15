from rope import Rope
from text import Text

def rope_test():
    rope = Rope()
    # for i, char in enumerate("helloworld"):
    #     rope.insert(char, i)
    # rope.extend("helloworld")
    # print(rope.substring(0, 20))

    # for i in range(15):
    #     rope.splay(i)
    #     print(rope.root.char, rope.substring(0, 10))

    # rope2 = rope.slice(5, 7)

    # print(rope.substring(0, 15))
    # print(rope2.substring(0, 10))

    rope = Rope()
    # for i, char in enumerate("abcdef"):
    #     rope.insert(char, i)
    rope.extend("hlelowrold")

    print(rope.substring(0, 10))

    rope2 = rope.slice(1, 2)
    rope.join(2, rope2)

    print(rope.substring(0, 10))

    rope2 = rope.slice(6, 7)
    rope.join(7, rope2)

    print(rope.substring(0, 10))

def main():
    text = Text("abcdefghijklmnop")
    print(text)
    text.append("qrstuvwxyz")
    print(text)
    text.insert(5, "ven")
    print(text)
    text.cut(3, 8)
    print(text)
    text.paste(0)
    print(text)
    text.remove(0, 5)
    print(text)
    print(text.subtext(3, 13))

if __name__ == "__main__":
    main()