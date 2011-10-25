var db;
var templateRow = '<div class="searchResult" id="searchResultTemplateRow" onclick="searchResultClick(\'%%PLACEID%%\');">	<div class="placeID">%%PLACEID%%</div><div class="placeName">%%PLACENAME%%</div>	<div class="placeDistance">&nbsp;</div>	<div class="placeLinkButton">		&nbsp;	</div></div>';
var searchTimer = null;
var screenWidth = 0;
var currentPlaceID = -1;

var startDate = null;

function initDB() {	 	
	try {
		if (!window.openDatabase) {
	   	throw 'Web SQL databases are not supported by this browser.';
	   } 
		else {
	   	var shortName = 'BuildingsData';
	      var version = '1.0';
	      var displayName = 'Stores the list of Buildings';
	      var maxSize = 65536; // in bytes
        
			db = openDatabase(shortName, version, displayName, maxSize);
			
			// create required tables if they don't exist
			db.transaction(function (tx) {
			  	tx.executeSql('CREATE TABLE IF NOT EXISTS buildings (id, name, address, image_url, latitude, longitude, tags)', [], function(tx, results) {
					// all is good - either the table already exists or we created it first

					$("#loadingIndicator").show();
					
					tx.executeSql("SELECT COUNT(*) as recordCount FROM buildings", [], function(tx, results) {
						var recordCount = results.rows.item(0)["recordCount"];

						// we have no records, let's fetch the data and insert it
						if (recordCount == 0) {
							// make an xmlhttprequest to fetch the list of buildings
							// Building details are loaded from static file rather than database to improve performance.
							// When a new place gets added to the database,this file needs to be updated.
							$.getJSON("buildingData.json", insertJSONDataIntoDB);
						}
						else {
							// console.log((Date.now() - startDate) + " gonna clear tags table");
							// 							startDate = Date.now();
							insertTagsData();
						}
					});
				},
				function(tx, err) { // handle create table errors 
					displayErrorMessage(err);
				});
			});
	   }
	} 
	catch(e) {
		// Safari docs (http://developer.apple.com/library/safari/#documentation/iphone/conceptual/safarijsdatabaseguide/usingthejavascriptdatabase/usingthejavascriptdatabase.html#//apple_ref/doc/uid/TP40007256-CH3-XSW1)
		// say that version mismatch is error code 2, however
		// the W3 WebSQL Specs (http://dev.w3.org/html5/webdatabase/#sql) 
		// say it should be a INVALID_STATE_ERROR
		// From my testing it is the latter which gets thrown, but I'm
		// including both just in case.
	   if (e == 2 || (e instanceof DOMException && e.code == 11)) {
	        // Version number mismatch.
	         throw "Invalid database version.";
	   }
	 	else {
	        throw e;
	   }
	}
}

// Get the latest set of tags for places
function insertTagsData() {
	db.transaction(function (tx) {
		tx.executeSql('CREATE TABLE IF NOT EXISTS buildingsTags (buildingid, tag_id, tag)', [], function (tx, results) {
			tx.executeSql("DELETE FROM buildingsTags", [], function(tx, results) {
				// console.log((Date.now() - startDate) + " done clearing tags");
				// 				startDate = Date.now();
				$.getJSON("../../api/gtplaces/tags", null, insertTagsDataIntoDB);
			});
		});
	});
}

// Convert the returned json object into a form that is easier to insert into the local html5 db
function preprocessTagsData(data) {
	var tagsData = {};
	for (var i = 0; i < data.length; i++) {
		if (tagsData[data[i]["b_id"]] == null)
			tagsData[data[i]["b_id"]] = [{"id": data[i]["tag_id"], "tag": data[i]["tag_name"].replace("'", "").replace("'", "")}];
		else
			tagsData[data[i]["b_id"]].push({"id": data[i]["tag_id"], "tag": data[i]["tag_name"].replace("'", "").replace("'", "")});
	}
	
	var x = [];
	//console.log(data);
	//console.log(tagsData);
	//var buildingids = Object.keys(tagsData);
	var buildingids = [];
	for (bid in tagsData)
		buildingids.push(bid);

	for (var i = 0; i < buildingids.length; i++) {
		var bid = buildingids[i];
		x.push({
			"buildingid": bid,
			"tags": tagsData[bid]
		});
	}
	
	return x;
}

