
const hesabimAyarlar = document.getElementById('hesabimAyarlar');

function toggleBlurEffect() {
    const elementsToBlur = document.querySelectorAll('body > *:not(.hesabim-ayarlar)');
    elementsToBlur.forEach(element => {
        element.classList.toggle('blur-effect');
    });
    const ayarlar = document.getElementById("ayarlar")
    ayarlar.classList.toggle('goster')
}

// Toggle blur effect when .hesabim-ayarlar is clicked
hesabimAyarlar.addEventListener('click', toggleBlurEffect);

function hes_gecis_yap(){
    document.getElementById("bil").className = ('aktif');
    document.getElementById("deg").classList.remove('aktif');
    const icerik1 = document.getElementById("icerik1")
    const icerik2 = document.getElementById("icerik2")
    icerik1.style.display = 'block';    
    icerik2.style.display = 'none';
}

function deg_gecis_yap(){
    document.getElementById("deg").className = ('aktif');
    document.getElementById("bil").classList.remove('aktif');
    const icerik1 = document.getElementById("icerik1")
    const icerik2 = document.getElementById("icerik2")
    icerik1.style.display = 'none';
    icerik2.style.display = 'block'; 
}

$("#bas").click(function() {
    window.location.href = 'http://www.google.co.uk'
  });