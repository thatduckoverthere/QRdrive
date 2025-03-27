import qrcode, qrcode.image.svg
import pyqrcode
import hashlib
import encoder
import os
import math
import datetime

input_file = 'test.jpeg'

size = os.path.getsize(input_file)*8
# size in bits

req_parts=math.ceil(size/367)
# requierd parts
print(size, req_parts)
red_chunks = 4

encoded_parts = encoder.encode_file(file_path=input_file, chunks=req_parts, red_chunks=red_chunks)

os.makedirs("encoded_parts", exist_ok=True)
QR_collection = []

file_meta_data = {
    "filename": input_file,
    "file_type": os.path.splitext(input_file)[1],
    "file_size": size,
    "file_hash": hashlib.md5(open(input_file,'rb').read()).hexdigest(),
    "redundant_chunks": red_chunks,
    "encoder_version": encoder.ver,
    "date_encoded": str(datetime.datetime.now()),
    "comment": ""
    
}

print(file_meta_data)
QR_collection.append(pyqrcode.create(str(file_meta_data), error='M', version=13, mode='binary'))


for part in encoded_parts:
    QR_collection.append(pyqrcode.create(part, error='L', version=13, mode='binary', encoding='iso-8859-1'))


    
for index in range(len(QR_collection)):
    img=QR_collection[index]
    # img.save(f'QR/MyQRCode{index}.png')
    img.png(f'QR/MyQRCode{index}.png', scale=4)
    



# for i, part in enumerate(encoded_parts):
#     QR_collection.append(pyqrcode.create(part, error='L', version=10, mode='binary', encoding='iso-8859-1'))
#     with open(os.path.join("encoded_parts", f"part_{i}.zfec"), "wb") as f:
#         f.write(part)







# for chunk in chuncks.Chuncker(filename=file):
#     # QR_collection.append(qrcode.make(chunk, version=10, error_correction=qrcode.ERROR_CORRECT_H, border=4))
#     QR_collection.append(pyqrcode.create(chunk, error='L', version=10, mode='binary', encoding='iso-8859-1'))
    
# for index in range(len(QR_collection)):
#     img=QR_collection[index]
#     # img.save(f'QR/MyQRCode{index}.png')
#     img.png(f'QR/MyQRCode{index}.png', scale=4)
