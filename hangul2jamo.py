# -*- coding: utf8 -*-

def hangul2jamo(uchar):
    HANGUL_BASE = 0xac00
    HANGUL_END  = 0xd7a4
    LEAD_BASE = 0x1100
    VOWEL_BASE = 0x1161
    TAIL_BASE = 0x11A7

    cp = ord(uchar)

    if not ( HANGUL_BASE <= cp <= HANGUL_END):
        return uchar
    
    idx = cp - HANGUL_BASE
    tail = idx % 28
    idx = idx / 28
    vowel = idx % 21
    idx = idx / 21
    lead = idx % 19

    jamos = (unichr(lead + LEAD_BASE), unichr(vowel + VOWEL_BASE), unichr(tail + TAIL_BASE) if tail > 0 else '')
    
    return jamos

if __name__ == '__main__':
    s = u'다들어와담엔누구차례'
    for c in s:
        print c, '=>', ' '.join(hangul2jamo(c))
            
