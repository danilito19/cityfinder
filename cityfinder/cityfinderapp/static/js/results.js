

console.log(results);

console.log(print_string)

var test = [1, 2, 3, 4]

d3.select("#chart_area").selectAll("p").data(results).enter().append("p").text("city!!!!")

define(['d3', 'wq/pandas'], function(d3, pandas) {
    pandas.parse(results);
});