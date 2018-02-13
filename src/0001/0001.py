#!/usr/bin/env python

import string, random

strs = string.ascii_letters + string.digits

def gen_key(length=8):
    return ''.join(random.sample(strs, length))

if __name__ == "__main__":
    with open('./result.txt', 'wt') as f:
        for i in range(200):
            f.write(gen_key()+'\n')