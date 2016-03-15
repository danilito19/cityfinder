//Original

function get_community_inputs () {
	var communities = document.getElementsByTagName("input")
	var communities_checked = []
	for (i = 0; i < communities.length; i++)
		if (communities[i].checked) {
			communities_checked.push(communities[i].name)
		}
	console.log(communities_checked)
	document.getElementById('community').value = communities_checked;
	$('#community-form').attr('action', "../city_results/").submit();
}