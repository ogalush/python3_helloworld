#coding: utf_8

## Ref
## https://python.keicode.com/lang/type-string.php


## Python の文字列リテラル
a = 'CA'
print (a)

b = "TX"
print(b)

c = 'ABC\'D' # ' で始まる文字列中で ' を使う
print(c)


## Python の複数行文字列リテラル
msg = '''
Hi,
My name is John Doe.
'''
print(msg)


## Python の文字列の結合と繰り返し
a = 'Hello'
b = 'world'
print(a + ',' + b)

## Python 文字列中の文字へのインデックスアクセス
### 先頭のindex = 0
### 末尾のindex = -1
a = 'Hello'
print(a[0])
print(a[-1])
print(a[1:3])
print(a[:-2]) ## 先頭 - 末尾から2文字前まで

## Python の文字列に使える関数の調べ方
a = 'Hello'
print(len(a)) # aの長さ
print(a.find('e')) # 最初に[e]が表示されるIndex番号
print(a.upper()) # 文字列を大文字へ変換する

## dir関数を用いると、今扱っているオブジェクトのアトリビュートが取得できます。
## print(dir(a)) 

## ビルトイン関数の説明を表示するときは、 help(関数名)すると良い
## help(a.find)

