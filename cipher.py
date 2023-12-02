key = int(input())
if 0<key<26:
    ptext = input()
    ctext = ""
    if ptext == "":
        print(ctext)
    elif ptext.isalpha() and ptext.isupper():
        for i in range(0, len(ptext)):
            ch = ptext[i]
            asciich = ord(ch)
            normch = asciich - 65
            cnormch = (normch + key) % 26
            cascii = cnormch + 65
            cch = chr(cascii)
            ctext = ctext + cch
        print(ctext)
    elif ptext.islower() or ptext.isalpha()==False:
        print("Invalid Input")    
elif key<0 or key>25:
    print("Invalid Input")