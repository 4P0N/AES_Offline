
# pip install BitVector (command for vitvector install)


"""Tables"""
from BitVector import *
import time

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"),
     BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"),
     BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"),
     BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"),
     BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"),
     BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"),
     BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"),
     BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"),
     BitVector(hexstring="09"), BitVector(hexstring="0E")]
]


b = BitVector(hexstring="4E")
int_val = b.intValue()
s = Sbox[int_val]
s = BitVector(intVal=s, size=8)
# print(s.get_bitvector_in_hex())

AES_modulus = BitVector(bitstring='100011011')

bv1 = BitVector(hexstring="02")
bv2 = BitVector(hexstring="02")
bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
# print(bv3)


# ---round constant-------
round_const = BitVector(size=32)
round_const[7] = 1
# print(round_const)


def substituteByte(subsByte):

    for x in range(0, 32, 8):
        int_val = subsByte[x:x+8].intValue()
        s = Sbox[int_val]
        s = BitVector(intVal=s, size=8)
        subsByte[x:x+8] = s

    return subsByte


def getNextRoundKey(bv_key):

    round_key = BitVector(size=128)
    round_key[0:32] = bv_key[96:128]
    # print(round_key1.get_bitvector_in_hex())

    # ----shift left------
    round_key[0:32] = round_key[0:32].__lshift__(8)
    # print(round_key1.get_bitvector_in_hex())

    # -----byte substitute-----
    round_key[0:32] = substituteByte(round_key[0:32])
    # print(round_key1.get_bitvector_in_hex())

    # -----adding round constant----------
    global round_const
    round_key[0:32] = round_key[0:32] ^ round_const
    # print(round_key1.get_bitvector_in_hex())

    round_const_multiplier = BitVector(hexstring="02")
    round_const[0:8] = round_const_multiplier.gf_multiply_modular(
        round_const[0:8], AES_modulus, 8)
    # print(round_const.get_bitvector_in_hex())

    round_key[0:32] = round_key[0:32] ^ bv_key[0:32]
    round_key[32:64] = round_key[0:32] ^ bv_key[32:64]
    round_key[64:96] = round_key[32:64] ^ bv_key[64:96]
    round_key[96:128] = round_key[64:96] ^ bv_key[96:128]

    return round_key


def calcRoundKeys(key):
    for x in range(11):
        #print('Round ' + str(x) + ': ' + key.get_bitvector_in_hex())
        global round_keys
        round_keys.append(key.intValue())
        key = getNextRoundKey(key)


def columnMatrix(key):
    temp = BitVector(size=128)
    cnt = 0
    cnt1 = 0
    cnt2 = 0
    while(cnt < 16):
        temp[cnt1:cnt1+8] = key[cnt2:cnt2+8]
        cnt += 1
        cnt1 += 8
        if cnt == 4:
            cnt2 = 8
        elif cnt == 8:
            cnt2 = 16
        elif cnt == 12:
            cnt2 = 24
        else:
            cnt2 += 32

    return temp


