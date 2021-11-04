import argparse
import sys
from caesarcipher import CaesarCipher

def main(args):
    if args.offset == None:
        for l in sys.stdin:
            cipher = CaesarCipher(l)
            sys.stdout.write(cipher.cracked)
    else:
        for l in sys.stdin:
            cipher = CaesarCipher(l, offset=args.offset)
            sys.stdout.write(cipher.decoded)
    
if __name__ ==  '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--offset', type=int, help='encode with offset')
    args = parser.parse_args()
    main(args)
