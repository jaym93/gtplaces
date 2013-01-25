<?php
require_once("Zend/Json.php");
include_once("Zend/Db.php");
require_once("Zend/Db/Table.php");
include_once("db_config.php");

function fb($param,$name){
	//Had to disable
}

$params = array("host" => $db_host, "username" => $db_username, "password" => $db_password, "dbname" => $db_database);
$db = Zend_Db::factory("Pdo_Mysql", $params);

class Buildings extends Zend_Db_Table_Abstract {

	protected $_name = "Building";

	public function getIdsNames() {
		$select = $this->select()->from($this, array("GTB_BUILDING_NUMBER", "GTB_NAME"));
		$row_values = array();
		foreach ($this->fetchAll($select) as $row) {
			array_push($row_values, $row->toArray());
		}
		fb($row_values, "IdNames");
		$ze = Zend_Json::encode($row_values);
		return $ze;
	}


	public function getAllCols($arr) { 

		//takes an array of columns through arr
		// GTB_BUILDING_NUMBER,GTB_NAME,GTB_ADDRESS,latitude,longitude
		//the select statements below

		$select = $this->select()->from($this, $arr);

		$row_values = array();
		//fetch each row
		foreach ($this->fetchAll($select) as $row) {

			array_push($row_values, $row->toArray());
		}
		$ze = Zend_Json::encode($row_values);
		return $ze;
	}

	public function getAll() {
		$row_values = array();
		foreach ($this->fetchAll() as $row) {
			array_push($row_values, $row->toArray());
		}
		$ze = Zend_Json::encode($row_values);
		echo $ze;
	}

	public function getRow($bid) {
		$select = $this->find($bid);
		$ze = Zend_Json::encode($select->getRow()->toArray());
		return $ze;
	}

}

class Tags extends Zend_Db_Table_Abstract {
	protected $_name = "tags";
	protected $_primary = array('GTB_BUILDING_NUMBER', 'tag_name');
}

$building = new Buildings(array("db" => $db));
$tag = new Tags(array("db" => $db));

function getNames() {
	global $building;
	echo $building->getIdsNames();
}

function getUser($columns) {
	global $building;
	if (isset($columns)) {
		$cols = explode(",", $columns);
		echo $building->getAllCols($cols);
	}
}

/*
 Added by Janani Narayanan
 *************************
 Returns a list of building ids and tag names associated with a 
 building.Buildings and Tags have a many to many relationship.
 The sql statement returns all tags ordered in ascending order
 of building id.The conditional statement in for loop checks if 
 a tag belongs to a new building or same building as previous 
 row and consolidates tags belonging to the same building by 
 pushing them into array $row_values.
 */
function getBuildingsTags() {
	global $db;
	$rvals = $db->select()->from("tags", array("GTB_BUILDING_NUMBER","tag_name"))->order("GTB_BUILDING_NUMBER ASC");

	$stmt = $rvals->query();
	$row_values = array();
	$prev_bid ="";
	$tlist="";
	$patterns = array();
	$patterns[0] = "/^'*/";
	$patterns[1] = "/'*$/";

	foreach ($stmt->fetchAll() as $row) {

		$curr_bid = $row['GTB_BUILDING_NUMBER'];

		if ($prev_bid != $curr_bid)
		{ //make a new taglist since a new building has appeared
			if (isset($prev_row))
			{ //to make sure its not the 1st row
				$prev_row['tag_list']=$tlist;
				array_push($row_values, $prev_row);//push into row_values the current row. 
			}
			$tlist= array();
		}
		array_push($tlist,preg_replace($patterns,"",$row['tag_name']));

		$prev_bid = $curr_bid;
		$prev_row['b_id']=$row['GTB_BUILDING_NUMBER'];

	}
	$ze = Zend_Json::encode($row_values);
	echo $ze;
}

function searchByTagName($tagname) {
	global $db;
	$sl = $db->select()->from("Building", array("GTB_BUILDING_NUMBER","GTB_NAME","GTB_ADDRESS","image_url","phone_num"))->joinLeftUsing("tags","GTB_BUILDING_NUMBER",array("tag_name"))->where("tag_name LIKE ?", (preg_match("/^'.*?'$/", $tagname)) ? $tagname : $db->quote($tagname));
	// echo $sl;
	$qu = $sl->query();
	fb($sl->__toString(), "Query");
	$row_values = array();
	foreach ($qu->fetchAll() as $row) {
		array_push($row_values, $row);
	}
	$ze = Zend_Json::encode($row_values);
	echo $ze;
}

function searchByBuildingName($bname) {
	global $db;
	$sl = $db->select();
	$sl->from("Building", array("GTB_BUILDING_NUMBER", "GTB_NAME",
				"GTB_ADDRESS"));
	$sl->joinLeft("GoogleEarth",
			"Building.GTB_BUILDING_NUMBER = GoogleEarth.Building_GTB_BUILDING_NUMBER",
			array("latitude", "longitude", "phone", "image"));
	$sl->where("GTB_NAME LIKE ?", "%".implode("%",
				explode(" ", strtolower($bname)))."%");
	$qu = $sl->query();
	fb($sl->__toString(), "Query");
	$row_values = array();
	foreach ($qu->fetchAll() as $row) {
		$newrow = array();
		$newrow['b_id']=$row['GTB_BUILDING_NUMBER'];
		$newrow['name']=$row['GTB_NAME'];
		$newrow['address']=$row['GTB_ADDRESS'];
		$newrow['phone_num']=$row['phone'];
		if (isset($row['image'])) {
			$newrow['image_url']="http://maps.gatech.edu/bldgimg/".$row['image'].".gif";
		}
		$newrow['longitude']=$row['longitude'];
		$newrow['latitude']=$row['latitude'];
		array_push($row_values, $newrow);
	}
	$ze = Zend_Json::encode($row_values);
	echo $ze;
}

