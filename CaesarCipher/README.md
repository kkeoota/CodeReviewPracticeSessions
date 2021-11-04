# CaesarCipherFilter

# 説明
標準入力から受け取ったテキストをアルファベットで記載された Caesar Ciper とみなし、解読を試み、標準出力に書き出します。
明示的に offset を指定した場合は、offset だけずらした文字列を、標準出力に書き出します。

# 使い方
usage: caesarcipherfilter.py [-h] [--offset OFFSET]

## 暗号化
例：
```
cat plain.txt | /usr/local/bin/python3 ./caesarcipherfilter.py --offset -3
wklv lv wkh slfwxuh wkdw l wrrn lq wkh wuls.
wklv lv d shq.
```

## 解読
例：
```
cat ciper_3.txt | /usr/local/bin/python3 ./caesarcipherfilter.py            
this is the picture that i took in the trip.
this is a pen.
```