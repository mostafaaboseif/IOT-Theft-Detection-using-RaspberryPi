<html>
<head>
        <link rel="stylesheet" type="text/css" href="Style.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
    </head>
<body style= "background-color: black; color:white; background-image:url(safe.jpg); background-size: 100%;">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <a class="navbar-brand" href="#" style="color:Gainsboro;">Stay Safe <i class="fas fa-home"></i></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Theft Dection <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/PHP/owners.php">House Owners</a>
      </li>
    </ul>
  </div>
</nav>
<h3 style="margin-left:5%; font-family: Impact, Charcoal, sans-serif; margin-top:2%;"></h3>
<?php
$db=mysqli_connect('localhost', 'pi', 'ansary','IOT');
//if($db)
//   echo "You're connected to the db ";

$name = "ibrahim";
$date = "date";
$img = 'ay7aga3.jpeg';

$imgData = addslashes(file_get_contents($img));

//$sql = "INSERT INTO `Videos`(`name`, `date`, `image`) VALUES('$name', '$date', '$imgData');";
//$sql = "UPDATE `Videos` SET `name`='$name',`date`='$date',`image`='$imgData' WHERE name = '$name';";
$sql = "UPDATE `Videos` SET `name`='$name',`date`='$date',`image`='$imgData' WHERE `name`='$name';";
$query = mysqli_query($db, $sql);
//if($query)
//    echo ".";

$imagread = "SELECT * FROM Videos WHERE `name` = '$name' LIMIT 1;";
$result = mysqli_query($db, $imagread);
$row = mysqli_fetch_array($result);
//if($result)
//    echo ".";

echo ' <div class="card" style="width: 30rem; border: 3px solid #287eff; margin-left:5%; background-color:Gainsboro;">
<div class="caption"><h3><img class="card-img-top" style=" width:100%; " src="data:image/jpeg;base64,'.base64_encode($row['image']).'"/>'. '</h3></div>
</div>   ';
?>
</body>
</html>
