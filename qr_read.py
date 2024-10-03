import cv2, os

detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(cv2.imread("QR/MyQRCode0.png"))
filename="out/"+data[:data.find("#")]
print(filename)

f = open(filename, "w")
for index in range(1,len(os.listdir("QR"))):
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2.imread(f"QR/MyQRCode{index}.png"))
    f.write(data)
    print(index)
f.close