// Callback from tags fetch ajax call.
function insertTagsDataIntoDB(data) {
	// console.log((Date.now() - startDate) + " got new tags from server");
	// startDate = Date.now();
	
	var tagsData = preprocessTagsData(data);
	
	// console.log((Date.now() - startDate) + " done preprocessing tags");
	// startDate = Date.now();
	
	// console.log("tags_data:");
	// console.log(tagsData);
	
	for (var i = 0; i < tagsData.length; i++) {
		var buildingid = tagsData[i]["buildingid"];
		var tags = tagsData[i]["tags"];
		var allTagsString = "";
		
		var insertBuildingTagFunc = function(buildingid, tags, currentBldgIdx, maxBldgIdx) {
			return function(tx) {
				for (var j = 0; j < tags.length; j++) {
					var tagid = tags[j]["id"];
					var tag = tags[j]["tag"];

					allTagsString += tag + " ";

					tx.executeSql("INSERT INTO buildingsTags VALUES(?, ?, ?)",
									[
										buildingid,
										tagid,
										tag
									],
						function(buildingid, tag, currentTagIdx, maxTagIdx) {
							return function(tx, results) {
								// console.log(currentTagIdx + "/" + maxTagIdx + " inserted for building id:" + buildingid + " " + tag);
								if (currentTagIdx == maxTagIdx) {
									//console.log(allTagsString);
									tx.executeSql("UPDATE buildings SET tags = ? WHERE id = ?",
											[
												allTagsString,
												buildingid
											],
										function(tx, results) {
											// console.log("updated building tags: " + allTagsString + " for building id:" + buildingid);
										   allTagsString = "";
											if (currentBldgIdx == maxBldgIdx) {
												// console.log("all done");
											 	// console.log((Date.now() - startDate) + " all done updating tags in buildings");
												// startDate = Date.now();
												initList();
											}
										},
										function(tx, err) { // handle create table errors
											displayErrorMessage(err);
										});
												
									}
								}
							}(buildingid, tag, j+1, tags.length),
									
							function(tx, err) { // handle create table errors
								displayErrorMessage(err);
							});
						}
			};
		}
		db.transaction(insertBuildingTagFunc(buildingid, tags, i+1, tagsData.length));
	}
}

function insertJSONDataIntoDB(data) {
    // console.log("got json data, gonna process it");
	var buildingData = data["buildingData"];
	// console.log("buildingData:");
	// console.log(buildingData);
	
	var building;
	for (var i = 0; i < buildingData.length; i++) {
		building = buildingData[i];
		
		var insertFunc = function(bldg, currentIdx, maxIdx) {
			// this function "closes-over" the local scope which includes the bldg variable
			return function(tx) {
				tx.executeSql("INSERT INTO buildings VALUES(?, ?, ?, ?, ?, ?, ?)", 
					[
						bldg["id"], 
						bldg["name"], 
						bldg["address"], 
						bldg["image_url"],
						bldg["latitude"], 
						bldg["longitude"],
						""
					],
					function(tx, results) {
						// console.log("inserted" + currentIdx);
						// Check if we have finished inserting all the records
						if (currentIdx == maxIdx) {
							// console.log("all done inserting records, now gonna initlist");
							insertTagsData();
							// initList();
						}
										
						// console.log("Wrote row: " + bldg["name"]);
					},
					function(tx, err) { // handle create table errors
						displayErrorMessage(err);
					});
			};
		}(building, i, buildingData.length - 1);

		db.transaction(insertFunc);
	}
}

function testDB() {
	var ctr = 0;
	
	db.transaction(function(tx) {
		tx.executeSql("SELECT COUNT(*) FROM buildings", [], function(tx, results) {
			console.log("total number:");
			console.log(results.rows.item(0));
		});
	});
	
	for (var i = 0; i < buildingJSONData2.length; i++) {
		var building = buildingJSONData2[i];
		
		db.transaction(function(id, name, ctr) {
			return function(tx) {
				tx.executeSql("SELECT name FROM buildings where name = ?", [name], function(tx, results) {
					if (results.rows.length == 0)
						console.log(name + " not found!");
					else if (results.rows.length > 1)
						console.log(name + " more than one result found!");
					else
					{
						tx.executeSql("UPDATE buildings SET id = ? WHERE name = ?", [id, name], function(tx, results) {
							console.log("OK updated! " + id + " " + name);
						});
					}
				});
			}
		}(building["id"], building["name"], ctr));
	}
	
	// console.log("TOTAL MATCHED:" + ctr);
}

