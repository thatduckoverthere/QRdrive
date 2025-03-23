import qrcode, qrcode.image.svg
import pyqrcode
import hashlib
import chuncker
import os, math

input_file = 'test.jpeg'

size = os.path.getsize(input_file)*8
# size in bits

req_parts=math.ceil(size/367)
# requierd parts
print(size, req_parts)

encoded_parts = chuncker.encode_file(file_path=input_file, parts=req_parts, red_parts=4)

# Save all encoded parts
for i, part in enumerate(encoded_parts):
    with open(os.path.join("encoded_parts", f"part_{i}.bin"), "wb") as f:
        f.write(part)








# QR_collection = []

# file_meta_data = file + "#" + hashlib.md5(open(file,'rb').read()).hexdigest()
# # QR_collection.append(qrcode.make(file_meta_data, version=10, error_correction=qrcode.ERROR_CORRECT_H, border=4))
# QR_collection.append(pyqrcode.create(file_meta_data, error='L', version=10, mode='binary'))

# for chunk in chuncks.Chuncker(filename=file):
#     # QR_collection.append(qrcode.make(chunk, version=10, error_correction=qrcode.ERROR_CORRECT_H, border=4))
#     QR_collection.append(pyqrcode.create(chunk, error='L', version=10, mode='binary', encoding='iso-8859-1'))
    
# for index in range(len(QR_collection)):
#     img=QR_collection[index]
#     # img.save(f'QR/MyQRCode{index}.png')
#     img.png(f'QR/MyQRCode{index}.png', scale=4)
    