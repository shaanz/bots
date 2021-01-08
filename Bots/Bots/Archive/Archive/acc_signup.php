
<html>
<body>


<div id="print">

</div>

<?php
/*
$fn = fopen("credlist.txt","r");


while(! feof($fn))  {
    $line = fgets($fn);
   // echo $line;



    $line=trim($line);

     $strArrMain = (explode(",",$line));



    $username=trim($strArrMain[0]);
    $pass=trim($strArrMain[1]);

    echo $username."<br>";
    echo $pass."<br>";
*/


$url = 'https://airline.f5se.com/user/signup';
$i=0;


$fn = fopen("challenge_signup.csv","r");

$ch = curl_init();

while(! feof($fn)) {

    $i++;
    $line = fgets($fn);
// echo $line;


    $line = trim($line);

    $strArrMain = (explode(",", $line));


    $userid = trim($strArrMain[0]);
    $password = trim($strArrMain[3]);
    $userid=trim($userid);
    $password=trim($password);


    $useridasli=$userid;
    $passwordasli=$password;

     $userid=urlencode($userid);
     $password=urlencode($password);


     $post="first_name=".$userid."&last_name=".$userid."&phone=123456&email=".$userid."&password=Admin123&confirm=Admin123";






    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 0);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/x-www-form-urlencoded, Host:airline.f5se.com'));


    if(curl_exec($ch) === false)
    {
        echo 'Curl error: ' . curl_error($ch);
    }
    $errors = curl_error($ch);
    $result = curl_exec($ch);
    $returnCode = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);


    if(strpos($result, 'linked'))
    {
        echo '<br>';
        echo $i;echo '<br>';
        echo $useridasli;
        echo '<br>';

    }



}









fclose($fn);

?>


</body>
</html>