function loadDataIntoDB() {
	if (db) {
		db.transaction(function(tx) {
			tx.executeSql("SELECT * FROM buildings", [], function(tx, results) {
				if (results.rows.length == 0) {
					var building = null;
					for (var i = 0; i < buildingJSONData.length; i++) {
						building = buildingJSONData[i];
						tx.executeSql("INSERT INTO buildings VALUES(?, ?, ?, ?, ?, ?)", 
										[building["id"], building["name"], building["address"], building["image_url"],
										building["latitude"], building["longitude"]], 
										function(tx, results) {
											// console.log("Wrote row: " + building["name"]);
										});
					}
				}
				// else
					// alert("we already have data.")
			});
		});
	}
	else
		alert("No database found...");
}

function truncateTable() {
	db.transaction(function(tx) {
		tx.executeSql("DELETE FROM buildings", [], function(tx, results) {
			alert(results.rowsAffected);
		});
	});
}

function dropTable() {
	db.transaction(function(tx) {
		tx.executeSql("DROP TABLE buildings", [], function(tx, results) {
			alert("dropped!");
		});
	});
}

// This function takes the list of rows from the database and creates the
// HTML of the list of places to be shown on screen
function populateList(rows) {
    var listString = "";
    
	document.getElementById("searchResultsList").innerHTML = "";
	
	if (rows.length > 0) {	
		var row = null;
        for (var i = 0; i < rows.length; i++) {
			row = rows.item(i);
			listString += templateRow.replace("%%PLACEID%%", row["id"]).replace("%%ID%%", row["id"]).replace("%%PLACENAME%%", row["name"]);
		}
	}
	else
	    listString = '<div class="searchResult loadMoreResults">No places found</div>';
	
	$("#loadingIndicator").hide();
	document.getElementById("searchResultsList").innerHTML = listString;
	
	library.changeLinksForOffline();
	
	// $(".searchResult").live("click", function() {
	// 	alert($(this).children(".placeName").text());
	// 	showPlaceInfoPage($(this).children(".placeID").text());
	// });
}

function searchResultClick(placeID) {
	// showPlaceInfoPage($(this).children(".placeID").text());
	showPlaceInfoPage(jQuery.trim(placeID));
}

function emptyFuncHandler() {	}

function initList() {
	$("#loadingIndicator").hide();
	
	// var listString = '<div class="searchResult loadMoreResults" onclick="filterList();">Show list of all places</div>';
	// document.getElementById("searchResultsList").innerHTML = listString;
	filterList("");
}

// This function does the actual searching
function filterList(term) {
    // console.log("Searching " + term);
	var query = "";
	var queryParams = [];
	
	if (term == null || term.length == 0)
		query = "SELECT id, name FROM buildings";
	else {
		query = "SELECT id, name FROM buildings where name like ? or tags like ?";
		queryParams = ["%" + term + "%", "%" + term + "%"]
	}
	
	db.transaction(function(tx) {
		tx.executeSql(query, queryParams, function(tx, results) {
			populateList(results.rows);
		});
	});
}

// This function is called on every change of the search textbox
// Instead of immediately doing a search, which has the problem of 
// triggering multiple searches too quickly when the user types
// quickly, and slowing down the browser as a result, we ask the 
// functino to do the search after waiting for 400ms. If the next 
// ontxtchange is called before this timeout expires, we cancel 
// the timer and start a new one for 400ms. This way, we prevent
// too many searches getting triggered too quickly, while still
// providing a responsive system
function ontxtchange() {
	var searchTerm = document.getElementById("search").value;
	
	clearTimeout(searchTimer);
	searchTimer = setTimeout(function() {filterList(searchTerm);}, 400);
	
	// filterList(searchTerm);
};

function getPlaceDetails(placeID, callback) {
	var query = "SELECT name, address, image_url FROM buildings where id = ?";
	var queryParams = [placeID];
	
	db.transaction(function(tx) {
		tx.executeSql(query, queryParams, function(tx, results) {
			callback(results.rows);
		});
	});
}

function getPlaceTags(placeID, callback) {
	var query = "SELECT tag_id, tag FROM buildingsTags where buildingid = ?";
	var queryParams = [placeID];
	
	db.transaction(function(tx) {
		tx.executeSql(query, queryParams, function(tx, results) {
			callback(results.rows);
		});
	});
}

