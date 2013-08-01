//TODO: Hide tag button if not logged in
//TODO: permalink on placeInfoMain


var test;

var db;
var templateRow;
var searchTimer = null;
var screenWidth = 0;
var currentPlaceID = -1;
var buildings = {};
var tags;
var startDate = null;



$(document).ready(function() {
	body_onload();
});



function addTag() {
	if ($("#tag_input").is(":visible")) {
		$("#tag_input").hide();
	}
	else {
		$("#tag_input").show();
	}
}


function body_onload() {
	$("#mapChoice").live('click',function() {
        alert("Coming soon!");
	});
	
	$("#add_tag_link").live('click',addTag);
	$("#tag_button").live('click',saveTag);
	$("#cancel_new_tag").live('click',function() { $("#tag_input").hide(); })
	
	
	//$("#loadingIndicator").hide();
    $.mobile.hidePageLoadingMsg();//hide loading icons
	
	startDate = Date.now();
	
	try {
		if(placesJSONText = localStorage.getItem('OfflineGTplaces')) {
		    console.log("Loading data from localStorage");
			loadPlaces(placesJSONText);
		} else {
		    console.log("Fetching data from servers");
			init();
		}
		return;
	} catch (err) {
		alert("Error occurred! - " + err);
		console.log("Error Occurred:");
		console.log(err);
	}
}


function confirmFlagTag(e) {
    var selectedTag = $.trim($(e).text());
	var selectedTagId = $(e).attr("id");
	$("#txtFlag").empty();
	$("#txtFlag").append(selectedTag); 
	
	$("#btnFlag").click(function() {
        $.post("api/tags/" + selectedTag +"/flag", { "bid": currentPlaceID}, function(data) {
            $("#"+selectedTagId).find('a').css("color", "red");
            $("#"+selectedTagId).css("font-size", "12px");
        });
    });	
}


/*
Modified by Janani Narayanan
****************************
Function to query buildings to display tags 
for the selected building.
*/
function getPlaceTags(placeID, callback) {
    jQuery.map(tags,function (obj) {
        if(obj.b_id == placeID) {
            callback(obj);
        }
    });
}


function init() {
    // Put the object into storage - added by Janani Narayanan
   if(supports_html5_storage()) {
	   	localStorage.clear();
		$.getJSON("api/buildings/", function(data) {
		    console.log("Downloaded buildings");
			localStorage.setItem('OfflineGTplaces', JSON.stringify(data));
		    loadPlaces();
		});
   } else{
   		console.log("Your Browser Doesn't Support HTML5 Storage");
   }
}


function loadPlaces() {	
	//Load sequential array into associative array
	var OfflineGTplaces = JSON.parse(localStorage.getItem('OfflineGTplaces'));
	buildings = {};
	$.each(OfflineGTplaces, function(){
        buildings[this.b_id] = this;
    });
    
    //Build buildings list
	populateList();
	$.getJSON("api/tags/",function(data){
	    console.log("Downloaded tags");
    	localStorage.setItem('GTplacesTags',JSON.stringify(data));		
	    loadTags();
    });
    
    //Put name of building with supplied building id in search field
    bid = $.url().fparam("bid");
    if (bid !== undefined && bid.length > 0) {
        $.getJSON("api/buildings_id/"+bid,function(data){
            $("input[data-type='search']").val(data[0].GTB_NAME).trigger('change');
        });
    }
}


//Add tags to each element in building listview for searching by tag
function loadTags() {
	tags = JSON.parse(localStorage.getItem('GTplacesTags'));	
	for(var i = 0; i < tags.length; i++) {
	    $("p#" + tags[i].GTB_BUILDING_NUMBER).append(tags[i].tag_name + ", ");
	}	
}


function populateList() {
    var listString;
	/* Instantiate the global variable as an empty array.*/
	templateRow = {};
	$("#building_no_results_message").hide();
	/* 
	 * Clear the previous result elements from the HTML DOM, if they exist. This way nothing is attached to 
	 * the searchResultsList div.
	 */
	$("#searchResultsList").empty();
	if (buildings !== undefined && buildings !== {}) {
        //for (var i = 0; i < rows.length; i++) {
        $.each(buildings, function() {
			/* Add the newly created building name to the array list, with the key "buildingName" 
			 * Add the newly created building ID to the array list, with the key "buildingName"
			 */
			templateRow.buildingID = this.b_id;
			templateRow.buildingName = this.name.replace("\\","");
			$("#buildingListTemplate").tmpl(templateRow).appendTo( "#searchResultsList" );
			$('#searchResultsList').listview('refresh');
		});
	} else {
	    $("#building_no_results_message").show();
    }
	$.mobile.hidePageLoadingMsg(); //hide loading icons
	library.changeLinksForOffline();	
}


