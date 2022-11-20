// import * as d3 from "d3";

console.log(d3);

// d3.select("div")
//     .selectAll("p")
//     .data([1, 2, 3])
//     .enter()
//     .append("p")
//     .text(data => data);

var svg = d3.select("div")
  .selectAll("p")
  .data([1, 2, 3, 4, 5, 6])
  .enter()
  .append("p")
  .text(data => data);

d3.select("div")
  .insert("a");
d3.select("div")
  .html("This was added by d3");

d3.select("body")
    .selectAll("p")
    .data([1, 2, 3, 4])
    .enter()
    .insert("p")
    .text(data => data);

var data = [100, 200, 300, 400];
var paragraph = d3.select("body")
    .selectAll("p")
    .data(data)
    .text(function (d, i) {
        console.log(d + i);

        return 1;
    });

d3.selectAll("div, p")
    .on("mouseover", function() {
        d3.select(this)
            .transition()
            .duration(500)
            .style("background-color", "yellow");

        console.log(d3.event);

        console.log(d3.mouse(this));
    })
    .on("mouseout", function() {
        d3.select(this)
            .transition()
            .duration(125)
            .style("background-color", "red");
    });

d3.select("body")
    .transition()
    .duration(30000)
    .style("background-color", "blue");

console.log("hello world");
