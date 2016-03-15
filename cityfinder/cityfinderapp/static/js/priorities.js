//Parts adapted from other sources, as marked

//Sortable list adapted from https://github.com/RubaXa/Sortable

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

/*(Original) This function collects the values that the user has dragged
to their priority list upon clicking the "continue" button and returns this
ordered list to the back end. The user is then moved to the next page.
*/

$('#arrow').on("click", function(e){
    e.preventDefault();
	var priority_block = document.getElementById("sortTrue");
	var priority_list = [];

	for(var i = 1; i < priority_block.childNodes.length; i++){
		list_item = priority_block.childNodes[i];
		priority_list.push(list_item.id)
	}

	console.log(priority_list)

	document.getElementById('priorities').value = priority_list;
	$('#priorities-form').attr('action', "./preferences_citysize/").submit();
});





