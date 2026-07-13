# EN
---
# Smart Speed Limit Sign Recognition and Road Status Detection System (PLC & Computer Vision Integration)

This project is a next-generation autonomous driving assistant and road status detection system designed to enhance traffic safety by integrating computer vision, image processing, and Industrial Internet of Things (IIoT) technologies.

Leveraging the power of the **Python** ecosystem, the system establishes a real-time image processing pipeline over a camera stream to detect traffic signs, extract speed limits, and communicate with an industrial **GMT GLC-496T PLC** via the **Modbus TCP/IP** protocol to generate dynamic, physical alerts (lamp and relay control) for the driver.

---

## 🚀 Project Overview & Working Principle

The system detects red-rimmed circular speed limit signs along the roadside in real-time:
* **Intercity Detection (Speed > 55 km/h):** If the detected speed limit is above 55 km/h (e.g., 70, 80), the system switches to intercity mode, and the warning light on the industrial panel illuminates.
* **Urban Zone Detection (Speed < 55 km/h):** If the detected speed limit is below 55 km/h (e.g., 50), the warning light turns off. This informs the driver that they are within an urban zone and must maintain their speed below the 55 km/h threshold.

---

## 🛠️ Software Architecture & Hardware Description

### Software Components

* **Python 3.x**
* **OpenCV (`cv2`):** Handles real-time video streaming, BGR-to-HSV color space conversions, binary color masking (`cv2.inRange`) for red-ring detection, contour extraction (`findContours`), and Region of Interest (ROI) segmentation using the polygon approximation (`approxPolyDP`) algorithm.
* **Tesseract OCR (`pytesseract`):** Converts numerical data (speed limits) inside the segmented, grayscale, and binary-thresholded (`threshold`) sign images into string format. To optimize performance and eliminate false positives, custom Tesseract configuration parameters (`--psm 11 -c tessedit_char_whitelist=0123456789`) are utilized to restrict text extraction to numbers only.
* **NumPy:** Powers high-performance, multi-dimensional array operations on image matrices, handling filtering values and color mask combinations (`mask1 + mask2`).
* **PyModbus:** Serves as the industrial communication bridge between software and hardware. Speed limits parsed by the OCR engine are transmitted instantly over Ethernet to the PLC's data registers (`write_register`) using a Modbus TCP/IP client (`ModbusTcpClient`).
* **GMT Suite:** Used for designing the Ladder logic diagrams and configuring the PLC hardware environment.

### Hardware Components (PLC Panel Circuit)

* **GMT GLC-496T PLC:** The logical control center of the system, executing latching and comparative operations.
* **SPD2430 AC/DC Converter:** An industrial power supply that converts grid alternating current into the stable 24VDC (1.25A) direct current required by the PLC and control inputs.
* **EMAS REIP11 Relays:** Actuators used to safely switch the 220V warning lamp using the PLC's low-voltage transistor outputs.
* **Physical Start/Stop Buttons:** Industrial push buttons configured with latching logic to initialize the system bit and safely halt the execution loop.

---

## 🌐 Network & IP Configuration

To ensure collision-free, low-latency communication over Modbus TCP/IP, all devices are assigned static IP addresses within the same network subnet:

* **GMT PLC IP Address:** `192.168.1.100` (Port: `502`)
* **Host Computer (PC) IP Address:** `192.168.1.101`
* **Modbus Register Mapping:** The `MW2000` operand data block defined within GMT Suite maps directly to Modbus address `42001`. On the Python side, the base memory offset is subtracted, allowing data to be written directly to register address `2000`.

---

## 💻 Installation & Execution

### 1. Installing Dependencies
Ensure that Tesseract OCR is installed on your local operating system. Then, install the required Python packages using pip:

```bash
pip install opencv-python pymodbus pytesseract numpy
```

### 2. Defining the Tesseract Binary Path
Update the `tesseract_cmd` path variable inside the Python script to match your local environment's installation directory:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 3. Running the Pipeline
Power on the PLC control panel, verify that the physical Ethernet link lights are active, and execute the primary Python script:
```bash
python hiz_okuma.py
```

## 📸 Project Media & Gallery

## 👥 Developers & Contributors
* **Yavuz Selim Çakmak - Electrical & Electronics Engineer**
* **Ömeralp Koç - Electrical & Electronics Engineer**

### 📜 License Notice: All rights to the project are reserved. 

---

# TR
---
# Akıllı Hız Levhası Tanıma ve Yol Durum Tespit Sistemi (PLC & Görüntü İşleme Entegrasyonu)

Bu proje, bilgisayar görüsü, görüntü işleme ve Endüstriyel Nesnelerin İnterneti (IIoT) teknolojilerini entegre ederek trafik güvenliğini artırmayı hedefleyen yeni nesil bir otonom sürüş asistanı ve yol durum tespit sistemidir.

**Python** ekosisteminin gücünden faydalanan sistem, kamera akışı üzerinden trafik levhalarını algılamak, hız limitlerini okumak ve sürücüye dinamik fiziksel uyarılar (lamba ve röle kontrolü) üretmek amacıyla **Modbus TCP/IP** protokolü üzerinden endüstriyel bir **GMT GLC-496T PLC** ile haberleşmek için gerçek zamanlı bir görüntü işleme veri boru hattı (pipeline) kurar.

---

## 🚀 Proje Özeti ve Çalışma Mantığı

