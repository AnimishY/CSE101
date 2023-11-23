def swap_case(s):
    output = ""
    for i in range(0,len(s)):
        if s[i].isupper():
            output = output+s[i].lower()
        else:
            output = output+s[i].upper()
            
    print(output)

if __name__ == '__main__':
    s = input()
    swap_case(s)