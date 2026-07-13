# EN
---
# Smart Speed Limit Sign Recognition and Road Status Detection System (PLC & Computer Vision Integration)

This project is a next-generation autonomous driving assistant and road status detection system designed to enhance traffic safety by integrating computer vision, image processing, and Industrial Internet of Things (IIoT) technologies.

Leveraging the power of the Python ecosystem, the system establishes a real-time image processing pipeline over a camera stream to detect traffic signs, extract speed limits, and communicate with an industrial **GMT GLC-496T PLC** via the **Modbus TCP/IP** protocol to generate dynamic, physical alerts (lamp and relay control) for the driver.

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
