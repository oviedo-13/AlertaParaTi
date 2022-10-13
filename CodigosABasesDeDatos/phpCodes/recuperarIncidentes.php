<?php
// PHP Data Objects(PDO) Sample Code:
try {
    $conn = new PDO("sqlsrv:server = tcp:alerta-para-ti.database.windows.net,1433; Database = alerta-para-ti", "alerta-para-ti", "#teamdinamica2022");
    $fecha_inicial = htmlspecialchars($_GET['fecha_inicial']);
    $fecha_inicial_completa = $fecha_inicial . ' 00:00:00';
    $fecha_termino = htmlspecialchars($_GET['fecha_termino']);
    $fecha_termino_completa = $fecha_termino . ' 23:59:59';
    $id_tipo_incidente = htmlspecialchars($_GET['id_tipo_incidente']);
    if ($id_tipo_incidente == '') {
        $statement = $conn->prepare("
        SELECT incidentes.id, incidentes.tipo_id, tipo_incidente, tiempo_inicio, tiempo_final, desde_lugar, hasta_lugar, longitud_metros 
        FROM incidentes 
        INNER JOIN incidentes_tipos 
        ON incidentes.tipo_id = incidentes_tipos.id 
        WHERE tiempo_inicio BETWEEN ? 
        AND ?
        ORDER BY tiempo_inicio DESC");
    } else {
        $statement = $conn->prepare("
        SELECT incidentes.id, incidentes.tipo_id, tipo_incidente, tiempo_inicio, tiempo_final, desde_lugar, hasta_lugar, longitud_metros 
        FROM incidentes 
        INNER JOIN incidentes_tipos 
        ON incidentes.tipo_id = incidentes_tipos.id 
        WHERE tiempo_inicio BETWEEN ?
        AND ?
        AND incidentes_tipos.id = ?
        ORDER BY tiempo_inicio DESC");
    }
    $statement->execute(array($fecha_inicial_completa, $fecha_termino_completa, $id_tipo_incidente));
    $results = $statement->fetchAll(PDO::FETCH_ASSOC);
    $json = json_encode($results);
    echo $json;
}
catch (PDOException $e) {
    print("Error connecting to SQL Server.");
    die(print_r($e));
}