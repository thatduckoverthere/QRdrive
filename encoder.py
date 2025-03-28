import os
import math
import zfec

ver = 1.0

def encode_file(file_path, chunks, red_chunks):
    """Splits a file into N parts and adds M redundant parts using ZFEC."""

    with open(file_path, "rb") as f:
        data = f.read()

    # Calculate part size and pad if necessary
    part_size = math.ceil(len(data) / chunks)
    data += b'\x00' * (part_size * chunks - len(data))  # Pad to fit exactly into N parts

    # Split into exactly N parts
    parts = [data[i * part_size:(i + 1) * part_size] for i in range(chunks)]

    # Encode using ZFEC
    enc = zfec.Encoder(chunks, chunks + red_chunks)
    return enc.encode(parts)
#     encoded_parts = enc.encode(parts)

#     # Save all N+M parts
#     for i, part in enumerate(encoded_parts):
#         with open(os.path.join("encoded_parts", f"part_{i}.zfec"), "wb") as f:
#             f.write(part)

#     print(f"Encoded {file_path} into {chunks + red_chunks} parts. Any {chunks} can reconstruct the original.")

# # Example usage
# encode_file("test.jpeg", chunks=4, red_chunks=2)
