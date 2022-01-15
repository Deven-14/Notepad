from rope import Rope

def main():
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

if __name__ == "__main__":
    main()