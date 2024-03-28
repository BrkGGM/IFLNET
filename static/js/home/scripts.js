var aElements = document.getElementById("filtre").getElementsByTagName("a");

for (var a of aElements) {
var textContent = a.textContent;
var newTextContent = textContent.replaceAll("-", " ")

a.textContent = newTextContent;
}



function mAraAc(){
    var bar = document.getElementById("m-ara");
    bar.classList.toggle('ara-aktif');
}


