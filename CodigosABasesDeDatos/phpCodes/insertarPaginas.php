<?php
// PHP Data Objects(PDO) Sample Code:
try {
    $conn = new PDO("sqlsrv:server = tcp:alerta-para-ti.database.windows.net,1433; Database = alerta-para-ti", "insert_login", "#FanaticosDeShrek2000");
    $pagina = htmlspecialchars($_GET['pagina']);
    $hora = htmlspecialchars($_GET['hora']);
    $fecha = htmlspecialchars($_GET['fecha']);
    
    $fecha_completa = strval($fecha) . ' ' . strval($hora);

    $statement = $conn->prepare("INSERT INTO paginas (pagina, fecha) VALUES (?, ?)");
    if(!$statement->execute(array($pagina, $fecha_completa))){
        echo 'error';
    } else{
        echo 'dato insertado';
    }
}
catch (PDOException $e) {
    print("Error connecting to SQL Server.");
    die(print_r($e));
}