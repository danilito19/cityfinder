//Sortable List

// sort: true
Sortable.create(sortTrue, {
  group: "sorting",
  sort: true
});

// sort: false
Sortable.create(sortFalse, {
  group: "sorting",
  sort: false
});

$('#arrow').on("click", function(e){
    e.preventDefault();
	var priority_block = document.getElementById("sortTrue");
	var priority_list = [];

	for(var i = 1; i < priority_block.childNodes.length; i++){
		list_item = priority_block.childNodes[i];
		priority_list.push(list_item.id)
	}

	document.getElementById('priorities').value = priority_list;
	$('#priorities-form').attr('action', "./preferences/").submit();
	// window.location.href = "/preferences/"
});





