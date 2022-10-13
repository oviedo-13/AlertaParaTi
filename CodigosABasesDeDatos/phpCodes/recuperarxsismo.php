<?php
// PHP Data Objects(PDO) Sample Code:
try {
    $conn = new PDO("sqlsrv:server = tcp:alerta-para-ti.database.windows.net,1433; Database = alerta-para-ti", "select_login", "#FanaticosDeShrek2000");
    # $cantidad = htmlspecialchars($_GET['cantidad']);
    $statement = $conn->prepare("SELECT * FROM sismo_rows WHERE row# <= 10");

    # $statement->execute(array($cantidad));
    $statement->execute();
    
    $results = $statement->fetchAll(PDO::FETCH_ASSOC);
    $json = json_encode($results);
    echo $json;
}
catch (Error $e) {
    print("Error connecting to SQL Server.");
    die(print_r($e));
}