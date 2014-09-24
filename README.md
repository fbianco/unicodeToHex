unicodeToHex
============

Convert unicode string to hexadecimal in pdfmarks format

```
usage: unicodeToHex.py [-h] [-p PREFIX] [-s SUFFIX] string

Convert the given unicode string to hex encoded string with the given pre- and
suffix, by default return a PDFMARKS encoded string starting with FEFF and
enclosed with < >.

positional arguments:
  string                Unicode string to convert to hexadecimal format

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        Prefix
  -s SUFFIX, --suffix SUFFIX
                        Suffix
```