import encoder, decoder, os, math

input_file = 'test.jpeg'

size = os.path.getsize(input_file)
# size in bits

req_parts=math.ceil(size/367)
# requierd parts
print(size, req_parts)
red_chunks = 4

encoded_parts = encoder.encode_file(file_path=input_file, chunks=req_parts, red_chunks=red_chunks)

print("here", type(encoded_parts[0]))
decoder.decode_file(req_parts, red_chunks, encoded_parts)