Sistem, yol kenarındaki kırmızı halkalı hız limit levhalarını gerçek zamanlı olarak tespit eder:
* **Şehir Dışı Tespiti (Hız > 55 km/h):** Algılanan hız sınırı 55 km/h'nin üzerindeyse (örn. 70, 80), sistem şehir dışı moduna geçer ve endüstriyel pano üzerindeki uyarı lambası yanar.
* **Şehir İçi Tespiti (Hız < 55 km/h):** Algılanan hız sınırı 55 km/h'nin altındaysa (örn. 50), uyarı lambası söner. Bu durum sürücüye bir şehir içi bölgesinde olduğunu ve hızını 55 km/h sınırının altında tutması gerektiğini bildirir.

---

## 🛠️ Yazılım Mimarisi ve Donanım Açıklaması

### Yazılım Bileşenleri

* **Python 3.x**
* **OpenCV (`cv2`):** Gerçek zamanlı video akışını, BGR-HSV renk uzayı dönüşümlerini, kırmızı halka tespiti için ikili renk maskelemeyi (cv2.inRange), kontur çıkarımını (findContours) ve çokgen yaklaşımı (approxPolyDP) algoritması kullanarak İlgi Alanı (ROI) segmentasyonunu yönetir.
* **Tesseract OCR (`pytesseract`):** Bölütlenmiş, gri tonlamalı ve ikili eşikleme (threshold) uygulanmış levha görüntülerindeki sayısal verileri (hız limitlerini) metin formatına dönüştürür. Performansı optimize etmek ve hatalı okumaları ortadan kaldırmak için metin çıkarımını sadece rakamlarla sınırlandıran özel Tesseract yapılandırma parametreleri (--psm 11 -c tessedit_char_whitelist=0123456789) kullanılır.
* **NumPy:** Görüntü matrisleri üzerinde yüksek performanslı çok boyutlu dizi operasyonları sağlar, filtreleme değerlerini ve renk maskesi kombinasyonlarını (mask1 + mask2) işler.
* **PyModbus:** Yazılım ile donanım arasındaki endüstriyel haberleşme köprüsü olarak görev yapar. OCR motoru tarafından ayrıştırılan hız limitleri, bir Modbus TCP/IP istemcisi (ModbusTcpClient) kullanılarak Ethernet üzerinden anlık olarak PLC'nin veri kütüklerine (write_register) iletilir.
* **GMT Suite:** Ladder mantık diyagramlarını tasarlamak ve PLC donanım ortamını yapılandırmak için kullanılır.

### Donanım Bileşenleri (PLC Pano Devresi)

* **GMT GLC-496T PLC:** Sistemin mühürleme ve karşılaştırma işlemlerini yürüten mantıksal kontrol merkezidir.
* **SPD2430 AC/DC Konvertör:** Şebekeden gelen alternatif akımı PLC ve kontrol girişleri için gereken stabil 24VDC (1.25A) doğru akıma dönüştüren endüstriyel güç kaynağıdır.
* **EMAS REIP11 Röleler:** PLC'nin düşük voltajlı transistör çıkışlarını kullanarak 220V uyarı lambasını güvenli bir şekilde anahtarlayan aktüatörlerdir.
* **Physical Start/Stop Butonları:** Sistem bitini başlatmak ve çalışma döngüsünü güvenli bir şekilde durdurmak için mühürleme mantığıyla yapılandırılmış endüstriyel butonlardır.

---

## 🌐 Ağ ve IP Yapılandırması

Modbus TCP/IP üzerinden çakışmasız, düşük gecikmeli bir haberleşme sağlamak için tüm cihazlara aynı ağ alt ağında (subnet) sabit IP adresleri atanmıştır:

* **GMT PLC IP Adresi:** `192.168.1.100` (Port: `502`)
* **Ana Bilgisayar (PC) IP Adresi:** `192.168.1.101`
* **Modbus Register Eşleşmesi:** GMT Suite içinde tanımlanan MW2000 operand veri bloğu, doğrudan Modbus üzerindeki 42001 adresine eşleşir. Python tarafında temel bellek offset değeri çıkarılarak verilerin doğrudan 2000 register adresine yazılması sağlanır.

---

## 💻 Kurulum ve Çalıştırma

### 1. Bağımlılıkların Yüklenmesi
Yerel işletim sisteminizde Tesseract OCR'ın kurulu olduğundan emin olun. Ardından, gerekli Python paketlerini pip kullanarak yükleyin:

```bash
pip install opencv-python pymodbus pytesseract numpy
```

### 2. Tesseract Binary Yolunun Tanımlanması
Python betiği içindeki tesseract_cmd yol değişkenini, yerel ortamınızın kurulum dizinine uyacak şekilde güncelleyin:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 3. Pipeline Çalıştırması
PLC kontrol panosuna enerji verin, fiziksel Ethernet bağlantı ışıklarının aktif olduğunu doğrulayın ve ana Python betiğini çalıştırın:
```bash
python hiz_okuma.py
```

## 📸 Projenin Görüntüleri ve Galerisi

## 👥 Geliştiriciler ve Katkıda Bulunanlar
* **Yavuz Selim Çakmak - Elektrik-Elektronik Mühendisi**
* **Ömeralp Koç - Elektrik-Elektronik Mühendisi**

### 📜 Lisans Bildirimi: Projenin tüm hakları saklıdır. 

