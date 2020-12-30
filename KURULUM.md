## KURULUM

### GNU/Linux Dağıtımlarda Kurulum (Debian - Pardus - Mint - Ubuntu)

** Kullanıcının ev dizinine kurulum adımları anlatılacaktır.

1. Komut istemcisi (konsol/terminal) açılır.

2. Git kurulumu yapılır.

` sudo apt install git `

3. Github sayfasından proje dosyaları masaüstüne indirilir.

` git clone https://github.com/pyproject23/kackisivar.git `

4. kackisivar proje klasörü içine girilir.

` cd kackisivar `

5. Sanal ortam oluşturulur.

` python3 -m venv venv `

6. Sanal ortam aktif edilir.

` source venv/bin/activate `

7. Örnek konsol görüntüsü aşağıdaki gibi olmalıdır - en başta (venv) görünmeli.

(venv) __kullanici_adi__@__bilgisayar_adi__:~$

8.  Gerekli pip, setuptools, wheel güncellemeleri yapılır.

` python -m pip install --upgrade pip setuptools wheel `

9. pip ile paket kurulumları yapılır.

` pip install -r requirements.txt `

10. Hata vermesi durumunda requirements.txt içerisindeki pkg-resources==0.0.0 satırı silinir. ` pip install -r requirements.txt ` komutu tekrar çalıştırılır.

11. Program çalıştırılır.

` python main.py `

12. Varsayılan kullanıcı adı ve parola (admin - admin)

### Windows 10'da Kurulum

** Masaüstüne kurulum adımları anlatılacaktır.

1. [Git](https://git-scm.com/downloads "Git i buradan indiriniz")
Linkinden Git kurulumu yapılır.

2. CMD komut istemcisi açılır.

3. Masaüstüne geçiş yapılır.

` cd Desktop ` veya ` cd Masaüstü `

4. Github sayfasından proje dosyaları masaüstüne indirilir.

` git clone https://github.com/pyproject23/kackisivar.git `

5. kackisivar proje klasörü içine girilir.

` cd kackisivar `

6. Sanal ortam oluşturulur.

` python -m venv venv `

7. Sanal ortam aktif edilir.

` venv\Scripts\activate.bat `

8. Örnek konsol görüntüsü aşağıdaki gibi olmalıdır - en başta (venv) görünmeli.

(venv) C:\\Users\\__kullanici_adi__\\Desktop\\kackisivar>

9. Gerekli pip setuptools wheel güncellemeleri yapılır.

` python -m pip install --upgrade pip setuptools wheel `

10. pip ile paket kurulumları yapılır.

` pip install -r requirements.txt `

11. Hata vermesi durumunda requirements.txt içerisindeki pkg-resources==0.0.0 satırı silinir. ` pip install -r requirements.txt ` komutu tekrar çalıştırılır.

12. Program çalıştırılır.

` python main.py `

13. Varsayılan kullanıcı adı ve parola (admin - admin)
