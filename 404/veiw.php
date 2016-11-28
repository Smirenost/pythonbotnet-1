<?php
if(isset($_POST["id"]))
{
$postid = $_POST["id"];

}
?>


?>
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
<script src="js/bootstrap.min.js"></script>
	<title>Veiw</title>
</head>
<body>
<?php
include 'header.php'
?>
    <div class="table-responsive">
  <table class="table" border="5" BORDERCOLOR=#92FAF1>
      <tr>
    <th>id</th>
    <th>BOT ID</th> 
    <th>COMMAND</th>
    <th>STATUS</th>
    <th>OUTPUT</th> 
    <th>DATE/TIME</th>
    <th>PARAMETER 1</th>
    <th>PARAMETER 2</th>
    <th>PARAMETER 3</th> 
   
</tr>


<?php
 $query = mysqli_query($conn, "SELECT * FROM cmd Where uid='$postid' ");
  while ($row = mysqli_fetch_array($query))
  	# code...
  {
  	 
  $id = $row['id'];
   $uid = $row['uid'];
    $command = $row['command'];
     $status = $row['statu$'];
      $OUtput = $row['OUtput'];
       $datetime = $row['datetime'];
        $Para1 = $row['Para1'];
         $Para2 = $row['Para2'];
         $Para3 = $row['para3'];
          
?>



  
 
  <tr>
    <td><?php echo $id ?></td>
    <td><?php echo $uid ?></td> 
    <td><?php echo $command ?></td>
    <td><?php echo $status ?></td>
    <td><?php echo $OUtput ?></td>
    <td><?php echo $datetime ?></td> 
    <td><?php echo $Para1 ?></td>
    <td><?php echo $Para2 ?></td>
     <td><?php echo $Para3 ?></td>
    
    
  </tr>

<?php         
}
    ?>
      </table>
</div>
</body>
</html>
