import zfec, random

def decode_file(n:int, m:int, all_blocks:list, output_file="recovered.jpeg"):
    """Reconstructs the file using any N parts."""
    
    if len(all_blocks) < n:
        raise ValueError(f"Not enough parts! Need at least {n}, but found {len(all_blocks)}.")

    # Pick any N parts randomly
    # selected_parts = random.sample(all_blocks, n)
    del all_blocks[-m:]
    selected_parts = all_blocks

    # Read selected parts
    indices = []
    blocks = selected_parts
   
    for i, name in enumerate(selected_parts):
      indices.append(i)


 

    # for part in selected_parts:
    #     index = int(part.split("_")[-1].split(".")[0])  # Extract index
    #     with open(part, "rb") as f:
    #         blocks.append(f.read())
    #         indices.append(index)

    # Decode with ZFEC
    dec = zfec.Decoder(n, n + m)
    decoded_blocks = dec.decode(blocks, indices)

    # Join decoded blocks and remove padding
    recovered_data = b"".join(decoded_blocks).rstrip(b'\x00')

    with open(output_file, "wb") as f:
        f.write(recovered_data)

    print(f"Recovered original file as {output_file}")

# Example usage
# decode_file(n=4, m=2)