var aElements = document.getElementById("filtre").getElementsByTagName("a");

for (var a of aElements) {
var textContent = a.textContent;
var newTextContent = textContent.replaceAll("-", " ")

a.textContent = newTextContent;
}

console.log('aabb')
// JavaScript to toggle blur effect



