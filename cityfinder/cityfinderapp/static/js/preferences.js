//preference sliders

$("#size").slider();

$("#size-disabled").click(function() {
	if(this.checked) {
		$("#size").slider("disable");
	}
	else {
		$("#size").slider("enable");
	}
});

$("#sun").slider();

$("#sun-disabled").click(function() {
	if(this.checked) {
		$("#sun").slider("disable");
	}
	else {
		$("#sun").slider("enable");
	}
});
$("#temp").slider();

$("#temp-disabled").click(function() {
	if(this.checked) {
		$("#temp").slider("disable");
	}
	else {
		$("#temp").slider("enable");
	}
});
$("#seasons").slider();

$("#seasons-disabled").click(function() {
	if(this.checked) {
		$("#seasons").slider("disable");
	}
	else {
		$("#seasons").slider("enable");
	}
});

function get_inputs() {
	var preferences = document.getElementsByTagName("input");
	preference_list = []
	for(i = 0; i < preferences.length; i++){
		item_id = preferences[i].id;
		if (preferences[i].className == "") {
		item_value = preferences[i].value;
		};
		if (preferences[i].className == "slider_element") {
		item_value = preferences[i].checked
		};
		preference_list.push([item_id, item_value])
	};
	document.getElementById("preferences").value = preference_list;

	//console.log things are just checks for now printed to console, can be deleted in final
	console.log(preference_list);
	console.log(preferences)
	
	//document.getElementById("priorities").submit();
	//window.location.href = "???.html"
}