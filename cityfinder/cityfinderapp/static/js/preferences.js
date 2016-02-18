//preference sliders

$("#size").slider();

$("#size-enabled").click(function() {
	if(this.checked) {
		$("#ex7").slider("disable");
	}
	else {
		$("#ex7").slider("enable");
	}
});

$("#sun").slider();

$("#sun-enabled").click(function() {
	if(this.checked) {
		$("#ex7").slider("disable");
	}
	else {
		$("#ex7").slider("enable");
	}
});
$("#temp").slider();

$("#temp-enabled").click(function() {
	if(this.checked) {
		$("#ex7").slider("disable");
	}
	else {
		$("#ex7").slider("enable");
	}
});
$("#seasons").slider();

$("#seasons-enabled").click(function() {
	if(this.checked) {
		$("#ex7").slider("disable");
	}
	else {
		$("#ex7").slider("enable");
	}
});