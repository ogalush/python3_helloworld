#coding: utf_8

## Ref
## https://python.keicode.com/lang/type-numeric.php

from decimal import *

print ('{:d}'.format(0b11)) # 2進数 -> 10進数で表示
print ('{:d}'.format(0o11)) # 8進数 -> 10進数で表示
print ('{:d}'.format(0x11)) # 16進数 -> 10進数で表示

m = 123
print(type(m))


## False
print(0.1 + 0.1 + 0.1 == 0.3)

## True
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3'))