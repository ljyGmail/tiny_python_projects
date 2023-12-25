#!/usr/bin/env python3
"""
Author : macbookpro16 <macbookpro16@localhost>
Date   : 2023-12-25
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    jumper = {'1': '9',
              '2': '8',
              '3': '7',
              '4': '6',
              '5': '0',
              '6': '4',
              '7': '3',
              '8': '2',
              '9': '1',
              '0': '5'}

    for char in text:
        print(jumper.get(char, char), end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
