import string
import random
# written by dr0ppyb3@r_h@ck3r
# v0.3 - The release version will be much better
# Updated flag: flag{h1d3_0n_p@steb1n}
 
def xor_c(a):
    return bytearray([b^0xA8 for b in bytearray(a)])
 
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ., 1234567890-!{}"
tmp_alphabet = list(alphabet)
random.shuffle(tmp_alphabet, lambda: 0.97444187175646646) # Shuffle the list into random order (but the same order every time)
shuffled_alphabet = ''.join(tmp_alphabet)
 
shuffleit = string.maketrans(alphabet,shuffled_alphabet)
 
handler = open("original_file",'rb')
handler2 = open("encrypted_file",'wb')
contents = handler.read()
handler2.write(xor_c(string.translate(contents,shuffleit)))