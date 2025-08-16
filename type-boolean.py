#coding: utf_8

## Ref
## https://python.keicode.com/lang/type-boolean.php

a = True
print(a)


import random

# ダミーの関数
# - ランダムな数字を作り、それが 0.5よりも大の時 True
# - それ以外の場合に False としている
def doSomething():
    v = random.random()
    if v > 0.5:
        return True
    else:
        return False

# 変数 a は関数を呼び出した結果を保持
a = doSomething()

if a:
    print('a is True')
else:
    print('a is False')