def mixColumn(data):
    data = columnMatrix(data)
    temp = BitVector(size=128)

    temp[0:8] = Mixer[0][0].gf_multiply_modular(data[0:8], AES_modulus, 8) ^ Mixer[0][1].gf_multiply_modular(
        data[8:16], AES_modulus, 8) ^ Mixer[0][2].gf_multiply_modular(data[16:24], AES_modulus, 8) ^ Mixer[0][3].gf_multiply_modular(data[24:32], AES_modulus, 8)
    temp[8:16] = Mixer[0][0].gf_multiply_modular(data[32:40], AES_modulus, 8) ^ Mixer[0][1].gf_multiply_modular(
        data[40:48], AES_modulus, 8) ^ Mixer[0][2].gf_multiply_modular(data[48:56], AES_modulus, 8) ^ Mixer[0][3].gf_multiply_modular(data[56:64], AES_modulus, 8)
    temp[16:24] = Mixer[0][0].gf_multiply_modular(data[64:72], AES_modulus, 8) ^ Mixer[0][1].gf_multiply_modular(
        data[72:80], AES_modulus, 8) ^ Mixer[0][2].gf_multiply_modular(data[80:88], AES_modulus, 8) ^ Mixer[0][3].gf_multiply_modular(data[88:96], AES_modulus, 8)
    temp[24:32] = Mixer[0][0].gf_multiply_modular(data[96:104], AES_modulus, 8) ^ Mixer[0][1].gf_multiply_modular(
        data[104:112], AES_modulus, 8) ^ Mixer[0][2].gf_multiply_modular(data[112:120], AES_modulus, 8) ^ Mixer[0][3].gf_multiply_modular(data[120:128], AES_modulus, 8)

    temp[32:40] = Mixer[1][0].gf_multiply_modular(data[0:8], AES_modulus, 8) ^ Mixer[1][1].gf_multiply_modular(
        data[8:16], AES_modulus, 8) ^ Mixer[1][2].gf_multiply_modular(data[16:24], AES_modulus, 8) ^ Mixer[1][3].gf_multiply_modular(data[24:32], AES_modulus, 8)
    temp[40:48] = Mixer[1][0].gf_multiply_modular(data[32:40], AES_modulus, 8) ^ Mixer[1][1].gf_multiply_modular(
        data[40:48], AES_modulus, 8) ^ Mixer[1][2].gf_multiply_modular(data[48:56], AES_modulus, 8) ^ Mixer[1][3].gf_multiply_modular(data[56:64], AES_modulus, 8)
    temp[48:56] = Mixer[1][0].gf_multiply_modular(data[64:72], AES_modulus, 8) ^ Mixer[1][1].gf_multiply_modular(
        data[72:80], AES_modulus, 8) ^ Mixer[1][2].gf_multiply_modular(data[80:88], AES_modulus, 8) ^ Mixer[1][3].gf_multiply_modular(data[88:96], AES_modulus, 8)
    temp[56:64] = Mixer[1][0].gf_multiply_modular(data[96:104], AES_modulus, 8) ^ Mixer[1][1].gf_multiply_modular(
        data[104:112], AES_modulus, 8) ^ Mixer[1][2].gf_multiply_modular(data[112:120], AES_modulus, 8) ^ Mixer[1][3].gf_multiply_modular(data[120:128], AES_modulus, 8)

    temp[64:72] = Mixer[2][0].gf_multiply_modular(data[0:8], AES_modulus, 8) ^ Mixer[2][1].gf_multiply_modular(
        data[8:16], AES_modulus, 8) ^ Mixer[2][2].gf_multiply_modular(data[16:24], AES_modulus, 8) ^ Mixer[2][3].gf_multiply_modular(data[24:32], AES_modulus, 8)
    temp[72:80] = Mixer[2][0].gf_multiply_modular(data[32:40], AES_modulus, 8) ^ Mixer[2][1].gf_multiply_modular(
        data[40:48], AES_modulus, 8) ^ Mixer[2][2].gf_multiply_modular(data[48:56], AES_modulus, 8) ^ Mixer[2][3].gf_multiply_modular(data[56:64], AES_modulus, 8)
    temp[80:88] = Mixer[2][0].gf_multiply_modular(data[64:72], AES_modulus, 8) ^ Mixer[2][1].gf_multiply_modular(
        data[72:80], AES_modulus, 8) ^ Mixer[2][2].gf_multiply_modular(data[80:88], AES_modulus, 8) ^ Mixer[2][3].gf_multiply_modular(data[88:96], AES_modulus, 8)
    temp[88:96] = Mixer[2][0].gf_multiply_modular(data[96:104], AES_modulus, 8) ^ Mixer[2][1].gf_multiply_modular(
        data[104:112], AES_modulus, 8) ^ Mixer[2][2].gf_multiply_modular(data[112:120], AES_modulus, 8) ^ Mixer[2][3].gf_multiply_modular(data[120:128], AES_modulus, 8)

    temp[96:104] = Mixer[3][0].gf_multiply_modular(data[0:8], AES_modulus, 8) ^ Mixer[0][3].gf_multiply_modular(
        data[8:16], AES_modulus, 8) ^ Mixer[3][2].gf_multiply_modular(data[16:24], AES_modulus, 8) ^ Mixer[3][3].gf_multiply_modular(data[24:32], AES_modulus, 8)
    temp[104:112] = Mixer[3][0].gf_multiply_modular(data[32:40], AES_modulus, 8) ^ Mixer[3][1].gf_multiply_modular(
        data[40:48], AES_modulus, 8) ^ Mixer[3][2].gf_multiply_modular(data[48:56], AES_modulus, 8) ^ Mixer[3][3].gf_multiply_modular(data[56:64], AES_modulus, 8)
    temp[112:120] = Mixer[3][0].gf_multiply_modular(data[64:72], AES_modulus, 8) ^ Mixer[3][1].gf_multiply_modular(
        data[72:80], AES_modulus, 8) ^ Mixer[3][2].gf_multiply_modular(data[80:88], AES_modulus, 8) ^ Mixer[3][3].gf_multiply_modular(data[88:96], AES_modulus, 8)
    temp[120:128] = Mixer[3][0].gf_multiply_modular(data[96:104], AES_modulus, 8) ^ Mixer[3][1].gf_multiply_modular(
        data[104:112], AES_modulus, 8) ^ Mixer[3][2].gf_multiply_modular(data[112:120], AES_modulus, 8) ^ Mixer[3][3].gf_multiply_modular(data[120:128], AES_modulus, 8)

    return temp


