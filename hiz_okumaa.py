



import cv2
import pytesseract
import numpy as np
from pymodbus.client import ModbusTcpClient
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

PLC_IP = '192.168.1.100' 
PLC_PORT = 502
REGISTER_ADRESI = 2000

client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
client.connect()

def tabela_oku(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2
   
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detected_speed = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
            
            if len(approx) > 5:
                x, y, w, h = cv2.boundingRect(cnt)
                roi = frame[y:y+h, x:x+w]
                gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(gray_roi, 150, 255, cv2.THRESH_BINARY)

                text = pytesseract.image_to_string(thresh, config='--psm 11 -c tessedit_char_whitelist=0123456789')
                
                text = text.strip()
                if text.isdigit():
                    detected_speed = int(text)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, f"Hiz: {detected_speed}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    return detected_speed

    return 0

cap = cv2.VideoCapture(0)

print("Sistem baslatildi")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hiz_degeri = tabela_oku(frame)

        if hiz_degeri > 0:
            print(f"Algılanan Hız: {hiz_degeri}")
            
            try:
                if not client.connected:
                    print("Baglanti tazeleniyor...")
                    client.connect()
                
            
                client.write_register(REGISTER_ADRESI, hiz_degeri)
                
            except Exception as e:
                print(f"PLC Haberlesme Hatasi: {e}")
                client.close()
            

        cv2.imshow('Hiz Tabelasi Tespit', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program durduruluyor")

finally:
    cap.release()
    cv2.destroyAllWindows()
    client.close()