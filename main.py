import sys
import cv2
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QHBoxLayout, QVBoxLayout, QSlider, QMessageBox
from PySide6.QtGui import QPixmap, QImage
class GoruntuUygulamasi(QWidget):
    def __init__(self): 
        super().__init__()
        self.original_img= None
        self.sonuc_img= None
        
        #pencere ayarları yapalım
        self.setWindowTitle("Görüntü İşleme")
        self.resize(800, 500)
        
        #label yapalım orijinal için
        self.img1_lbl = QLabel(self)
        self.img1_lbl.move(20,30)
        self.img1_lbl.resize(520,400)
        self.img1_lbl.setStyleSheet("border: 1px solid blue;") #label kenarına 1 piksel kalınlığında mavi düz kenar çiz demek
        
        #label yeni resim için
        self.img2_lbl= 	QLabel(self)
        self.img2_lbl.move(650, 30)
        self.img2_lbl.resize(520, 400)
        self.img2_lbl.setStyleSheet("border: 1px solid purple;")
        
        #bulanıklaştırma için slider oluşturcaz
        self.slider = QSlider(Qt.Orientation.Horizontal, self) #slider yatay olsun demek
        self.slider.setMinimum(0)
        self.slider.setMaximum(15)
        self.slider.resize(300,30)
        self.slider.move(750,480)
        self.slider.valueChanged.connect(self.bulaniklastir) #valuechanged butonclicked gibi
        
        self.slider_txt = QLabel("Bulanıklaştır", self )
        self.slider_txt.move(720,470)
        
        self.slider_deger= QLabel("0", self)
        self.slider_deger.resize(50,25)
        self.slider_deger.move(710,485)
        
        #grileştirme, resim açma, sıfırlama, kaydetme, kenar bulma butonları ekleme
        self.btn= self.buton_olustur("Resim Aç", 50, 480, 150, 40, self.resim_ac)
        self.gray_btn= self.buton_olustur("Grileştir", 750, 520, 150, 40, self.grilestir)
        self.edge_btn=self.buton_olustur("Kenar Bul", 750, 570, 150, 40, self.kenar_bul)
        self.restart_btn= self.buton_olustur("Sıfırla", 750, 620, 150, 40, self.sifirla)
        self.save_btn= self.buton_olustur("Sonuç Kaydet", 750, 670, 150, 40, self.kaydet)

    def buton_olustur(self, metin, x, y, genislik, yukseklik, slot=None):
        btn = QPushButton(metin, self)
        btn.move(x, y)
        btn.resize(genislik, yukseklik)
        if slot is not None:
            btn.clicked.connect(slot)
        return btn
        
         
    def resim_ac(self):
    #dosyalardan resim seçme
        dosya_yolu, _ =QFileDialog.getOpenFileName(self, "Resim Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg)")
        if dosya_yolu:
           print("seçilen dosya:", dosya_yolu)#burada opencv ile resmi okutup ekrandaki etikete basacağız           
           img = cv2.imread(dosya_yolu)  #opencv ile resmi oku
           #resim basarıyla okundu mu
           if img is None:
               QMessageBox.warning(self, "HATA","Önce resim seçiniz!")
               return
           self.original_img= img #orijinele her yerden erişebilelim diye ve yol kesinleştikten sonra orijinale atadık
           self.sonuc_img = img
           self.resim_goster(img, self.img1_lbl)
           self.resim_goster(img, self.img2_lbl)
               
          
    def resim_goster(self, img, label):
        if img.ndim ==2: #resim 2boyutluysa yani griyse
            #gri olduğu için renk çevirme veya kanal yok
            h, w = img.shape
            bytes_per_line= w
            
            q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format.Format_Grayscale8).copy()
            
        else:
             img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #opencv renk formatı(BGR), qt renk formatı (RGB) fakrını dönüştürcez
             h, w, ch = img_rgb.shape #shape ile resmin boyutlarını 3 değere atıyoruz
             bytes_per_line = ch * w #bir satırda kaç bytelık yer olduğunu söyluyoruz çünkü 1 widelik yerde RGB kadar yer kaplar
             q_img = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888).copy() #qt formatına çevir
        label.setPixmap(QPixmap.fromImage(q_img))#QImageı arayüzde ekrana basan QPixmap formatına çevirip arayüzdeki etiket alanına resim_alani yapıştırdık ekranda görünsün diye
        label.setScaledContents(True)#resmi ekkran boyutuna sığdırsın diye
        
    def bulaniklastir(self):
        if self.original_img is None: #resim seçilmezse çalışmaz
            QMessageBox.warning(self, "HATA ", "Önce resim seçiniz !")
            return
        k = self.slider.value() * 2 + 1 #kernel yan (k,k) çift sayı kabul etmez çünkü matris ortası buluyo
        self.slider_deger.setText(str(k))
        bulanik= cv2.GaussianBlur(self.original_img, (k,k), 0)
        self.sonuc_img = bulanik
        self.resim_goster(bulanik, self.img2_lbl)
        
    def grilestir(self):
        if self.original_img is None:
            QMessageBox.warning(self, "HATA","Önce resim seçiniz!")
            return
        gray_img = cv2.cvtColor(self.original_img, cv2.COLOR_BGR2GRAY)
        self.sonuc_img = gray_img
        self.resim_goster(gray_img, self.img2_lbl)
        
    def kenar_bul(self):
        if self.original_img is None:
            QMessageBox.warning(self, "HATA", "Önce resim seçiniz")
            return
        gray_img = cv2.cvtColor(self.original_img, cv2.COLOR_BGR2GRAY)
        edge_img = cv2.Canny(gray_img, 100, 200) #100 ve 200 eşik değeri büyük olursa az, küçük olursa çok kenar bulur
        self.sonuc_img = edge_img
        self.resim_goster(edge_img, self.img2_lbl)
        
    def sifirla(self):
        if self.original_img is None:
            QMessageBox.warning(self, "HATA", "Önce resim seçiniz")
            return
        self.sonuc_img = self.original_img
        self.resim_goster(self.original_img, self.img2_lbl)
    
    def kaydet(self):
        if self.sonuc_img is None:
           QMessageBox.warning(self, "HATA", "Kaydedilecek sonuç yok")
           return
        yol, _ = QFileDialog.getSaveFileName(self, "Sonucu kaydet", "", "PNG (*.png);;JPEG (*.jpg)") 
        if not yol:
            return #kullanıcı vazgeçerse 
        if not yol.lower().endswith((".png", ".jpg", ".jpeg")):
            yol += ".png"
        kaydedildi = cv2.imwrite(yol, self.sonuc_img)
        if kaydedildi:
            QMessageBox.information(self, "Bilgi", "sonuç kaydedildi")
        else:
            QMessageBox.information(self, "Bilgi", "sonuç kaydedilemedi")
app = QApplication(sys.argv)
#sınıftan nesnemizi(pencereyi) türetiyoruz
pencere = GoruntuUygulamasi()
pencere.show() #pencere ekrana gelecek

sys.exit(app.exec())
