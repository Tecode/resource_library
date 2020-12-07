#!/bin/bash

# 变量
your_name="shell script"

echo "Hello World ! $your_name \n"

echo "第一个参数：$0"
echo "第二个参数：$1"
echo "全部参数：$@ \n"

# 数组
my_array=("你叫什么名字" "哈哈" 3)

# 数组插入数据
my_array[3]=666

echo "第一个元素为: ${my_array[0]}"
echo "第二个元素为: ${my_array[1]} \n"

# 获取数组的长度
echo "数组长度：${#my_array[@]}"

# 运算符
a=10
b=3

val_1=`expr $a + $b`
echo "两数之和：$val_1"

val_2=`expr $a \* $b`
echo "两数之积：$val_2"

val_3=`expr $a / $b`
echo "两数之商：$val_3"

val_4=`expr $a % $b`
echo "两数之余：$val_4"

val_5=`expr $a - $b`
echo "两数减法：$val_5"


# -eq	检测两个数是否相等，相等返回 true。	[ $a -eq $b ] 返回 false。
# -ne	检测两个数是否不相等，不相等返回 true。	[ $a -ne $b ] 返回 true。
# -gt	检测左边的数是否大于右边的，如果是，则返回 true。	[ $a -gt $b ] 返回 false。
# -lt	检测左边的数是否小于右边的，如果是，则返回 true。	[ $a -lt $b ] 返回 true。
# -ge	检测左边的数是否大于等于右边的，如果是，则返回 true。	[ $a -ge $b ] 返回 false。
# -le	检测左边的数是否小于等于右边的，如果是，则返回 true。	[ $a -le $b ] 返回 true。

if [ $a -lt $b ]
then
  echo "a小于b"
fi

if [ $a -gt $b ]
then
  echo "a大于b"
fi



