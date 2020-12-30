## KURULUM

### Windows 10'da Kurulum

* *Masaüstüne kurulum adımları anlatılacaktır.

* [Git](https://git-scm.com/downloads "Git i buradan indiriniz")
Linkinden Git kurulumu yapılır.

* CMD komut istemcisi açılır.

* Masaüstüne geçiş yapılır.
{ cd Desktop } veya { cd Masaüstü }

* Github sayfasından proje dosyaları masaüstüne indirilir.
{ git clone https://github.com/pyproject23/kackisivar.git }

* kackisivar proje klasörü içine girilir.
{ cd kackisivar }

* Sanal ortam oluşturulur.
{ python -m venv venv }

* Sanal ortam aktif edilir.
{ venv\\Scripts\\activate.bat }
* *Örnek konsol görüntüsü - en başta (venv) görünmeli.
(venv) C:\\Users\\__kullanici_adi__\\Desktop\\kackisivar>

* Gerekli pip güncellemeleri yapılır.
{ python -m pip install --upgrade pip setuptools wheel }

* requirements.txt içerisindeki pkg-resources==0.0.0 satırı silinir.

* pip ile paket kurulumları yapılır.
{ pip install -r requirements.txt }

* Program çalıştırılır.
{ python main.py }
