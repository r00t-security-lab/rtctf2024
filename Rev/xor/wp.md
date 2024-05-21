打开ida按一下f5可以看到伪代码，分析一下，整个加密流程就是异或0x19

解题脚本：

```python
enc="k))m+)+-bA)kF(jFj)Fpwm*k*jmpw~88888d"
for i in enc:
    print(chr(ord(i)^0x19),end='')
```

