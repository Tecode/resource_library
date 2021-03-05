#!/bin/sh

# read name 
echo "$name It is a test /n"

echo "\"转义字符"\"

echo -e "OK! \c"

# 显示结果定向至文件
echo "It is a test" > myfile.txt

# 原样输出字符串，不进行转义或取变量(用单引号)
echo '$name\"'

echo `date`