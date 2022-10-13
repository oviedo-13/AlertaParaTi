<?php
// PHP Data Objects(PDO) Sample Code:
try {
    $conn = new PDO("sqlsrv:server = tcp:alerta-para-ti.database.windows.net,1433; Database = alerta-para-ti", "insert_login", "#FanaticosDeShrek2000");
    $fecha_inicio = htmlspecialchars($_GET['fecha_inicio']);
    $hora_inicio = htmlspecialchars($_GET['hora_inicio']);
    
    $fecha_completa_inicio = $fecha_inicio . ' ' . $hora_inicio;
    $fecha_fin = htmlspecialchars($_GET['fecha_fin']);
    $hora_fin = htmlspecialchars($_GET['hora_fin']);
    
    $fecha_completa_fin = $fecha_fin . ' ' . $hora_fin;
    $statement = $conn->prepare("INSERT INTO sesiones VALUES (?, ?)");
    if(!$statement->execute(array($fecha_completa_inicio, $fecha_completa_fin))){
        echo 'error';
    } else{
        echo 'dato insertado';
    }
}
catch (PDOException $e) {
    print("Error connecting to SQL Server.");
    die(print_r($e));
}