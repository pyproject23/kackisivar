# KAÇ KİŞİ VAR
Anlık bina içinde kaç kişi olduğunu istatistiksel olarak gösteren bir uygulama

### Proje 4 ana bileşenden oluşmaktadır:

1. Deney düzeneğinin oluşturulması ( Kamera sisteminin kurulumu)
2. Görüntü işleme süreci sonunda elde edilen verilerin veri tabanına kayıt edilmesi
3. Uyarı sistemi ile verilerin e-posta ile sorumlu kişilere iletilmesi
4. Saatlik ve günlük istatistiki verilerin sunulması

## Özellikler

* Varsayılan kullanıcı adı: admin parola:admin
* Bilgileri yerel SQLite veritabanında saklama
* Kullanıcı yönetimi
* Log yönetimi
* Ayarlar yönetimi
* Mail ile uyarı ve günlük raporları belirlenen görevliye gönderme
* Anlık giriş çıkış verilerini veritabanına kaydetme
* Demo modda ve canlı modda kişi sayım işlemini yapma
* Anlık giriş, çıkış ve içerideki kişi sayılarını gösterme
* Gün içerisinde saatlik giriş çıkış verilerini grafiksel olarak gösterme
* İçinde bulunulan ay için günlük giriş çıkış verilerini grafiksel olarak gösterme

### [Kurulum - Debian ve Windows 10 üzerinde](KURULUM.md "KURULUM")

## MVC Yapısı

![Kaç Kişi Var](gorseller/mvc.png)

## Ekranlar

![Ekranlar](gorseller/ekranlar.png)

### Login Ekranı

![Login Ekranı](gorseller/login_ekrani.png)

### Ana Ekran

![Ana Ekran](gorseller/ana_ekran.png)

### Ayarlar Ekranı

![Ayarlar Ekranı](gorseller/ayarlar_ekrani.png)

### Kullanıcılar Ekranı

![Kullanıcılar Ekranı](gorseller/kullanicilar_ekrani.png)

### Log Ekranı

![Log Ekranı](gorseller/log_ekrani.png)

### Hakkında Ekranı

![Hakkında Ekranı](gorseller/hakkinda_ekrani.png)

* Not: models klasöründe örnek demo_kackisivar.sqlite veritabanı dosyası vardır.
