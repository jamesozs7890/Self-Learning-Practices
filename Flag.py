from Cryptodome.Util.number import *
import base64


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


def hexToBytes():
    hexCode = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

    bytesCode = bytes.fromhex(hexCode)
    print(bytesCode)


def BytesToBase64():
    hexCode = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

    bytesCode = bytes.fromhex(hexCode)
    print("Bytes:", bytesCode)

    baseSixFour = base64.b64encode(bytesCode)
    print("Base 64:", baseSixFour)


def intToBytes():
    # base10 int
    intNum = int(11515195063862318899931685488813747395775516287289682636499965282714637259206269)

    byteCode = long_to_bytes(intNum)

    print(byteCode)