def invMixColumn(data):
    temp = BitVector(size=128)

    temp[0:8] = InvMixer[0][0].gf_multiply_modular(data[0:8], AES_modulus, 8) ^ InvMixer[0][1].gf_multiply_modular(
        data[8:16], AES_modulus, 8) ^ InvMixer[0][2].gf_multiply_modular(data[16:24], AES_modulus, 8) ^ InvMixer[0][3].gf_multiply_modular(data[24:32], AES_modulus, 8)
    temp[8:16] = InvMixer[0][0].gf_multiply_modular(data[32:40], AES_modulus, 8) ^ InvMixer[0][1].gf_multiply_modular(
        data[40:48], AES_modulus, 8) ^ InvMixer[0][2].gf_multiply_modular(data[48:56], AES_modulus, 8) ^ InvMixer[0][3].gf_multiply_modular(data[56:64], AES_modulus, 8)
    temp[16:24] = InvMixer[0][0].gf_multiply_modular(data[64:72], AES_modulus, 8) ^ InvMixer[0][1].gf_multiply_modular(
        data[72:80], AES_modulus, 8) ^ InvMixer[0][2].gf_multiply_modular(data[80:88], AES_modulus, 8) ^ InvMixer[0][3].gf_multiply_modular(data[88:96], AES_modulus, 8)
    temp[24:32] = InvMixer[0][0].gf_multiply_modular(data[96:104], AES_modulus, 8) ^ InvMixer[0][1].gf_multiply_modular(
        data[104:112], AES_modulus, 8) ^ InvMixer[0][2].gf_multiply_modular(data[112:120], AES_modulus, 8) ^ InvMixer[0][3].gf_multiply_modular(data[120:128], AES_modulus, 8)

    temp[32:40] = InvMixer[1][0].gf_multiply_modular(data[0:8], AES_modulus, 8) ^ InvMixer[1][1].gf_multiply_modular(
        data[8:16], AES_modulus, 8) ^ InvMixer[1][2].gf_multiply_modular(data[16:24], AES_modulus, 8) ^ InvMixer[1][3].gf_multiply_modular(data[24:32], AES_modulus, 8)
    temp[40:48] = InvMixer[1][0].gf_multiply_modular(data[32:40], AES_modulus, 8) ^ InvMixer[1][1].gf_multiply_modular(
        data[40:48], AES_modulus, 8) ^ InvMixer[1][2].gf_multiply_modular(data[48:56], AES_modulus, 8) ^ InvMixer[1][3].gf_multiply_modular(data[56:64], AES_modulus, 8)
    temp[48:56] = InvMixer[1][0].gf_multiply_modular(data[64:72], AES_modulus, 8) ^ InvMixer[1][1].gf_multiply_modular(
        data[72:80], AES_modulus, 8) ^ InvMixer[1][2].gf_multiply_modular(data[80:88], AES_modulus, 8) ^ InvMixer[1][3].gf_multiply_modular(data[88:96], AES_modulus, 8)
    temp[56:64] = InvMixer[1][0].gf_multiply_modular(data[96:104], AES_modulus, 8) ^ InvMixer[1][1].gf_multiply_modular(
        data[104:112], AES_modulus, 8) ^ InvMixer[1][2].gf_multiply_modular(data[112:120], AES_modulus, 8) ^ InvMixer[1][3].gf_multiply_modular(data[120:128], AES_modulus, 8)

    temp[64:72] = InvMixer[2][0].gf_multiply_modular(data[0:8], AES_modulus, 8) ^ InvMixer[2][1].gf_multiply_modular(
        data[8:16], AES_modulus, 8) ^ InvMixer[2][2].gf_multiply_modular(data[16:24], AES_modulus, 8) ^ InvMixer[2][3].gf_multiply_modular(data[24:32], AES_modulus, 8)
    temp[72:80] = InvMixer[2][0].gf_multiply_modular(data[32:40], AES_modulus, 8) ^ InvMixer[2][1].gf_multiply_modular(
        data[40:48], AES_modulus, 8) ^ InvMixer[2][2].gf_multiply_modular(data[48:56], AES_modulus, 8) ^ InvMixer[2][3].gf_multiply_modular(data[56:64], AES_modulus, 8)
    temp[80:88] = InvMixer[2][0].gf_multiply_modular(data[64:72], AES_modulus, 8) ^ InvMixer[2][1].gf_multiply_modular(
        data[72:80], AES_modulus, 8) ^ InvMixer[2][2].gf_multiply_modular(data[80:88], AES_modulus, 8) ^ InvMixer[2][3].gf_multiply_modular(data[88:96], AES_modulus, 8)
    temp[88:96] = InvMixer[2][0].gf_multiply_modular(data[96:104], AES_modulus, 8) ^ InvMixer[2][1].gf_multiply_modular(
        data[104:112], AES_modulus, 8) ^ InvMixer[2][2].gf_multiply_modular(data[112:120], AES_modulus, 8) ^ InvMixer[2][3].gf_multiply_modular(data[120:128], AES_modulus, 8)

    temp[96:104] = InvMixer[3][0].gf_multiply_modular(data[0:8], AES_modulus, 8) ^ InvMixer[3][1].gf_multiply_modular(
        data[8:16], AES_modulus, 8) ^ InvMixer[3][2].gf_multiply_modular(data[16:24], AES_modulus, 8) ^ InvMixer[3][3].gf_multiply_modular(data[24:32], AES_modulus, 8)
    temp[104:112] = InvMixer[3][0].gf_multiply_modular(data[32:40], AES_modulus, 8) ^ InvMixer[3][1].gf_multiply_modular(
        data[40:48], AES_modulus, 8) ^ InvMixer[3][2].gf_multiply_modular(data[48:56], AES_modulus, 8) ^ InvMixer[3][3].gf_multiply_modular(data[56:64], AES_modulus, 8)
    temp[112:120] = InvMixer[3][0].gf_multiply_modular(data[64:72], AES_modulus, 8) ^ InvMixer[3][1].gf_multiply_modular(
        data[72:80], AES_modulus, 8) ^ InvMixer[3][2].gf_multiply_modular(data[80:88], AES_modulus, 8) ^ InvMixer[3][3].gf_multiply_modular(data[88:96], AES_modulus, 8)
    temp[120:128] = InvMixer[3][0].gf_multiply_modular(data[96:104], AES_modulus, 8) ^ InvMixer[3][1].gf_multiply_modular(
        data[104:112], AES_modulus, 8) ^ InvMixer[3][2].gf_multiply_modular(data[112:120], AES_modulus, 8) ^ InvMixer[3][3].gf_multiply_modular(data[120:128], AES_modulus, 8)

    return temp


