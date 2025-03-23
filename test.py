import os
import math
import zfec

def encode_file(file_path, n, m, output_dir="encoded_parts"):
    """Splits a file into N parts and adds M redundant parts using ZFEC."""
    os.makedirs(output_dir, exist_ok=True)

    with open(file_path, "rb") as f:
        data = f.read()

    # Calculate part size and pad if necessary
    part_size = math.ceil(len(data) / n)
    data += b'\x00' * (part_size * n - len(data))  # Pad to fit exactly into N parts

    # Split into exactly N parts
    parts = [data[i * part_size:(i + 1) * part_size] for i in range(n)]

    # Encode using ZFEC
    enc = zfec.Encoder(n, n + m)
    encoded_parts = enc.encode(parts)

    # Save all N+M parts
    for i, part in enumerate(encoded_parts):
        with open(os.path.join(output_dir, f"part_{i}.zfec"), "wb") as f:
            f.write(part)

    print(f"Encoded {file_path} into {n + m} parts. Any {n} can reconstruct the original.")

# Example usage
encode_file("test.jpeg", n=4, m=2)

import glob
import random

def decode_file(n, m, input_dir="encoded_parts", output_file="recovered.jpeg"):
    """Reconstructs the file using any N parts."""
    all_parts = sorted(glob.glob(os.path.join(input_dir, "part_*.zfec")))

    if len(all_parts) < n:
        raise ValueError(f"Not enough parts! Need at least {n}, but found {len(all_parts)}.")

    # Pick any N parts randomly
    selected_parts = random.sample(all_parts, n)

    # Read selected parts
    blocks = []
    indices = []

    for part in selected_parts:
        index = int(part.split("_")[-1].split(".")[0])  # Extract index
        with open(part, "rb") as f:
            blocks.append(f.read())
            indices.append(index)

    # Decode with ZFEC
    dec = zfec.Decoder(n, n + m)
    decoded_blocks = dec.decode(blocks, indices)

    # Join decoded blocks and remove padding
    recovered_data = b"".join(decoded_blocks).rstrip(b'\x00')

    with open(output_file, "wb") as f:
        f.write(recovered_data)

    print(f"Recovered original file as {output_file}")

# Example usage
decode_file(n=4, m=2)
