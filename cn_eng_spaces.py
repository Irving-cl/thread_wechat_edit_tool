#!/usr/bin/env python
from enum import Enum
import sys

Char_Type = Enum('Chat_Type', ('NONE', 'EN', 'CN', 'NU'))

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False

def is_number(uchar):
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False

def get_type(uchar):
    if is_chinese(uchar):
        return Char_Type.CN
    elif is_alphabet(uchar):
        return Char_Type.EN
    elif is_number(uchar):
        return Char_Type.NU
    else:
        return Char_Type.NONE

# Add spaces between English words and Chinese,
# or numbers and Chinese
def add_spaces(line):
    ret = ''
    tmp = unicode(line, 'utf8')
    last_char_type = Char_Type.NONE;
    for char in tmp:
        cur_char_type = get_type(char)
        if cur_char_type == Char_Type.CN:
            if last_char_type == Char_Type.NU or last_char_type == Char_Type.EN:
                ret += ' '
        elif cur_char_type == Char_Type.NU or cur_char_type == Char_Type.EN:
            if last_char_type == Char_Type.CN:
                ret += ' '
        ret += char
        last_char_type = cur_char_type
    return ret

def main(argv):
    if len(argv) != 2:
        print 'Usage: python cn_eng_spaces.py [input_file] [output_file]'
        return
    in_file = open(argv[0], 'rU')
    out_file = open(argv[1], 'w')
    try:
        i = 0
        for line in in_file:
            i = i + 1
            out_file.write(add_spaces(line).encode('utf-8'))
    finally:
        in_file.close()
        out_file.close()

if __name__ == "__main__":
    main(sys.argv[1:])

