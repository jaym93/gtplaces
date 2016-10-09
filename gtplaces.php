<?php
require_once("Zend/Json.php");
include_once("Zend/Db.php");
require_once("Zend/Db/Table.php");
//require_once("FirePHPCore/fb.php");
//$firephp = FirePHP::getInstance(true);
include_once("db_config.php");

function fb($param,$name){
	//Had to disable
}

$params = array("host" => $db_host, "username" => $db_username, "password" => $db_password, "dbname" => $db_database);
$db = Zend_Db::factory("Pdo_Mysql", $params);

class Buildings extends Zend_Db_Table_Abstract {

	protected $_name = "buildings";
	
	public function getIdsNames() {
		$select = $this->select()->from($this, array("b_id", "name"));
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
	// b_id,name,address,latitude,longitude
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
	protected $_primary = array('b_id', 'tag_name');
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
   $rvals = $db->select()->from("tags", array("b_id","tag_name"))->order("b_id ASC");

	$stmt = $rvals->query();
   $row_values = array();
   $prev_bid ="";
   $tlist="";
   $patterns = array();
   $patterns[0] = "/^'*/";
   $patterns[1] = "/'*$/";

	foreach ($stmt->fetchAll() as $row) {

      $curr_bid = $row['b_id'];

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
		$prev_row['b_id']=$row['b_id'];

   }
   $ze = Zend_Json::encode($row_values);
   echo $ze;
}

function searchByTagname($tagname) {
	global $db;
   $sl = $db->select()->from("buildings", array("b_id","name","address","image_url","phone_num"))->joinLeftUsing("tags","b_id",array("tag_name"))->where("tag_name LIKE ?", (preg_match("/^'.*?'$/", $tagname)) ? $tagname : $db->quote($tagname));
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
   $sl = $db->select()->from("buildings", array("b_id", "name", "address", "image_url","longitude","latitude","phone_num"))->where("name LIKE ?", "%".implode("%", explode(" ", strtolower($bname)))."%");
   $qu = $sl->query();
   fb($sl->__toString(), "Query");
   $row_values = array();
   foreach ($qu->fetchAll() as $row) {
      array_push($row_values, $row);
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
   $cols = array("b_id" => $bid, "tag_name" => $db->quote(strtolower($tagname))); //"gtuser" => $_GET["user"]);
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

function getCategories() {
   global $db;
   $categories=array();
   $stmt=$db->select()->distinct()->from("categories",array("cat_name"))->query();
   foreach($stmt->fetchAll() as $row){
	array_push($categories,$row['cat_name']);
   }
   $ze= Zend_Json::encode($categories);
   echo $ze;
}

function getBuildingsByCategory($category){
   global $db;
   $sl = $db->select()->from("buildings", array("b_id","name","address","image_url","phone_num"))->joinLeftUsing("categories","b_id",array("cat_name"))->where("cat_name LIKE ?", $category)->query();
      $categories=array();
   
   foreach($sl->fetchAll() as $row){
      array_push($categories,$row);
   }
   $ze= Zend_Json::encode($categories);
   echo $ze;

}

function getTagsList() {
	global $db;
   $rvals = $db->select()->from("buildings", array("b_id","name","address","image_url","latitude","longitude","phone_num"))->joinLeftUsing("tags", "b_id", array("tag_name"))->order("b_id ASC");
   $stmt = $rvals->query();
   $row_values = array();
   $prev_bid ="";
   $tlist="";
   $patterns = array();
   $patterns[0] = "/^'*/";
   $patterns[1] = "/'*$/";

   foreach ($stmt->fetchAll() as $row) {
      $curr_bid = $row['b_id'];

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
      $prev_row['b_id']=$row['b_id'];
      $prev_row['name']=$row['name'];
      $prev_row['address']=$row['address'];
		$prev_row['image_url']=$row['image_url'];
      $prev_row['latitude']=$row['latitude'];
      $prev_row['longitude']=$row['longitude'];
		$prev_row['phone_num']=$row['phone_num'];
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
   // $logger = new Zend_Log();
   // $writer = new Zend_Log_Writer_Stream('php://output');
   // $logger->addWriter($writer);
   // $logger->info('Informational message');
   
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
