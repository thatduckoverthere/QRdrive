import glob
import random
import os
import zfec

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
decode_file(n=233, m=4)