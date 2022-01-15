from rope import Rope

def main():
    rope = Rope()
    for i, char in enumerate("helloworld"):
        rope.insert(char, i)
    
    print(rope.get(0, 10))

    # for i in range(15):
    #     rope.splay(i)
    #     print(rope.root.char, rope.get(0, 10))

    # rope2 = rope.cut(5, 7)

    # print(rope.get(0, 15))
    # print(rope2.get(0, 10))

    rope = Rope()
    for i, char in enumerate("abcdef"):
        rope.insert(char, i)

    rope2 = rope.cut(0, 2)
    rope.paste(rope2, 1)

    print(rope.get(0, 10))

    rope2 = rope.cut(4, 6)
    rope.paste(rope2, 0)

    print(rope.get(0, 10))

if __name__ == "__main__":
    main()