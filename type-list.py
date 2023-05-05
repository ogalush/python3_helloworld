#coding: utf_8

## Ref
## https://python.keicode.com/lang/type-list.php

## Python のリストの基本操作
L = [2,4,6,8,10]

print(L[1])
print(L[1:3])

## リストの結合
M = L + [1,3,5] ## リストは+を使用して結合出来る.

## Sort前の状態確認
print(M)

## Sort実施
M.sort()

## Sort後の状態確認
print(M) ## sort後の結果が表示される

## リスト末尾への追加
M.append(100)
print(M)

## リスト末尾からの取り出し
print(M.pop())
print(M)

## リストの要素数
print(len(M))

## リストの中の指定した要素の数を返す.
print([1,1,1,2,3,4,4,5].count(1))
print([1,1,1,2,3,4,4,5].count(4))

## 同じ配列の中に異なる型を配置することが可能. (PerlやPHPとはちょっと違う)
L = [ 1, 'Hello', 3.14 ]
print(L[1])
print(L[1][1]) ## 配列の要素番号1の1(Stringの2文字目)を抽出する.

## オブジェクトリテラルを配列の要素に含む場合
N = [[1,2,3], 'Hello', {'name':'John Doe','age':37}]
print(N[0])
print(N[2])
print(N[2]['name']) ## プロパティ名でオブジェクトの値にアクセスできます


## リストの内包表記 (Comprehensions)
L = [1,2,3,4,5]

### リスト L の 2 より大きな値を持つ要素のみからなるリストを作る
print([x for x in L if x > 2])
### 通常の書き方
array_x = []
for x in L:
    if x > 2:
        array_x.append(x)
print(array_x)

### 上記の要素をそれぞれ 3 倍するなどの操作を加える場合
print([3*x for x in L if x > 2])


## 文字列へも適用出来るとのこと
L = ['hello','world']
print([x.upper() for x in L])

## 通常の書き方
array_x = []
for x in L:
        array_x.append(x.upper())
print(array_x)
