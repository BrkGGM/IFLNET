$(document).ready(function(){
    var liElements = document.getElementById("filtre").getElementsByTagName("a");

    for (var a of liElements) {
    var textContent = a.textContent;
    var newTextContent = textContent.replace("-", " ");
    a.textContent = newTextContent;
    }

});
