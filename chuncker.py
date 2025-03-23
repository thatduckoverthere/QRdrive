import os
import reedsolo

def encode_file(file_path, parts, red_parts):
    """Splits a binary file into N fixed-size parts with M redundant parts."""

    with open(file_path, "rb") as f:
        data = f.read()

    part_size = len(data) // parts  # Ensure fixed-size parts
    parts = [data[i * part_size:(i + 1) * part_size] for i in range(parts)]

    # Use Reed-Solomon to generate M redundant parts
    rs = reedsolo.RSCodec(red_parts)  # M redundant symbols
    encoded_parts = [rs.encode(part) for part in parts]
    
    return encoded_parts
    # return a list of all parts