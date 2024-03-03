# IFL Bilgi Ağı

### IFL Bilgi Ağı Nedir?
İnsanların bilgi alış verişi yapabileceği şuanda geliştirilmekte olan bir websitesidir. İstiyen kişiler kendi yazılarını paylaşabilecek veyahut başkalırının yazılarını okuyabilecek. Yazılar kategorilere ayrılacak: teknoloji, gündem, kişisel gelişim, genel kültür, sport... Bu sayede websitesini kullanan herkes bilgi edinecek. Websitesindeki gereksiz, boş yazılar websitesi yetkilileri tarafından kaldırılacaktır. Websitesinde herhangi bir sansür politikası olmayacak lakin herkes kendi yazdığı yazıdan sorumlu tutulacaktır! Kişilere hakaret içeren veya yasadışı yazılardan kişi sorumlu olacaktır.

### Kendi bilgisayarınızda çalıştırmak için

#### 1. Python indirin
Uyarı : Python'u indirirken altta "Add Python to PATH" diye bir kutucuk olacak o kutucuğu işaretleyin!
[Mac Os](https://www.python.org/downloads/macos/)
[Windows](https://www.python.org/downloads/windows/)

#### 2. Dosyaları indirip klasörü
Üstteki yeşil 'Code' yazısına basarsanız orada 'download zip' seçeneği var oradan indirip dosyaları uygun bir klasöre çıkartabilirsiniz ya da bilgisayarınızda git indirili ise

```bash git clone https://github.com/BrkGGM/IFLNET/```
komudu ile de kopyalayabilirsiniz.

Daha sonra terminal/cmd/powershell'i o klasörün içinde açın.

Windows:
Dosya yöneticisinden klasörü açtıktan sonra dosya yöneticisinde boş bir alana shift + click yapıp 'Komut işleminde açın'ı seçin ya da direk CMD'yi açıp 

```bash cd C:\buraya\dosya\yolunu\yazın```

Mac OS:
```bash cd /dosya/yolunu/girin```

Linux:
```bash cd /dosya/yolunu/girin```

#### 3. Sanal ortama girin (Opsiyonel)
Linux

```bash pip3 install virtualenv --break-system-packages```

ya da varsayılan paket yöneticiniz ile python-venv paketini indirin

```bash python3 -m venv venv```

```bash source venv/bin/activate```


Mac Os 
```bash pip3 install virtualenv```

```bash python3 -m venv venv```

```bash source venv/bin/activate```


Windows
```bash pip install virtualenv```

```bash python -m venv venv```


```bash 
#CMD Kullanıyorsanız
venv\Scripts\activate.bat
#Powershell Kullanıyorsanız
venv\Scripts\Activate.ps1
```
#### 4. Gerekli paketleri indirin
Windows:

```bash pip install -r requirements.txt```

Linux/Mac OS: 

```bash pip3 install -r requirements.txt```

#### 5. Database'i oluşturun

Windows:

```bash python db_olustur.py```

Linux / Mac OS:

```bash python3 db_olustur.py```

#### 6. Çalıştırın

Windows :

```bash python app.py```

Linux / Mac OS :

```bash python3 app.py```

Tamamdır bu kadar basit bundan sonra tek yapmanız gereken tarayıcınızdan [127.0.0.1:5000](127.0.0.1:5000) adresine girmek. IFLNET'i kendi bilgisayarınızda çalıştırıyorsunuz.

UYARI : Böyle yaparak websitesini sadece kendi bilgisayarınızda açıyorsunuz ve kendi internetinize açmak için bile birkaç ayar değiştirmeniz lazım, sunucuda açmak için de koddaki en son yorum satırına alınan bölgelerdeki yorum satırlarını silip en son satırı yorum satırına almanız lazım. Eğer bunu bir sunucuda çalıştırmayı düşünüyorsanız ve ne yapacağınızı bilmiyorsanız her zaman benden yardım isteyebilirsiniz. 300 TL + hosting & domain fiyatı karşılığında sizin için websitesinin adını değiştirerek size veya okulunuza özel websitesini ayarlayabilirim.
