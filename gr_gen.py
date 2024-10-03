import qrcode, qrcode.image.svg
import hashlib
import chuncks

QR_collection = []
file = "test.jpeg"

file_meta_data = file + "#" + hashlib.md5(open(file,'rb').read()).hexdigest()
QR_collection.append(qrcode.make(file_meta_data, version=10, error_correction=qrcode.ERROR_CORRECT_H, border=4))

for chunk in chuncks.Chuncker(filename=file):
    QR_collection.append(qrcode.make(chunk, version=10, error_correction=qrcode.ERROR_CORRECT_H, border=4, mode='binary'))
    
for index in range(len(QR_collection)):
    img=QR_collection[index]
    img.save(f'QR/MyQRCode{index}.png')
    