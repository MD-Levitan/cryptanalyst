from Crypto.Cipher import AES
import base64

def pkcs7(data, block=16):
    data += bytearray([(block - len(data) % block)] * (block - len(data) % block))
    return data

key_b64 = "AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRqrHB0eHyA="
cipher_text = "cY1Y1VPXbhUqzYLIOVR0RhUXD5l+dmymBfr1vIKlyqD8KqHUUp2I3dhFXgASdGWzRhOdTj8WWFTJPK0k/GDEVUBDCk1MiB8rCmTZluVHImczlOXEwJSUEgwDHA6AbiCwyAU58e9j9QbN+HwEm1TPKHQ6JrIOpdFWoYjS+cUCZfo/85Lqi26Gj7JJxCDF8PrBp/EtHLmmTmaAVWS0ID2cJpdmNDl54N7tg5TFTrdtcIplc1tDvoCLFPEomNa5booC"
with open("text", "r") as f:
    plain_text_clear = f.read()

plain_text = pkcs7(plain_text_clear.encode('utf-8'))
cipher_text = base64.b64decode(cipher_text)
plain_text_list = [plain_text[i * 16: (i + 1) * 16] for i in range(0, len(plain_text) // 16)]
cipher_text_list = [cipher_text[i * 16: (i + 1) * 16] for i in range(0, len(cipher_text) // 16)]
ecb_crypter = AES.new(base64.b64decode(key_b64), AES.MODE_ECB)

import sys
def xor(var, key):
    key = key[:len(var)]
    int_var = int.from_bytes(var, sys.byteorder)
    int_key = int.from_bytes(key, sys.byteorder)
    int_enc = int_var ^ int_key
    return int_enc.to_bytes(len(var), sys.byteorder)

iv = None
for encr, decr in zip(reversed(plain_text_list), reversed(cipher_text_list)):
    if iv is not None:
        decr_b = xor(decr, iv)
    decr_new = ecb_crypter.decrypt(decr)
    iv = xor(decr_new, encr)

test_crypter = AES.new(base64.b64decode(key_b64), AES.MODE_CBC, iv)
decr = test_crypter.encrypt(plain_text)
if decr == cipher_text:
    print("Success decode")
    print(iv.decode("utf-8"))
