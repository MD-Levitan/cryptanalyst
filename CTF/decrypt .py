import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random
import string

class Nonce(object):
    def __init__(self):
        self.value = Random.new().read(AES.block_size)
    def __call__(self):
        return self.value

def encrypt_line(cipher, line):
    return base64.b64encode(cipher.encrypt(line))

def encrypt_file(filename):
    key = Random.new().read(16)
    nonce = Nonce()
    
    f_in = open(filename, "r")
    f_out = open(filename + ".crypt", "w")
    
    for line in f_in.read().split("\n"):
        if len(line) > 1:
            cipher = AES.new(key, AES.MODE_CTR, counter=nonce)
            line_enc = encrypt_line(cipher, line)
            f_out.write(line_enc + "\n")
     
def decrypt_file(filename):
    f_in = open(filename, "r")
    #f_out = open(filename + ".crypt", "w")
    
    lines = []
    for line in f_in.read().split("\n"):
        if len(line) > 1:
            ##cipher = AES.new(key, AES.MODE_CTR, counter=nonce)
            line = base64.b64decode(line)
            print(str(len(line)) + " " + str(len(line) % 16))
            print
            lines.append(line)
    print(len(lines))
    return lines


def try_(data, block=16, values=None):
    if values is None:
        values = [[set(string.printable)] * block] * len(data)
    for number in range(0, len(data)):
        xor_list = []
        for y in data:
            xor_list.append(list(map(lambda x: x[0] ^ x[1], zip(data[number][:block], y[:block]))))

        result = []
        for it in range(0, block):
            variants = []
            for xor_data_ind in range(0, len(data)):
                letter_variant = []
                letter_variant2 = []
                for i in values[xor_data_ind][it]:
                    for j in values[number][it]:
                        if ord(i) ^ ord(j) == xor_list[xor_data_ind][it]:
                            letter_variant.append(j)
                            letter_variant2.append(i)
                variants.append(set(letter_variant))
                #values[xor_data_ind][it] = values[xor_data_ind][it].intersection(set(letter_variant2))


            res = set(variants[0])
            for var in variants:
                res = res.intersection(var)
            result.append(res)

        #new_values.append(result)
        values[number] = result
    return values


def try__(data, words, block=16):
    import enchant
    dictionary = enchant.Dict("en_US")
    words_res = set()
    for number in range(0, 1):
        xor_list = []
        for y in data:
            xor_list.append(list(map(lambda x: x[0] ^ x[1], zip(data[number][:block], y[:block]))))

        for word in words:
            word_b = str(word).encode("UTF-8")
            for ind in range(0, len(xor_list)):
                if ind == number:
                    continue
                xor_word = xor_list[ind]
                for i in range(0, block):
                    result = list(map(lambda x: x[0] ^ x[1], zip(word_b, xor_word[i:i + len(word_b)])))
                    new_word = "".join(list(map(chr, result)))
                    if result == list(filter(lambda x: chr(x) in string.printable, result)):# \
                            #and dictionary.check(new_word):
                        print("Message {}:{}, find word {} with {} in message{}".format(
                            str(ind), i, "".join(list(map(chr, result))), word, number))
                        words_res.add("".join(list(map(chr, result))))
    print(words_res)



var = decrypt_file("file.txt.crypt")
print(var)
# for i in range(1, len(var)):
#     print(chr(ord("?") ^ var[i][16] ^ var[0][16]))
#try__(var, ["the", "flag", "you", "yet", "if", "The", "Flag", "can", "should", "man", "is", "Is", "IV"])
try__(var, ["validate"])
