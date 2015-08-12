#### Problem

For example, let’s say we have an API response:
var data = [
  {
    name: "Jamestown",
    population: 2047,
    temperatures: [-34, 67, 101, 87]
  },
  {
    name: "Awesome Town",
    population: 3568,
    temperatures: [-3, 4, 9, 12]
  }
  {
    name: "Funky Town",
    population: 1000000,
    temperatures: [75, 75, 75, 75, 75]
  }
];

If we want to use a chart or graphing library to compare the average temperature to population size, we’d need to write some JavaScript that makes a few changes to the data before it’s formatted correctly for our visualization. Our graphing library wants an array of x and y coordinates, like so:
[
  [temp, pop_size],
  [temp, pop_size]
  …etc
]
