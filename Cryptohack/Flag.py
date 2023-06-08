from Cryptodome.Util.number import *
import base64
from pwn import *


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


def FuncXOR():
    label = "label"

    for i in label:
        newLabel = ord(i)
        message = xor(newLabel, 13)

        print(message)


def finalDecryption():
    k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"  # Identity
    k1Bytes = bytes.fromhex(k1)
    
    t1 = xor(k1Bytes, k1Bytes)
    print("K1 in Bytes:", k1Bytes)
    print("K1 XOR K1 =", t1, "\n")

    # k2^k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e" / Commutative
    k2XORk1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
    k2XORk1Bytes = bytes.fromhex(k2XORk1)

    print("K2^K1 in Bytes:", k2XORk1Bytes, "\n")

    # k2^k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1" / Commutative
    k2XORk3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
    k2XORk3Bytes = bytes.fromhex(k2XORk3)

    print("K2^K3 in Bytes:", k2XORk3Bytes, "\n")

    # flag^k1^k3^k2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
    print("Flag:")


finalDecryption()
