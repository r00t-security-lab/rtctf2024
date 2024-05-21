# broken_flag

在主函数中是对flag的第一部分的加密，就是一个简单的字母移位操作，由于未设定随机数种子，会采用默认的种子，可以直接跑一下获取随机数的值

继续向下看可以看到一个tips函数，会提示看一下奇怪的字符串和交叉引用，这两种方法都能找到第二部分

![Snipaste_2024-05-21_09-45-09](broken_flag.assets\Snipaste_2024-05-21_09-45-09.png)

就能找到第二部分了，第二部分的加密是对每一位异或0x24

第三部分的线索就要看字符串了，可以看到在函数fun11_()中，在旁边搜索函数列表，可以搜到几个函数名满足条件的，依次查看就行

![Snipaste_2024-05-21_09-43-53](broken_flag.assets\Snipaste_2024-05-21_09-43-53.png)

![Snipaste_2024-05-21_09-36-01](broken_flag.assets\Snipaste_2024-05-21_09-36-01.png)

在fun114()中找到了不一样的东西，进入Th3_8r0kEn_flag函数，里面是一句话，意思就是这个函数名很奇怪，发现是符合flag的常用格式的，这个函数名就是第三部分了



脚本：

```
#include<iostream>
#include<cstdlib>
using namespace std;
int main(){
    string p1 = "es4sZ_N0J_UDc_";
    int v6 = rand() %26;
    int v5 = 26-v6;
    for (int i=0;i<14;i++){
        if(p1[i]>='a'&&p1[i]<='z'){
            p1[i] = (p1[i] - 97 - v5 + 26) % 26 + 97;
        }
        if(p1[i]>='A'&&p1[i]<='Z'){
            p1[i] = (p1[i] - 65 - v6 + 26) % 26 + 65;
        }
        cout << p1[i];
    }
    int p2[] = {0x11, 0x51, 0x47, 0x67, 0x61, 0x57, 0x11, 0x62, 0x51, 0x15, 
  0x48, 0x7D, 0x7B, 0x42, 0x15, 0x5C, 0x05, 0x6A, 0x43, 0x7B};
    for(int i=0;i<20;i++){
        p2[i] ^= 0x24;
        cout << (char)p2[i];
    }

}
```

flag：r00t2024{th4hK_Y0U_FOr_5ucCEs5Fu1lY_f1x!Ng_Th3_8r0kEn_flag}