function showPlaceInfoPage(placeID) {
    currentPlaceID = placeID;
	// $("#placeListMain").css("-webkit-transform","translate3d(" + -1 * (screenWidth) + "px, 0, 0)");
	// $("#placeInfoMain").css("-webkit-transform","translate3d(" + -1 * (screenWidth) + "px, 0, 0)");
	
	$("#portal_header #left a img").attr("src", "img/back.png");
	
	// $("#portal_header #left a").live("click", function() {
	// 	showPlaceListPage();
	// 	return false;
	// });
	
	$("#portal_header #left a").click(function() {
		showPlaceListPage();
		return false;
	});
	
	getPlaceDetails(placeID, populatePlaceInfo);
	
	getPlaceTags(placeID, populatePlaceTags);
	
	$("#placeListMain").hide();
	$("#placeInfoMain").show();
	
	library.changeLinksForOffline();
}

function showPlaceListPage() {
    $("#tag_input").hide();
	$("#placeInfoMain").hide();
	$("#placeListMain").show();
	
	$("#portal_header #left a img").attr("src", "include/Home.png");
	
	// $("#portal_header #left a").die();
	$('#portal_header #left a').unbind('click');
	
	library.changeLinksForOffline();
}

function populatePlaceInfo(placeInfoRows) {
	if (placeInfoRows.length > 0) {
		var placeInfo = placeInfoRows.item(0);
		// console.log(placeInfo);
	
		$("#placeInfoMain .placeName").text(placeInfo.name);
		$("#placeInfoMain .placeAddress a").text(placeInfo.address);
		$("#placeInfoMain .placeAddress a").attr("href", "http://maps.google.com?q=" + escape(placeInfo.address));
		
		$("#placeInfoMain .placeImage img").attr("src", "http://gtalumni.org/map/images/buildings/" + placeInfo.image_url);
	}
	else
		alert("Place not found!");

}

function populatePlaceTags(placeTags) {
	// console.log(placeTags);
	
	$("#tags_list").empty();

	if (placeTags.length > 0) {
		for (var i = 0; i < placeTags.length; i++) {
			var placeTag = placeTags.item(i);
	        // $("#tags_list").append("<span class='tag' id='tag" + placeTag["tag_id"] + "'>" + placeTag["tag"] + "</span> ");
	        // $("#tags_list").append("<span class='tag' id='tag" + placeTag["tag_id"] + "'>" + placeTag["tag"] + "</span> ");
			$("<span class='tag' id='tag" + placeTag["tag_id"] + "'>" + placeTag["tag"] + " </span> ").appendTo("#tags_list").click(confirmFlagTag);
	        // $(".tag" + placeTag["tag_id"]).click(function() { alert("asd");});
		}
	}
	else {
		$("#tags_list").append("<p id='noTagsYet'>No tags yet...<p>")
	}
	
    // $("#tags_list .tag").live('click', confirmFlagTag);
}

// function confirmFlagTag(tagId, tag)
function confirmFlagTag() {
    var windowWidth = $(window).width(),
        windowHeight = $(window).height();
    
    var tag = $(this).text().trim();
    var spanTag = this;
    
    $("#confirmFlagPopup #txtFlag").text($(this).text());
    $("#confirmFlagPopup")  .css("top", $(this).position()["top"] + "px").css("left", ((windowWidth - 245)/2) + "px")
                            .show();
    // $("#confirmFlagPopup #txtFlag").text($(this).text())
    //         .css({
    //             'left'  : ((windowWidth - 245)/2) + "px",
    //             'top'   : "200px"
    //         })
    //         .show();
    
	$("#confirmFlagPopup #btnCancel").unbind('click');
    $("#confirmFlagPopup #btnCancel").click(function() {
        $("#confirmFlagPopup").hide();
    });
    
	$("#confirmFlagPopup #btnFlag").unbind('click');
    $("#confirmFlagPopup #btnFlag").click(function() {
		tag = "'" + tag + "'";
		console.log(tag);
        $.post("../../api/gtplaces/tags/" + tag + "flag", { "bid": currentPlaceID}, function(data) {
		    // console.log("flagged tag: " + tag);
		    
		    $("#confirmFlagPopup").hide();
		    $(spanTag).css("color", "red");
	    });
    });
}

function findElemIn(coll, itemName, value) {
	for (var i= 0 ; i < coll.length; i++) {
		item = coll[i];
		if (item[itemName] == value)
			return item;
	}
	
	return null;
}

