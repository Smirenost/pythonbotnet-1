<?
session_start();
if(isset($_SESSION['login_user'])){
header("location:501.php");
}
?>
<?php

include 'include/connection.php';

?>

<!DOCTYPE html>
<html>
<head>
  <style>

body {
    background-image: url("1747969.jpg");
    
}

  </style>
<title>404 Not Found</title>
<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
<script src="js/bootstrap.min.js"></script>
</head>
<br><br><br><br>
<div class="row">
  <div class="col-md-6 col-md-offset-3"><h1 style="color:#92FAF1 ;font-size:300%">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp [+]K3rn3l R00t</h1>
</div>
<body>
  <br>
<br><br><br>
<form method="post" action="<?php $_SERVER["PHP_SELF"];?>">
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1" style="color:#92FAF1">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp[*]Email</label>
  <input type="email" class="form-control" id="email" name="email">
</div>
<div class="form-group has-warning">
  <label class="control-label" for="inputWarning1" style="color:#92FAF1">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp[*]Password</label>
  <input type="password" class="form-control" id="password" name="password">
</div>
<div class="form-group has-error">
  <label class="control-label" for="inputError1" style="color:#92FAF1">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp[*]Security Number</label>
  <input type="text" class="form-control" id="security" name="security">
</div>

<div class="row">
  <div class="col-md-4"></div>
 &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <div class="col-md-4"><button  class="btn btn-primary btn-lg btn-block" type="submit" name="submit" value="submit">Login</button></div>
  <div class="col-md-4"></div>
</div>

</form>

<?php
$userverified=0;
$passverified=0;
if(isset($_POST["submit"]))
{
$email = $_POST["email"];
$password = $_POST["password"];
$Security = $_POST["security"];

if($Security!= '')
{
 $x = "<h1 style=\"color:#92FAF1\">&nbsp&nbsp&nbsp[+]Waiting For Script Kiddies To Piss OFF [+]</h1>";
  echo $x;
  
}
if($Security== '')
{
  $query = mysqli_query($conn, "SELECT * FROM admin");
  $row = mysqli_fetch_array($query);
   $user = $row['user'] ;
    $PASS = $row['PASS'] ;

     if($email==$user) {
     $userverified=1;
  }
       if($password==$PASS){
     $passverified=1;
  }
    if($userverified==1 and $passverified==1 )
    {
      session_start();
      $_SESSION['login_user']= $user;
     
      header("location:501.php");
    }
    else
    {
 $x = "<h1 style=\"color:#92FAF1\">&nbsp&nbsp&nbsp[+]Waiting For Script Kiddies To Piss OFF [+]</h1>";
  echo $x;
    }
}
}
?>
</body>
</html>
