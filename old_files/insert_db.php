<?php

require_once "Zend/Json.php";
function get_all_info() {
	$fp = file_get_contents("buildings.json");
	$zj = Zend_Json::decode($fp);

	$url = "http://gtalumni.org/map/mapquery.php?type=id&value=";

	$json_arr = array();
	foreach ($zj as $b) {
		$bstuff = file_get_contents($url.$b['bId']);
		try {
			$zd = Zend_Json::decode($bstuff);
		} catch (Zend_Json_Exception $zje) {
		}
		if (count($zd) == 1) {
			$temp = $zd[0];
			array_push($json_arr, $temp);
		}
	}

	$ze = Zend_Json::encode($json_arr);
	file_put_contents("full_buildings.json", $ze);
}

function insert_into_db() {
	include_once("Zend/Db.php");
	require_once("Zend/Db/Table.php");
	require_once("../db_config.php");

	$params = array("host" => $db_host, "username" => $db_username, "password" => $db_password, "dbname" => "gtplaces");
	$db = Zend_Db::factory("Pdo_Mysql", $params);

	class Buildings extends Zend_Db_Table_Abstract {
		protected $_name = "buildings";
	}

	$building = new Buildings(array("db" => $db));

	$fp = file_get_contents("full_buildings.json");
	$zd = Zend_Json::decode($fp);
	foreach ($zd as $row) {
		$temp_row = array(
				'b_id' => $row['bId'], 
				'name' => $row['name'], 
				'address' => ($row['address'] == NULL) ? "No Address Given" : $row['address'], 
				'image_url' => ($row['image'] == NULL) ? "" : $row['image'], 
				'longitude' => $row['longitude'], 
				'latitude' => $row['latitude']
				);
		try{
			$building->insert($temp_row);
		}catch (Exception $pe) {
			var_dump($temp_row);
		}
	}

	foreach ($stmt->fetchAll() as $row) {
		var_dump($row);
	}
}
?>