def encryptData(temp_data):
    for i in range(9):
        # ----------- subsbyte---------------------------------
        for x in range(0, 128, 8):
            int_val = temp_data[x:x+8].intValue()
            s = Sbox[int_val]
            s = BitVector(intVal=s, size=8)
            temp_data[x:x+8] = s

        # print(temp_data.get_bitvector_in_hex())

        # --------- shift rows-------------------------------------

        column_data = columnMatrix(temp_data)
        # print(column_data.get_bitvector_in_hex())

        column_data[32:64] = column_data[32:64].__lshift__(8)
        column_data[64:96] = column_data[64:96].__lshift__(16)
        column_data[96:128] = column_data[96:128].__lshift__(24)

        # print(column_data.get_bitvector_in_hex())

        # ------------- Mix Column ------------------------------

        mix_column_data = mixColumn(column_data)
        #print('Afetr mix column : ')
        # print(mix_column_data.get_bitvector_in_hex())

        # ------ add round key ----------------------------------

        trans_mix_column_data = columnMatrix(mix_column_data)
        curr_rkey = BitVector(intVal=round_keys[i+1], size=128)
        temp_data = trans_mix_column_data ^ curr_rkey
        # print('round_final_data.get_bitvector_in_hex()')
        # print(temp_data.get_bitvector_in_hex())

    # ------------------last round-------------------------------------last round----------------------

    #print('before last round:')
    # print(temp_data.get_bitvector_in_hex())

    # ----------- subsbyte---------------------------------
    for x in range(0, 128, 8):
        int_val = temp_data[x:x+8].intValue()
        s = Sbox[int_val]
        s = BitVector(intVal=s, size=8)
        temp_data[x:x+8] = s

    # --------- shift rows-------------------------------------

    column_data = columnMatrix(temp_data)
    # print(column_data.get_bitvector_in_hex())

    column_data[32:64] = column_data[32:64].__lshift__(8)
    column_data[64:96] = column_data[64:96].__lshift__(16)
    column_data[96:128] = column_data[96:128].__lshift__(24)

    # print(column_data.get_bitvector_in_hex())

    # ------ add round key ----------------------------------

    trans_column_data = columnMatrix(column_data)
    current_round_key = BitVector(intVal=round_keys[10], size=128)
    temp_data = trans_column_data ^ current_round_key
    # print(round_final_data.get_bitvector_in_hex())

    return temp_data


