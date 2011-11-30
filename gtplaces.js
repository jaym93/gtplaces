var db;
var templateRow;
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

					//$("#loadingIndicator").show();
					$.mobile.showPageLoadingMsg(); //show loading icons
					
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
				$.getJSON("../api/tags", null, insertTagsDataIntoDB);
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
	
	var tagsData = preprocessTagsData(data);
	

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

// This function takes the list of rows from the database and create template rows
// HTML of the list of places to be shown on screen
function populateList(rows) {
    var listString;
	
	/* Instantiate the global variable as an empty array.*/
	templateRow= {};
	
	$("#building_no_results_message").hide();
	/* 
	 * Clear the previous result elements from the HTML DOM, if they exist. This way nothing is attached to 
	 * the searchResultsList div.
	 */
	$("#searchResultsList").empty();
	
	if (rows.length > 0) {	
		var row = null;
        for (var i = 0; i < rows.length; i++) {
			row = rows.item(i);	
			
			/* Add the newly created building name to the array list, with the key "buildingName" 
			 * Add the newly created building ID to the array list, with the key "buildingName"
			 */
			templateRow.buildingID=row["id"];
			templateRow.buildingName=row["name"];
			
			$("#buildingListTemplate").tmpl(templateRow).appendTo( "#searchResultsList" );
			$('#searchResultsList').listview('refresh');
		}
	}
	else
	    $("#building_no_results_message").show();
	
	//$("#loadingIndicator").hide();
	 $.mobile.hidePageLoadingMsg();//hide loading icons
	
	library.changeLinksForOffline();	
}

function searchResultClick(placeID) {
	
	showPlaceInfoPage(jQuery.trim(placeID));
}

function emptyFuncHandler() {	}

function initList() {
	//$("#loadingIndicator").hide();
	 $.mobile.hidePageLoadingMsg();//hide loading icons

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
	
	getPlaceDetails(placeID, populatePlaceInfo);
	
	getPlaceTags(placeID, populatePlaceTags);
	
	library.changeLinksForOffline();
}

function populatePlaceInfo(placeInfoRows) {
	/* Instantiate the variable as an empty array.*/
	var templateBuildingInfo = {};
	var buildingAddressInfo={};
	
	/*Clear the previous result elements from the HTML DOM, if they exist. */
	$("#buildingDetailInfo").empty();
	
	$("#building_address_link").empty();
	
	if (placeInfoRows.length > 0) {
		var placeInfo = placeInfoRows.item(0);
		
		/* Add the newly created building place name to the array list, with the key "placeName" 

         * Add the newly created building image url to the array list, with the key "placeImageUrl"

         */
		templateBuildingInfo.placeName=placeInfo.name;
		templateBuildingInfo.placeImageUrl= "http://gtalumni.org/map/images/buildings/" + placeInfo.image_url;
		
		buildingAddressInfo.placeAddress=placeInfo.address;
		buildingAddressInfo.placeAddressUrl="http://maps.google.com?q=" + escape(placeInfo.address);
		
		$("#buildingInfoTemplate").tmpl(templateBuildingInfo).appendTo( "#buildingDetailInfo" );
	
        $('#searchResultsList').listview('refresh');
		
		$("#buildingAddressTemplate").tmpl(buildingAddressInfo).appendTo( "#building_address_link");
	}
	else
		alert("Place not found!");

}


function populatePlaceTags(placeTags) {
	//console.log(placeTags);
	var placeTagList={};
	$("#tags_list").empty();

	if (placeTags.length > 0) {
		for (var i = 0; i < placeTags.length; i++) {
			var placeTag = placeTags.item(i);
			
	        placeTagList.buildingTagId =placeTag.tag_id;
			placeTagList.buildingTag=placeTag.tag;
			
			$("#tagInfoTemplate").tmpl(placeTagList).appendTo( "#tags_list" );
			
			
		}
	}
	else {
		$("#noTaginfo").show();
	}
	
}

function confirmFlagTag(e) {
	
    var selectedTag=$(e).text().trim();
	var selectedTagId = $(e).attr("id");
	console.log(selectedTagId);
	console.log(selectedTag);
	$("#txtFlag").empty();
	$("#txtFlag").append(selectedTag); 
	
	$("#btnFlag").click(function() {
		//console.log(selectedTag);
        $.post("../api/tags/" + selectedTag +"/flag", { "bid": currentPlaceID}, function(data) {
		    
		    $("#"+selectedTagId).find('a').css("color", "red");
			$("#"+selectedTagId).css("font-size", "12px");
			
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
			}
	else {
		$("#tag_input").show();
	}
}

function saveTag() {
	// alert($("#new_tag").val());
	var newTag = $.trim($("#new_tag").val().toLowerCase());
	
	if (newTag.length != 0) {
	    // Send a AJAX reques to save the new tag
		$.post("../api/tags/", { "bid": currentPlaceID, "tag": newTag }, function(data) {
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
						
						$("#tags_list #noTagsYet").remove();
						$("<span class='tag' id='tag" + tagData["tag_id"] + "'>" + "<a href='#confirmFlagPopup' data-role='button' data-inline='true' data-rel='dialog' data-transition='pop'>"+ newTag + "</a>" +" </span> ").appendTo("#tags_list").click(function(){
							confirmFlagTag(this);
						});
					
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
	
	
	//$("#loadingIndicator").hide();
	 $.mobile.hidePageLoadingMsg();//hide loading icons
	
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
