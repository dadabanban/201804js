<?php
session_start();
error_reporting(E_ALL);
date_default_timezone_set("PRC");
header("Content-Type: text/html; charset=UTF-8");
include "ini.php";
//版权：胡老师
//作者：胡老师
//网址：www.taomiss.top

?>
<!DOCTYPE html>
<html lang="zh-cn">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=100%, initial-scale=1"/>
  <title>胡老师VIP视频解析站</title>
  <link rel="shortcut icon" href="images/tx.png">
  <meta name="keywords" content="<?php echo $ini['keywords']?>" />
  <meta name="description" content="<?php echo $ini['description']?>" />
  <link href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet"/>
  <script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
  <script src="//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  <script src="public/js/jquery-1.7.2.min.js"></script>
  <script type="text/javascript">eval(function(p,a,c,k,e,d){e=function(c){return(c<a?"":e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)d[e(c)]=k[c]||e(c);k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('b a(){0 6=1.2("9").4;0 5=1.2("3");0 3=1.2("3").c;0 8=5.e[3].4;0 7=1.2("f");7.d=8+6}',16,16,'var|document|getElementById|jk|value|jkurl|diz|cljurl|jkv|url|dihejk|function|selectedIndex|src|options|player'.split('|'),0,{}))</script>
  <script type="text/javascript">var OriginTitile = document.title;
      var titleTime;
      document.addEventListener('visibilitychange',
      function() {
        if (document.hidden) {
          document.title = 'φ(>ω<*) 这有好东西哦~ ' + OriginTitile;
          clearTimeout(titleTime);
        } else {
          document.title = '( • ̀ω•́ )✧恭喜你发现了~ ' + OriginTitile;
          titleTime = setTimeout(function() {
            document.title = OriginTitile;
          },
          2000);
        }
      });</script>
  </head>
<body style="background: url(&quot;./images/bj.jpg&quot;);">
  <div class="col-xs-12 col-sm-10 col-md-8 col-lg-8 center-block" style="float: none;">
  <h2 class="text-muted" style="color:black" align="center"><strong>胡老师VIP视频解析站</strong></h2>
  <center>
   <span style="color:blue"><marquee behavior="scroll"><strong>
   公告：1.部分地区用户不能使用（不是我的锅，绝对是接口的锅）；2.使用前请先看接口可用情况；3.若接口有失效或者您有新接口，可联系我
   </strong>
   </marquee>
   </span>
  </center>
  
<form action="http://kan.sogou.com/search" target="_blank">
 <div align="center"> 
  <table bgcolor="#87CEEB"> 
   <tr>
    <td> 
     <div class="input-group" style="width: 100%;">
      <input class="form-control input-lg" type="text" placeholder="全网视频搜索"name=keyword size=30">  
	  <span class="input-group-addon input-lg" style="width: 80px;">
	  <button id="bf" type="submit" value="">搜索</button>
	  </span>
     </div>

    </td>
   </tr> 
  </table> 
 </div> 
</form>

<hr>
 <thead>
	<tr>
	    <a target="_blank" href="http://www.bilibili.com/video/av8588155" class="btn btn-default btn-sm"><span class="glyphicon glyphicon-thumbs-up"></span>本网站使用方法</a>
		<a target="_blank" href="/vip/ff.html" class="btn btn-default btn-sm"><span class="glyphicon glyphicon-thumbs-up"></span>磁力链使用方法</a>
		<a target="_blank" href="http://www.adtchrome.com" class="btn btn-default btn-sm"><span class="glyphicon glyphicon-thumbs-up"></span>去广告（电脑）</a>
		<a target="_blank" href="/vip/jiexi.html" class="btn btn-default btn-sm"><span class="glyphicon glyphicon-thumbs-up"></span>解析失败解决方法</a>
	</tr>
 </thead>
 <table class="table table-bordered">
  <tbody>
	<div class="col-md-14 column">
    <div class="panel panel-default">
    <div id="kj" class="panel-body">
    <iframe src="./public/vip_js/index.htm" id="player" width="100%" height="450px" allowtransparency="true" frameborder="0" scrolling="no"></iframe>
    </div>
    </div>
    </div>
    <td>
    <table bgcolor="#87CEEB">
    <div class="col-md-14 column">
    <form method="get" >
	<div class="col-md-5 column" style="margin-top: 2px;">
    <div class="input-group" style="width: 100%;">
	<span class="input-group-addon input-lg" style="width: 80px; ">接口</span>
    <select class="form-control input-lg" id="jk">
	<option value="http://api.47ks.com/webcloud/?v="  style="color:red">1号通用接口👍</option>
	<option value="http://v.72du.com/api/?url=" style="color:red">2号通用接口👍</option>
	<option value="http://qtzr.net/s/?qt=">3号通用接口</option>
	<option value="http://000o.cc/jx/ty.php?url=">4号通用接口</option>
	<option value="http://yyygwz.com/index.php?url=">5号通用接口</option>
	<option value="http://www.wmxz.wang/video.php?url=">6号通用接口</option> 
	<option value="http://yun.zihu.tv/play.html?url=">7号通用接口</option>
	<option value="http://www.vipjiexi.com/yun.php?url=">8号通用接口</option>
	<option value="https://jxapi.nepian.com/ckparse/?url=">9号通用接口</option>
	<option value="http://2gty.com/apiurl/yun.php?url=">10号通用接口</option>
	<option value="http://v.m3l.net/vip/?url=">11号通用接口</option>
	<option value="http://www.chepeijian.cn/jiexi/vip.php?url=">12号通用接口</option>
	<option value="https://apiv.ga/magnet/">万能磁力链接解析</option>
	<option value="http:// ">更多接口待添加...</option></select>
    </div>
	</div>
    <div class="col-md-5" style="margin-top: 2px;">
    <div class="input-group" style="width: 100%;">
    <input class="form-control input-lg" type="search" placeholder="输入需要会员的视频播放地址" id="url">
    </div></div>
    <div class="col-md-2" style="margin-top: 2px;">
    <button id="bf" type="button" class="btn btn-success btn-lg btn-block" onclick="dihejk()">播放</button>
    </div>
    </div>
    </form>
    </div>
	</table> 
   </td> 
    </tbody>
    </table>
    <table class="table table-bordered">
	<thead>
	<div class="alert alert-success alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
  <strong>
  
		
  </strong></div>
</thead>
<?php include "qk.php";?>

<?php include "chuangkou.php";?>
<script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1261247377'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s11.cnzz.com/z_stat.php%3Fid%3D1261247377%26online%3D1%26show%3Dline' type='text/javascript'%3E%3C/script%3E"));</script>
</body>
</html>