def decryptCypher(tem_data):
    for i in range(10):
        # ---------inv shift rows-------------------------------------

        column_data = columnMatrix(tem_data)
        # print(column_data.get_bitvector_in_hex())

        column_data[32:64] = column_data[32:64].__rshift__(8)
        column_data[64:96] = column_data[64:96].__rshift__(16)
        column_data[96:128] = column_data[96:128].__rshift__(24)

        #print('INV SHIFT ROW:')
        # print(column_data.get_bitvector_in_hex())
        column_data = columnMatrix(column_data)

        # print(column_data.get_bitvector_in_hex())

        # -----------inv subsbyte---------------------------------
        for x in range(0, 128, 8):
            int_val = column_data[x:x+8].intValue()
            s = InvSbox[int_val]
            s = BitVector(intVal=s, size=8)
            column_data[x:x+8] = s

        #print('inv sub:')
        # print(column_data.get_bitvector_in_hex())

        # ------ add round key ----------------------------------

        current_round_key = BitVector(intVal=round_keys[9-i], size=128)
        tem_data = column_data ^ current_round_key
        #print('add round key')
        # print(tem_data.get_bitvector_in_hex())

        # ------------- Mix Column ------------------------------
        if i < 9:
            tem_data = invMixColumn(tem_data)
            tem_data = columnMatrix(tem_data)
            #print('mix COLUMN:')
            # print(tem_data.get_bitvector_in_hex())

    return tem_data


    #       ---------------------------  Starting Here    ------------------------------------------------#


#key=input("Enter the key :")
#inputData=input("Enter the data to be encrypted :")

key = 'BUET CSE16 Batch'
inputData = 'WillGraduateSoon'
bv_key = BitVector(textstring=key)
bv_main_data=BitVector(textstring=inputData)

#-------key formatting------------
if bv_key.length()==128:
    root_key=bv_key
elif bv_key.length()>128:
    root_key=BitVector(size=128)
    root_key=bv_key[0:128]
else:
    root_key=BitVector(intVal=bv_key.intValue(), size=128)


#--------------key scheduling-----------------
elapsed_time = []
round_keys = []
start=time.time()
calcRoundKeys(root_key)
end=time.time()
elapsed_time.append(end-start)



print('Key:')
print(key + ' [IN ASCII]')
print(root_key.get_bitvector_in_hex() + ' [IN HEX]')
print()
print('Plain Text:')
print(inputData + ' [IN ASCII]')
print(bv_main_data.get_bitvector_in_hex() + ' [IN HEX]')
print()

#------------------------------Encryption Strats------------------------------------

padding=0
start=time.time()

if bv_main_data.length()%128==0:
    extra=0
else:
    extra=128

