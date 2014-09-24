#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2014 François Bianco <francois.bianco@skadi.ch>

Freely distributed under MIT License.
"""

def unicodeToHex(s, prefix='<FEFF ', suffix='>'):
    """Convert the given unicode string to hex encoded string
      with the given pre- and suffix, by default return a
      PDFMARKS encoded string starting with FEFF and enclosed
      with < >.
    """
    return prefix + ' '.join(['{0:04X}'.format(ord(i)) for i in s]) + suffix

def main():
    import argparse

    parser = argparse.ArgumentParser(description=unicodeToHex.func_doc)
    # type, lambda function = Python 2.6+ hack, not required for Py v3.
    parser.add_argument("string", type=lambda s: unicode(s, 'utf8'),
                        help="Unicode string to convert to hexadecimal format")
    parser.add_argument("-p", "--prefix", help="Prefix", default='<FEFF')
    parser.add_argument("-s", "--suffix", help="Suffix", default='>')
    args = parser.parse_args()

    print unicodeToHex(args.string, args.prefix, args.suffix)

if __name__ == '__main__':
    main()
