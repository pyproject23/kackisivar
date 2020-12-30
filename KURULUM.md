## KURULUM

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

10. requirements.txt içerisindeki pkg-resources==0.0.0 satırı silinir.

11. pip ile paket kurulumları yapılır.

` pip install -r requirements.txt `

12. Program çalıştırılır.

` python main.py `