function populatePlaceInfo(placeInfo) {
	/* Instantiate the variable as an empty array.*/
	var templateBuildingInfo = {};
	var buildingAddressInfo = {};
	/*Clear the previous result elements from the HTML DOM, if they exist. */
	$("#buildingDetailInfo").empty();
	$("#building_address_link").empty();
	$("#phone_num_link").empty();
	
	if (placeInfo.name != "") {
		
		/* Add the newly created building place name to the array list, with the key "placeName" 

         * Add the newly created building image url to the array list, with the key "placeImageUrl"

         */
		templateBuildingInfo.placeName=placeInfo.name;
		templateBuildingInfo.placeImageUrl= placeInfo.image_url;
		
		buildingAddressInfo.placeAddress=placeInfo.address;
		buildingAddressInfo.placeAddressUrl="http://maps.google.com?q=" + escape(placeInfo.address) + " Georgia Institute of Technology";
		buildingAddressInfo.phone_num=placeInfo.phone_num;
		$("#buildingInfoTemplate").tmpl(templateBuildingInfo).appendTo( "#buildingDetailInfo" );
	
        $('#searchResultsList').listview('refresh');
		
		$("#buildingAddressTemplate").tmpl(buildingAddressInfo).appendTo( "#building_address_link");
		$("#phoneNumberTemplate").tmpl(buildingAddressInfo).appendTo("#phone_num_link");
	} else {
		alert("Place not found!");
	}
}


function populatePlaceTags(placeTag) {
	var placeTagList = {};
	$("#tags_list").empty();
	$("#noTaginfo").hide();
	test = placeTag;

	if(placeTag.tag_list != "") {
        var currTokens = placeTag.tag_list;
        for (var i = 0; i < currTokens.length; i++) {
            placeTagList.buildingId = placeTag.b_id;
            placeTagList.buildingTag = currTokens[i];
            $("#tagInfoTemplate").tmpl(placeTagList).appendTo( "#tags_list" );
        }
	} else {
		$("#noTaginfo").show();
	}
	
}


function saveTag() {
	var newTag = $.trim($("#new_tag").val().toLowerCase());
	
	if (newTag.length != 0) {
	    // Send a AJAX reques to save the new tag
		$.post("api/tags/", { "bid": currentPlaceID, "tag": newTag }, function(data) {
			if("success" == $.trim(data)) {
			    console.log("Saved tag");
			    // Once the ajax request returns successfully, insert the new tag
			    // into the buildingTags table and update the buildings tags string
			    // so that the new tag can be used for searching
			    $.map(tags, function (obj) {
                    if(obj.GTB_BUILDING_NUMBER == currentPlaceID) {
                        obj.tag_list.push(newTag);
                        $("#tags_list #noTagsYet").remove();
                        $("<span class='tag' id=" + currentPlaceID + "_" 
                                + newTag + "'>" 
                                + "<a href='#confirmFlagPopup' data-role='button'"
                                + " data-inline='true' data-rel='dialog' data-transition='pop'>"
                                + newTag + "</a>" +" </span> ")
                        .appendTo("#tags_list").click(function() {
                            confirmFlagTag(this);
                         });

                        $("#new_tag").val("");
                        $("#tag_input").hide();
                    }
		       });
			}
		});
	}
}


function searchResultClick(placeID) {
	showPlaceInfoPage($.trim(placeID));
}


function showPlaceInfoPage(placeID) {
	currentPlaceID = placeID;
	console.log(buildings[placeID]);
	populatePlaceInfo(buildings[placeID]);
	getPlaceTags(placeID, populatePlaceTags);
	library.changeLinksForOffline();
}


// Check if the browser supports offline sotrage
function supports_html5_storage() {
    try {
        return 'localStorage' in window && window['localStorage'] !== null;
    } catch (e) {
        return false;
    }
}

