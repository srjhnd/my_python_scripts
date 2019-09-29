# coding: utf-8
base64code = [chr(i) for i in  range(65,91)] + [chr(i) for i in range(97,123)] + [i for i in range(0,10)] + ['+','/']

def base64enc(txt):
    txt_enc = []
    txt_bin = []

    for i in range(len(txt)):
        txt_bin += bin(ord(txt[i]))[2:].zfill(8)

    if len(txt_bin) == 16:
        txt_bin += bin(0)[2:].zfill(8)
    elif len(txt_bin) == 8:
        txt_bin += 2 * bin(0)[2:].zfill(8)

    if len(txt_bin)%3 == 0:
        for i in range(0,len(txt_bin),6):
            txt_enc += [base64code[int(''.join(txt_bin[i:i+6]),2)]]
    return txt_enc

def base64(txt):
    txt_enc = []
    for i in range(0,len(txt),3):
            txt_enc += base64enc(txt[i:i+3])
    if len(txt)%3 == 2:
        txt_enc += ['=']
    if len(txt)%3 == 1:
        txt_enc += ['==']
    return txt_enc


def main():
    input_txt = raw_input()
    encoded_txt = base64(input_txt)
    print(''.join(str(v) for v in encoded_txt))

if (__name__ == "__main__"):
    main()



#decoded_txt = base64dec(encoded_txt)
#print "decoded text: "+decoded_txt
