#!/bin/bash 
set -e #hata varsa devam etmesin diye
hata_yakalama()
{ echo "HATA!"
echo "Kurulum Adımlarından Biri Basarisiz Oldu"
exit 1
}
trap hata_yakalama ERR #betikte herhangi bir hata olursa yukarıdaki fonksiyon çalışsın dedik

#internet kontrolü
if ! ping -c 1 google.com > /dev/null 2>&1; then
echo "HATA! Internet bağlantısı yok!"
exit 1
fi

echo "Kurulum Betigi Calısıyor..."
echo "Sistem Guncelleniyor"
sudo apt update -y  #apt update ile paket listesini güncelledim
echo "Python ve pip kuruluyor..."  #pip:python paket yükleyici
sudo apt install -y libgl1 libxcb-cursor0 #pyside6 ve opencv'nin çalışırken ihtiyaç duyduğu linux parçaları
sudo apt install -y python3 python3-pip python3-venv #-y direkt evet kabul etsin diye
echo "OpenCV ve Qt yükleniyor.."
pip3 install opencv-python-headless PySide6 --break-system-packages
#pyside6 qt'yi pythonda kullanabilmek için

#kurulu çalışıyor mu kontrol
echo "kurulum kontrol ediliyor"
python3 -c "import cv2, PySide6" #tırnak içindeki python komutu çalıştırıp cevaba göre başarılı diyoruz yüklenemezse hata vercek
echo "Kurulum Başarılı"
