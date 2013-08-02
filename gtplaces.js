//TODO: Hide tag button if not logged in
//TODO: Make tags show on building page


var test;

var currentPlaceID;
var buildings;
var tags;



$(document).ready(function() {
    //Actions
	$("#add_tag_link").on('click', addTag);
	$("#new_tag").on('keypress', function(e) {
	    if (e.keyCode == 13) { //13 == Enter
	        saveTag();
        }
	});
	$("#tag_button").on('click', saveTag);
	$("#cancel_new_tag").on('click', function() {
        $("#tag_input").hide();
    });
	
	//Load building data from localStorage or download from server
	if(placesJSONText = localStorage.getItem('OfflineGTplaces')) {
	    console.log("Loading data from localStorage");
		loadPlaces(placesJSONText);
	} else {
	    console.log("Fetching data from servers");
		init();
	}
	
	//Permalink handling
	var bid = $.url().fparam("bid");
	if ("placeInfoMain" === $.mobile.activePage.attr('id')) {
	    //Load data for building with supplied building id
        if (bid !== undefined && bid.length > 0) {
            console.log("Loading building via permalink");
            searchResultClick(bid);
        }
	} else if ("placeListMain" === $.mobile.activePage.attr('id')) {
	    //Put name of building with supplied building id in search field
        if (bid !== undefined && bid.length > 0) {
            console.log("Loading building via permalink");
            $("input[data-type='search']").val(buildings[bid].name).trigger('change');
        }
        $('#searchResultsList').listview('refresh');
    }
});



function addTag() {
	if ($("#tag_input").is(":visible")) {
		$("#tag_input").hide();
	}
	else {
		$("#tag_input").show();
	}
}


function confirmFlagTag(tagSpan) {
    var selectedTag = $.trim($(tagSpan).text());
	var selectedTagId = $(tagSpan).attr("id");
	$("#txtFlag").empty();
	$("#txtFlag").append(selectedTag);
	
	$("#btnFlag").click(function() {
        $.post("api/tags/" + selectedTag + "/flag", {"bid": currentPlaceID}, function(data) {
            console.log(data);
            test = data;
            $("#"+selectedTagId).find('a').css("color", "red");
            $("#"+selectedTagId).css("font-size", "12px");
        });
    });	
}


function init() {
   // Put the object into storage - added by Janani Narayanan
   if(supports_html5_storage()) {
        $.ajax({
            url: "api/buildings/",
            dataType: 'json',
            async: false,
            success: function(data) {
                console.log("Downloaded buildings");
                localStorage.clear();
                localStorage.setItem('OfflineGTplaces', JSON.stringify(data));
                loadPlaces();
            }
        });
   } else{
   		console.log("Your Browser Doesn't Support HTML5 Storage");
   }
}


function loadPlaces() {	
	//Load places sequential array into associative array
	var OfflineGTplaces = JSON.parse(localStorage.getItem('OfflineGTplaces'));
	buildings = {};
	$.each(OfflineGTplaces, function(){
        buildings[this.b_id] = this;
    });
    
    //Build buildings list
	var listString;
	var templateRow = {};
	$("#building_no_results_message").hide();
	$("#searchResultsList").empty();
	if (buildings !== undefined && buildings !== {}) {
        $.each(buildings, function() {
			templateRow.buildingID = this.b_id;
			templateRow.buildingName = this.name.replace("\\","");
			$("#buildingListTemplate").tmpl(templateRow).appendTo( "#searchResultsList" );
		});
		if ("placeListMain" === $.mobile.activePage.attr('id')) {   
		    $('#searchResultsList').listview('refresh');
	    }
	} else {
	    $("#building_no_results_message").show();
    }
	library.changeLinksForOffline();
	
	//Get tags
	$.getJSON("api/tags/",function(data){
	    console.log("Downloaded tags");
    	localStorage.setItem('GTplacesTags', JSON.stringify(data));		
	    tags = JSON.parse(localStorage.getItem('GTplacesTags'));	
	    //Add tags to each element in building listview for searching by tag
	    for(var i = 0; i < tags.length; i++) {
	        $("p#" + tags[i].GTB_BUILDING_NUMBER).append(tags[i].tag_name + ", ");
	    }
    });
}


function populatePlaceInfo(placeInfo) {
	var templateBuildingInfo = {};
	var buildingAddressInfo = {};
	$("#buildingDetailInfo").empty();
	$("#building_address_link").empty();
	$("#phone_num_link").empty();
	
	if (placeInfo.name != "") {
	    //Handle place info
		templateBuildingInfo.placeName = placeInfo.name;
		templateBuildingInfo.placeImageUrl = placeInfo.image_url;
		$("#buildingInfoTemplate").tmpl(templateBuildingInfo).appendTo( "#buildingDetailInfo" );
		
		buildingAddressInfo.placeAddress = placeInfo.address;
		buildingAddressInfo.placeAddressUrl = "http://maps.google.com?q=" + escape(placeInfo.address) + " Georgia Institute of Technology";
		buildingAddressInfo.phone_num = placeInfo.phone_num;		
		$("#buildingAddressTemplate").tmpl(buildingAddressInfo).appendTo("#building_address_link");
		$("#phoneNumberTemplate").tmpl(buildingAddressInfo).appendTo("#phone_num_link");
		
		//Handle tags
		var placeTagList = {};
	    $("#tags_list").empty();
	    $("#noTaginfo").hide();
	    if(placeInfo.tag_list[0] != "") {
            var currTokens = placeInfo.tag_list;
            for (var i = 0; i < currTokens.length; i++) {
                placeTagList.buildingId = placeInfo.b_id;
                placeTagList.buildingTag = currTokens[i];
                $("#tagInfoTemplate").tmpl(placeTagList).appendTo("#tags_list");
            }
	    } else {
		    $("#noTaginfo").show();
	    }
	} else {
		alert("Place not found!");
	}
}


function saveTag() {
	var newTag = $.trim($("#new_tag").val().toLowerCase());
	if (newTag.length != 0) {
		$.post("api/tags/", { "bid": currentPlaceID, "tag": newTag }, function(data) {
			if("success" == $.trim(data)) {
			    console.log("Saved tag");
			    // Once the ajax request returns successfully, insert the new tag
			    // into the buildingTags table and update the buildings tags string
			    // so that the new tag can be used for searching
                buildings[currentPlaceID].tag_list.push(newTag);
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
                $("#noTaginfo").hide();
			}
		});
	} else {
	    alert("You didn't type a tag yet!");
	}
}


function searchResultClick(placeID) {
	currentPlaceID = placeID;
	console.log(buildings[placeID]);
	populatePlaceInfo(buildings[placeID]);
	library.changeLinksForOffline();
}


// Check if the browser supports offline storage
function supports_html5_storage() {
    try {
        return 'localStorage' in window && window['localStorage'] !== null;
    } catch (e) {
        return false;
    }
}