#print(int(bv_main_data.length()/128))
cypher_full_text=BitVector(size=(int(bv_main_data.length()/128))*128 + extra)

for i in range (0,bv_main_data.length(),128):
    #--------block encrytion loop------------------
    #print(bv_main_data.length())
    t=BitVector(size=128)
    #print(t.get_bitvector_in_hex())
    if i+128>bv_main_data.length():
        #print("################")
        padding= i+128 - bv_main_data.length()
        t[0:128-padding]=bv_main_data[i:bv_main_data.length()]
    else:
        t=bv_main_data[i:i+128]


    #print(t.get_bitvector_in_hex())
    temp_data=t ^ root_key
    cypher_text=encryptData(temp_data)
    #print(cypher_text.get_bitvector_in_hex())
    #print("cupher fyll text len : " + str(cypher_full_text.length()))
    cypher_full_text[i:i+128]=cypher_text
    


    #print(t.get_bitvector_in_ascii())



end=time.time()
elapsed_time.append(end-start)
print('Cipher Text:')
print(cypher_full_text.get_bitvector_in_hex() + ' [IN HEX]')
print(cypher_full_text.get_bitvector_in_ascii() + ' [IN ASCII]')
print()



#-------------------------Decryption Starts-----------------------------

curr_rkey=BitVector(intVal=round_keys[10],size=128)
#print(curr_rkey.get_bitvector_in_hex())
start=time.time()

main_full_data=BitVector(size=cypher_full_text.length()-padding)
#print("main full data lrn: " + str(main_full_data.length()))

for i in range (0,cypher_full_text.length(),128):
    #--------block decrytion loop------------------
    t=BitVector(size=128)
    
    t=cypher_full_text[i:i+128]

    tem_data=t ^ curr_rkey
    main_data=decryptCypher(tem_data)

    if i==cypher_full_text.length()-128:
        #print("printing main data here  " + str(main_data.get_bitvector_in_hex()))
        #main_data=main_data.__rshift__(padding)
        main_full_data[i:main_full_data.length()]=main_data[0:128-padding]
    else:
        main_full_data[i:i+128]=main_data
    

end=time.time()
elapsed_time.append(end-start)
print('Deciphered Text:')
print(main_full_data.get_bitvector_in_hex() + ' [IN HEX]')
print(main_full_data.get_bitvector_in_ascii() + ' [IN ASCII]')
print()

print('Execution Time')
print('Key Scheduling: ' + str(elapsed_time[0]))
print('Encryption Time: ' + str(elapsed_time[1]))
print('Decryption Time: ' + str(elapsed_time[2]))
print()

"""

# --------------------Rijndeal-box-------------------

def printRijndaelBox(inverse):
    print()
    if inverse==False:
        print("----------------S-Box--------------")
        print()
        global Rijndael_S_box
        idx=0
        for i in range(16):
            for j in range(16):
                print(Rijndael_S_box[idx].get_bitvector_in_hex() , end=" ")
                idx+=1
            print()
    else:
        print("--------------Inverse-S-Box------------")
        print()
        global Rijndael_Inverse_S_box
        idx=0
        for i in range(16):
            for j in range(16):
                print(Rijndael_Inverse_S_box[idx].get_bitvector_in_hex() , end=" ")
                idx+=1
            print()
    print()



Rijndael_S_box = [BitVector(hexstring="63")]
for i in range(1,256):
    a = BitVector(intVal= i, size=8)
    b = a.gf_MI(AES_modulus, 8)
    c = BitVector(hexstring="63")
    int_val = c.intValue()
    val = BitVector(intVal=int_val, size=8) ^ b ^ (b << 1) ^ (b << 1) ^ (b << 1) ^ (b << 1)
    Rijndael_S_box.append(val)

printRijndaelBox(False)


Rijndael_Inverse_S_box = []
for i in range(256):
    if i==99:
        Rijndael_Inverse_S_box.append(BitVector(hexstring="00"))
    else:
        ai = BitVector(intVal= i, size=8)
        ci = BitVector(hexstring="5")
        int_val = ci.intValue()
        val = BitVector(intVal=int_val, size=8) ^ (ai << 1) ^ (ai << 2) ^ (ai << 3)
        bi = val.gf_MI(AES_modulus, 8)
        Rijndael_Inverse_S_box.append(bi)

printRijndaelBox(True)
"""
