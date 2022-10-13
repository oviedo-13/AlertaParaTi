<?php
// PHP Data Objects(PDO) Sample Code:
try {
    $conn = new PDO("sqlsrv:server = tcp:alerta-para-ti.database.windows.net,1433; Database = alerta-para-ti", "select_login", "#FanaticosDeShrek2000");
    $id_incidente = htmlspecialchars($_GET['id_incidente']);
    $statement = $conn->prepare("SELECT id, longitud, latitud FROM incidentes_coordenadas where id_incidente = ?");
    $statement->execute(array($id_incidente));
    $results = $statement->fetchAll(PDO::FETCH_ASSOC);
    $json = json_encode($results);
    echo $json;
}
catch (PDOException $e) {
    print("Error connecting to SQL Server.");
    die(print_r($e));
}