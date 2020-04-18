# webhacking.kr(old) write-ups

## old-01

쿠키 인젝션  

<code>
  <?php  
    if(!is_numeric($_COOKIE['user_lv'])) $_COOKIE['user_lv']=1;  
    if($_COOKIE['user_lv']>=6) $_COOKIE['user_lv']=1;  
    if($_COOKIE['user_lv']>5) solve(1);  
    echo "<br>level : {$_COOKIE['user_lv']}";  
  ?>  
</code>

쿠키 user_lv의 값을 조건에 맞게 바꿔야 한다.  
쿠키는 5 초과 6 미만인 값이어야 하므로, 그 사이의 값(ex 5.5)을 넣으면 성공.  

![pwned](./pwned/old-01.png)  

## old-02