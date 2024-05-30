# 5num_secret.jpg

题目提示密码是 5 位的数字，放进 binwalk 分离，可以看到有个 zip 文件，或者 010 看到末尾的 zip 标志，分离出来，有密码，可以用 kali 自带的 fcrackzip 进行解密

`fcrackzip -b -c '1' -l 5-5 -u 1DCDF7.zip` 或者其他方式爆破出来密码，密码是 `12138` ，爱情公寓忠实粉丝