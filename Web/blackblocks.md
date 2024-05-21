打开题目发现是一个别踩白块的游戏，提示10000分就给Flag

> 如果能手打当然也可以

F12查看源码发现我们的得分是可以修改的

```javascript
function fail(){
	clearInterval(clock);
	flag = false;
	alert('你的最终得分 '+parseInt($('score').innerHTML));
	if(parseInt($('score').innerHTML)>10000){
		var myscore=parseInt($('score').innerHTML)
		var xhr = new XMLHttpRequest();
        xhr.open("POST", "api.php", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        var data = {
            score: myscore,
        };
        xhr.send(JSON.stringify(data));
		var response = JSON.parse(xhr.responseText);
        alert(response.message);
	}
	var con = $('con');
	con.innerHTML = "";
	$('score').innerHTML = 0;
	con.style.top = '-408px';
}
```

代码逻辑很简单，当我出错了就会从html中拿取分数，以post方式（json格式）向api.php发送post请求，然后返回相应。

那么解法就很多了

+ 解1：直接传json数据给api.php

  `{"score":1000000}`方式为application/json（hackbar）

  ![image-20240521132826800](img\image-20240521132826800.png)

+ 解2：修改html中的数据，在进入函数的地方下断点，当停止运行时将html中表示分数的地方改为1000000

<img src="img\image-20240521133338116.png" alt="image-20240521133338116" style="zoom: 67%;" />

​	也可以在if前下

<img src="img\image-20240521133438978.png" alt="image-20240521133438978" style="zoom: 80%;" />

<img src="img\image-20240521134332035.png" alt="image-20240521134332035" style="zoom:50%;" />

