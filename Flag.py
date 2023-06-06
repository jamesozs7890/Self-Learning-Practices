def flag1():
    ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

    print("Here is your flag:")
    print("".join(chr(o ^ 0x32) for o in ords))


def flag2():
    ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

    print("Here is your flag:")

    for o in ords:
        flagWord = chr(o)
        print(" ".join(flagWord), end="")

    print("\n")

    # shortcut
    print("".join(chr(o) for o in ords))

flag2()