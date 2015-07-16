def b64table(index):
    if index <= 25:
        return chr(index + ord('A'))
    elif index <= 51:
        return chr(index - 26 + ord('a'))
    elif index <= 61:
        return chr(index - 52 + ord('0'))
    elif index == 62:
        return '+'
    elif index == 63:
        return '/'

def h2b64(hexin):
    assert(isinstance(hexin,basestring))
    print('in:', hexin)
    out = ''
    assert len(hexin) % 6 == 0
    for itr in range(len(hexin) / 6):
        atom_str = hexin[itr*6:itr*6+6]
        atom_int = int(atom_str[4:6],16) | (int(atom_str[2:4],16) << 8) | (int(atom_str[0:2],16) << 16)
        first = (atom_int >> 18) & 0x3F
        second = (atom_int >> 12) & 0x3F
        third = (atom_int >> 6) & 0x3F
        fourth = (atom_int) & 0x3F
        #print(itr, atom, bin(atom_int), first, second, third, fourth, b64table(first), b64table(second), b64table(third), b64table(fourth))
        out = out + str(b64table(first)) + str(b64table(second)) + str(b64table(third)) + str(b64table(fourth))
    return out


def main():
   print(h2b64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
   #print(h2b64('4d616e'))

if __name__ == "__main__":
    main()
