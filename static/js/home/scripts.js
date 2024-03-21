$(document).ready(function(){
    var aElements = document.getElementById("filtre").getElementsByTagName("a");

    for (var a of aElements) {
    var textContent = a.textContent;
    var newTextContent = textContent.replace("-", " ")
    
    a.textContent = newTextContent;
    }

    // JavaScript to toggle blur effect


});
