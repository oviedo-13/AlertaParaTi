<?php
// PHP Data Objects(PDO) Sample Code:
try {
    $conn = new PDO("sqlsrv:server = tcp:alerta-para-ti.database.windows.net,1433; Database = alerta-para-ti", "select_login", "#FanaticosDeShrek2000");
    
    # $fecha = htmlspecialchars($_GET['fecha']);
    $statement = $conn->prepare("SELECT id, 
    cast(ROUND(temperatura, 0) as int) AS temperatura, 
    porcentaje_lluvia, cast(indice_UV as DECIMAL(9, 1)) as indice_UV, 
    calidad_aire, fecha, CONCAT(DATEPART(HOUR, fecha), ':00') AS hora, 
    CAST((SELECT TOP 1 temperatura FROM clima WHERE FORMAT(fecha, 'yyyy-MM-dd') = format(dateadd(hour, -5, GETDATE()), 'yyyy-MM-dd') ORDER BY temperatura DESC) AS DECIMAL(9,1)) AS temperatura_maxima, 
    CAST((SELECT TOP 1 temperatura FROM clima WHERE FORMAT(fecha, 'yyyy-MM-dd') = format(dateadd(hour, -5, GETDATE()), 'yyyy-MM-dd') ORDER BY temperatura ASC) AS DECIMAL(9,1)) AS temperatura_minima 
    FROM clima 
    WHERE FORMAT(fecha, 'yyyy-MM-dd HH') = format(dateadd(hour, -5, GETDATE()), 'yyyy-MM-dd HH')");
    
    # $statement->execute(array($fecha));
    $statement->execute();
    $results = $statement->fetchAll(PDO::FETCH_ASSOC);
    $json = json_encode($results);
    echo $json;
}
catch (PDOException $e) {
    print("Error connecting to SQL Server.");
    die(print_r($e));
}