
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
    icerik1.style.display = 'block';    
}

function deg_gecis_yap(){
    document.getElementById("deg").className = ('aktif');
    document.getElementById("bil").classList.remove('aktif');
    const icerik1 = document.getElementById("icerik1")
    icerik1.style.display = 'none';
}