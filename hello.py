#coding: utf_8

## Visual Studio Code を使用して Python 初心者向けの開発環境をセットアップする
## https://docs.microsoft.com/ja-jp/learn/modules/python-install-vscode/


print("HelloWorld おがらっしゅ\n")

## 練習
## https://www.javadrive.jp/python/if/index1.html#section1
old = 20
boarder = 10
if old > boarder:
    print ("%d 歳よりも年上です" % boarder)
else:
    print ("%d 歳よりも年下です" % boarder)
print("\n")

## 1文字ずつprintしていく
## https://atmarkit.itmedia.co.jp/ait/articles/1905/10/news023.html
message = 'Hello Python'
for ch in message:
     print(ch)
print ("\n")

## 0..100
## range() https://www.javadrive.jp/python/function/index6.html#section1
## range(stop)
## range(start, stop[, step]) 
for i in range(0,100,2):
    print(i)
print ("\n")
