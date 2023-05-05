#coding: utf_8

## Ref
## https://python.keicode.com/lang/type-tuple.php

## Tuple (タプル) というのは、「複数のオブジェクトをひとつにまとめたもの」 ということができます。
## タプルは ( ) で括って記述します。
## , 区切りでデータを並べることで、タプルとすることができます。(=()を省略する事も可能.)

## 例
A = ('John', 37)
print(A)

## Tupleの複製
x = A
print(x)

## Tupleの代入
a, b = A  ## key, valueのような形で代入される
print(a)
print(b)

## , 区切りでデータを並べることで、タプルとすることができます。
A = 'John', 37
print(A)

A = 'John', # 文字列一個だけのタプルを作るなら、最後に , を付ければ OK
print(A)


## ListとTupleの違い.
## TupleはListと違い、要素の代入をすることができない.
## print(A[0])
## A[0] = 'ABC'
"""
Traceback (most recent call last):
  File "/Users/ogalush/Documents/github/python3_helloworld/type-tuple.py", line 34, in <module>
    A[0] = 'ABC'
    ~^^^
TypeError: 'tuple' object does not support item assignment
"""