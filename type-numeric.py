#coding: utf_8

## Ref
## https://python.keicode.com/lang/type-numeric.php

from decimal import *

'{:d}'.format(0b11) # 10進数で表示
'{:d}'.format(0o11)
'{:d}'.format(0x11)


m = 123
type(m)


## False
0.1 + 0.1 + 0.1 == 0.3

## True
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3')