function getRowById($bid) {
	global $building;
	echo $building->getRow($bid);
}

function addTag($bid,$tagname) {
	global $db,$tag;
	//Placeholder to call getusername()
	global $_USER;
	$user = $_USER['uid'];
	$sl = $tag->find($bid, $db->quote($tagname));
	$cols = array("GTB_BUILDING_NUMBER" => $bid, "tag_name" => $db->quote(strtolower($tagname))); //"gtuser" => $_GET["user"]);
	if ($sl->count() == 0) {
		$cols["gtuser"] = $user;
		$temp = $tag->insert($cols);
	} else {
		foreach ($sl as $row) {
			$cols["times_tag"] = $row->times_tag + 1;
			//TODO:
			$row->setFromArray($cols);
			$row->save();
		}
	}
	echo "success";
}

function getTagNames() {
	global $tag;
	$row_values = array();
	$sl = $tag->select()->where("times_flagged < 5");
	// foreach ($tag->fetchAll() as $row) {
	foreach ($tag->fetchAll($sl) as $row) {
		array_push($row_values, $row->toArray());
	}
	$ze = Zend_Json::encode($row_values);
	echo $ze;
}

function getTagsList() {
	global $db;
	try {
		$rvals = $db->select();
		$rvals->from("Building", array("GTB_BUILDING_NUMBER", "GTB_NAME",
										"GTB_ADDRESS"));
		$rvals->joinLeft("GoogleEarth",
			"Building.GTB_BUILDING_NUMBER = GoogleEarth.Building_GTB_BUILDING_NUMBER",
			array("latitude", "longitude", "phone", "image"));
		$rvals->joinLeft("tags",
			"tags.GTB_BUILDING_NUMBER = GoogleEarth.Building_GTB_BUILDING_NUMBER",
			array("tag_name"));
		$stmt = $rvals->query();
	} catch (Exception $e) {
		error_log($e->getMessage());
		die();
	}
	$row_values = array();
	$prev_bid ="";
	$tlist="";
	$patterns = array();
	$patterns[0] = "/^'*/";
	$patterns[1] = "/'*$/";

	foreach ($stmt->fetchAll() as $row) {
		$curr_bid = $row['GTB_BUILDING_NUMBER'];

		if ($prev_bid != $curr_bid)
		{ //make a new taglist since a new building has appeared
			if (isset($prev_row))
			{ //to make sure its not the 1st row
				$prev_row['tag_list']=$tlist;
				array_push($row_values, $prev_row);//push into row_values the current row. 
			}
			$tlist= array();
		}
		array_push($tlist,preg_replace($patterns,"",$row['tag_name']));

		$prev_bid = $curr_bid;
		$prev_row['b_id']=$row['GTB_BUILDING_NUMBER'];
		$prev_row['name']=$row['GTB_NAME'];
		$prev_row['address']=$row['GTB_ADDRESS'];
		$prev_row['phone_num']=$row['phone'];
		if (isset($row['image'])) {
			$prev_row['image_url']="http://maps.gatech.edu/bldgimg/".$row['image'].".gif";
		}
		$prev_row['longitude']=$row['longitude'];
		$prev_row['latitude']=$row['latitude'];
	}
	$ze = Zend_Json::encode($row_values);
	echo $ze;
}

function stags($tagname) {
	global $tag;
	$sl = $tag->select()->where("tag_name LIKE ?", (preg_match("/^'.*?'$/", $tagname)) ? $tagname : $db->quote($tagname));
	$row_values = array();
	foreach ($tag->fetchAll($sl) as $row) {
		array_push($row_values, $row->toArray());
	}
	$ze = Zend_Json::encode($row_values);
	echo $ze;
}

function flagTag($bid,$tagname) {
	global $db,$tag,$_USER;

	$sl = $tag->find($bid, $db->quote($tagname));
	$gtuser = $_USER['uid'];
	$flagged = 0;
	// error_log("$sl");
	foreach ($sl as $row) {
		fb($row, "Flag Row");
		foreach (explode(",", $row["flag_users"]) as $key) {
			if (strcmp($gtuser, $key) == 0) {
				error_log("$key has already flagged this item");
				fb("$key has already flagged this item");
				$flagged = 1;
				break;
			}
		}
		if (!$flagged) {
			fb("$gtuser hasn't flagged it", "Hasn't");
			$data = array ("times_flagged" => $row["times_flagged"] + 1, "flag_users" => $row["flag_users"]."$gtuser,");
			fb($data, "Data to be updated");
			$row->setFromArray($data);
			$row->save();
		} else {
			$ze = Zend_Json::encode($row->toArray());
			// echo $ze;
		}
	}
}

function getAllBuildings() {
	global $building;
	$building->getAll();
}

?>
