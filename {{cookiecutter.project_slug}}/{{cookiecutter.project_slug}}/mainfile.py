# -*- coding: utf-8 -*-

import argparse
import sys

#
# DEFINE YOUR FUNCTIONS HERE...
#

def foo1(args):
    print(args.a * args.b)

def foo2(args):
    print(args.z)


    
def main():

    '''Console script'''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_foo1 = subparsers.add_parser('foo1')
    # An argument without - is required
    parser_foo1.add_argument('a', type=int, default=1, help='First Intiger')
    # An argument with - is optional
    parser_foo1.add_argument('-b', type=float, default=2, help='Second Float')
    parser_foo1.set_defaults(func=foo1)

    parser_foo2 = subparsers.add_parser('foo2')
    parser_foo2.add_argument('-z', type=int, default=1)
    parser_foo2.set_defaults(func=foo2)
    
    if len(sys.argv) <=1:
        sys.argv.append('--help')

    # Show help if no arguments are given
    args = parser.parse_args()
    args.func(args)
    
    
if __name__ == "__main__":
    main()
