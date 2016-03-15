//Parts adapted from other sources, as marked

//Preference sliders adapted from http://seiyria.com/bootstrap-slider/

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

/* (Original) These function collect the preferences from the weather  and city sliders and "indifferent"
checkboxes that correspond to them. They returns this information as a list to the back end.
The list includes only items for which the user as not checked "indifferent." Each string is
followed by a number indicating the user's preference with regard to that attribute, i.e. ["sun", 1].
The user is then moved to the next page.
*/

function get_weather_inputs() {
	var inputs = document.getElementsByTagName("input");
	var preferences = []
	for (i = 0; i < inputs.length; i++) {
		if (inputs[i].type.toLowerCase() == "checkbox") {
			if (!(inputs[i].checked)) {
				preferences.push(inputs[i-1].id);
				preferences.push(inputs[i-1].value);
			};
		};
	};
	console.log(preferences)

	document.getElementById('weather').value = preferences;
	$('#weather-form').attr('action', "../preferences_community/").submit();
};

function get_city_size() {
	var inputs = document.getElementsByTagName("input");
	var preferences = []
	for (i = 0; i < inputs.length; i++) {
		if (inputs[i].type.toLowerCase() == "checkbox") {
			if (!(inputs[i].checked)) {
				preferences.push(inputs[i-1].id);
				preferences.push(inputs[i-1].value);
			};
		};
	};
	console.log(preferences)

	document.getElementById('citysize').value = preferences;
	$('#citysize-form').attr('action', "../preferences_weather/").submit();
};

