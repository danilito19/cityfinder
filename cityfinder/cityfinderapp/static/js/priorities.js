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

function get_inputs() {
	var priority_block = document.getElementById("sortTrue");
	priority_list = []
	for(i = 1; i < priority_block.childNodes.length; i++){
		list_item = priority_block.childNodes[i];
		priority_list.push(list_item.id)
	}
	document.getElementById("priorities").value = priority_list;

	//console.log things are just checks for now printed to console, can be deleted in final
	console.log(priority_list);
	console.log(Array.isArray(priority_list))
	
	//document.getElementById("priorities").submit();
	window.location.href = "/preferences/"
}
