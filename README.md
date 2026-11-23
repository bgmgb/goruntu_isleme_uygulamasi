# Qt ve OpenCV ile Görüntü İşleme Uygulaması

Python, PySide6 (Qt) ve OpenCV ile yazılmış bir masaüstü uygulaması.
Seçilen resim üzerinde ayarlanabilir bulanıklaştırma, gri seviyeye çevirme ve kenar bulma işlemleri yapar.
Orijinal resim solda sonuç resmi sağda olmak üzere yan yana gösterilir. İstenirse işlem sırasında resme uygulanan işlemler sıfırlanabilir.
Sonuç resmi kaydedilebilir.

## Özellikler

- PNG, JPG ve JPEG resim açma
- Gri seviyeye dönüştürme
- Kaydırıcı ile kernel boyutu ayarlanarak bulanıklaştırma (Gaussian)
- Canny ile kenar bulma
- Sonucu dosyaya kaydetme
- Hata kontrolleri: geçersiz dosya açma, resim açmadan işlem yapma, kayıt hataları

## Gereksinimler

- Ubuntu (VirtualBox üzerinden test edildi.)
- Python 3
- Kurulum için internet bağlantısı

## Kurulum

 Proje klasöründe şu komutlar çalıştırılmalıdır:

```bash
chmod +x kurulum.sh
./kurulum.sh
``` 

Betik önce internet bağlantısını kontrol eder. Bağlantı varsa gerekli paketleri kurar (OpenCV ve PySide6). Kurulumun başarısını kontrol etmek için basit bir python kodunu dener. Kurulum başarılıysa ekrana "Kurulum Başarılı" yazısı gelmelidir.

## Çalıştırma

```bash
python3 main.py
```

## Kullanım

1. **Resim Aç** butonuyla bir resim seçilir. Seçilen resim iki kutuda da görünür.
2. **Grileştir** veya **Kenar Bul** butonuna basarak sonuç resmi sağ kutuda görünür.
3. Bulanıklaştırma için Kaydırıcıyı oynatarak istenilen seviyede bulanıklaştırılır ve sonuç resmi sağ kutuda görünür.
4. **Görünütyü Sıfırla** butonu ile işlem aralarında görüntü orijinal halinde döndürülebilir.
5. **Sonucu Kaydet** butonu ile sağ kutudaki sonuç resmi dosyaya kaydedilebilir.

## Ekran Görüntüsü

![Uygulama](ekran_goruntusu.png)
## Bilinen sorunlar
 
- Kaydırı sıfırdan başlayarak kaydırılmıyor önce orta bir değere getirmek gerekiyor.
- Resimler bazen olduğundan daha basık gözükebiliyor..

## Dosyalar

- `main.py`: uygulama kodu
- `kurulum.sh`: kurulum betiği

## Hazırlayan

Begüm Gaba, 251307020, Grup 6



