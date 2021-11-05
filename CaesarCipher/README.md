# CaesarCipherFilter

# 方針
1.  [UNIX哲学](https://ja.wikipedia.org/wiki/UNIX%E5%93%B2%E5%AD%A6)（？）に従い、標準入出力を扱うプログラムを書く。
2. 極力手抜きする。


# 説明
標準入力から受け取ったテキストをアルファベットで記載された Caesar Ciper とみなし、解読を試み、標準出力に書き出します。
オプションにより明示的に offset を指定した場合は、offset だけずらした文字列を、標準出力に書き出します。

# 使い方
usage: caesarcipherfilter.py [-h] [--offset OFFSET]

## 暗号化
### 例：
```
cat plain.txt | /usr/local/bin/python3 ./caesarcipherfilter.py --offset -3
wklv lv wkh slfwxuh wkdw l wrrn lq wkh wuls.
wklv lv d shq.
```

## 解読
### 例1：
```
cat ciper_3.txt | /usr/local/bin/python3 ./caesarcipherfilter.py            
this is the picture that i took in the trip.
this is a pen.
```

### 例2:
the, this, that いずれの単語も含まない暗号文の解読も可能
```
cat ciper2_4.txt | python3 ./caesarcipherfilter.py                            
his name is nobita. he is wareing glasses. he is an elementary school student. he lives in tokyo.
```
## See Also
https://github.com/RobSpectre/Caesar-Cipher