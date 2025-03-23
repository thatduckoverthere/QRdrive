import glob
import random
import reedsolo
import os


def decode_file(n, m, input_dir="encoded_parts", output_file="recovered.bin"):
    """Reconstructs the original file using any N parts from N+M."""
    all_parts = sorted(glob.glob(os.path.join(input_dir, "part_*.bin")))
    
    if len(all_parts) < n:
        raise ValueError(f"Not enough parts! Need at least {n}, but found {len(all_parts)}.")

    # Pick any N parts randomly
    selected_parts = random.sample(all_parts, n)

    rs = reedsolo.RSCodec(m)  # M redundant symbols
    decoded_data = b"".join(rs.decode(open(p, "rb").read()) for p in selected_parts)

    with open(output_file, "wb") as f:
        f.write(decoded_data)

    print(f"Recovered original file as {output_file}")

# Example usage
decode_file(n=233, m=4)