function doJSONStuff() {
	var finalBuildingData = [];
	
	for (var i = 0; i < buildingJSONData.length; i++) {
		var name = buildingJSONData[i]["name"];
		var item = findElemIn(buildingJSONData2, "name", name);

		buildingJSONData[i]["id"] = item["b_id"];
		
		var item2 = findElemIn(buildingJSONData3, "b_id", item["b_id"]);
		
		buildingJSONData[i]["address"] = item2["address"];
		buildingJSONData[i]["image_url"] = item2["image_url"];
		
		// console.log(name);
	}
	
	// console.log(JSON.stringify(buildingJSONData));
	
	// var x = "";
	// 			for (var i = 0; i < buildingJSONData.length; i++)
	// 			{
	// 
	// 				x += "http://"+window.location.hostname+"/gtplaces.php?id=row&bid=" + buildingJSONData[i]["id"] + "\n";
	// 			}
	// 			
	// 			console.log(x);
}

function displayErrorMessage(err) {
	alert("Error occurred! - " + err);
	if (console && console.log) {
		console.log("Error Occurred:");
		console.log(err);
	}
}

function addTag() {
	if ($("#tag_input").is(":visible")) {
		$("#tag_input").hide();
		$("#add_tag_link img").attr("src", "img/button_add_up.png")
	}
	else {
		$("#tag_input").show();
		$("#add_tag_link img").attr("src", "img/button_add_down.png")
	}
}

function saveTag() {
	// alert($("#new_tag").val());
	var newTag = $.trim($("#new_tag").val().toLowerCase());
	
	if (newTag.length != 0) {
	    // Send a AJAX reques to save the new tag
		$.post("../../api/gtplaces/tags", { "bid": currentPlaceID, "tag": newTag }, function(data) {
			// console.log("added tag!");
		   var tagData = data.pop();
		    
         while(tagData["tag_name"] != "'" + newTag + "'") {
         	tagData = data.pop();
         }
		    
            // console.log("added tag!");
			// insertTagsDataIntoDB();
			
			// Once hte ajax request returns successfully, inser the new tag
			// into the buildingTags table and update the buildings tags string
			// so that hte new tag can be used for searching
			db.transaction(function(tx) {
				tx.executeSql("INSERT INTO buildingsTags VALUES(?, ?, ?)",
					[
						currentPlaceID,
						tagData["tag_id"],
						newTag
					],
					function(tx, results) {
						// console.log("saved tag");
					},
					function(tx, err) {
						displayErrorMessage(err);
					}
				);
								
				tx.executeSql("UPDATE buildings SET tags = tags || ' ' || ? WHERE id = ?",
					[
						newTag,
						currentPlaceID
					],
					function (tx, results) {
						// console.log("updated db");
						// $("#tags_list").append("<span class='tag' id='tag" + -1 + "'>" + newTag + "</span> ");
						$("#tags_list #noTagsYet").remove();
						$("<span class='tag' id='tag" + tagData["tag_id"] + "'>" + newTag + " </span> ").appendTo("#tags_list").click(confirmFlagTag);
						$("#new_tag").val("");
						$("#tag_input").hide();
					},
					function (tx, err) {
						displayErrorMessage(err);
					}
				);
			});
		},"json");
	}
}

function body_onload() {
	$("#mapChoice").click(function() {
	   alert("Coming soon!");
	});
	
	$("#add_tag_link").click(addTag);
	$("#tag_button").click(saveTag);
	$("#cancel_new_tag").click(function() { $("#tag_input").hide(); })
	
	// set the widths of the screen divs, etc so that we can slide them left and right
	// using either just javascript or css3 animations
	// right now these animations are slow and have been disabled
	screenWidth = $(window).width();
	
	$("#screens").width(screenWidth*2);
				
	$("#placeListMain").width(screenWidth - 20);
	$("#placeInfoMain").width(screenWidth - 20);
	
	$("#placeInfoMain").css("left", screenWidth);
	$(window).resize(function() {
   	screenWidth = $(window).width();
      $("#screens").width(screenWidth*2);          
      $("#placeListMain").width(screenWidth - 20);
      $("#placeInfoMain").width(screenWidth - 20);
    	$("#placeInfoMain").css("left", screenWidth);
   });	
	$("#loadingIndicator").hide();
	
	startDate = Date.now();
	
	try {
		initDB();
		return;
	}
	catch (err) {
		displayErrorMessage(err);
	}
}

$(document).ready(function() {
	body_onload();
});
