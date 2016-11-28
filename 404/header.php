<?php
session_start();
include 'include/connection.php';
$query = mysqli_query($conn, "SELECT * FROM admin");
  $row = mysqli_fetch_array($query);
   $userx = $row['user'] ;
    if($userx==$_SESSION['login_user'])
{

}
else
{
  header("location:index.php");
}
?>
<!DOCTYPE html>
<html>
<head>

<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
<script src="js/bootstrap.min.js"></script>
</head>
<body>
<ul class="nav nav-tabs nav-justified">
 



  <li role="presentation" ><a href="501.php">./Home</a></li>
  <li role="presentation"><a href="list.php">./Bots List</a></li>
  <li role="presentation"><a href="sendcmd.php">./Command Center</a></li>
    <li role="presentation"><a href="SucessCmdlist.php">./Command's Output</a></li>
  <li role="presentation"><a href="keylogs.php">./Veiw keylogs</a></li>
<li role="presentation"><a href="ads.php">./ads</a></li>
<li role="presentation"><a href="logout.php">Log Out</a></li>
  

	
</ul>
</nav>

</body>
</html>
