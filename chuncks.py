CHUNK_collection = []
CHUNK_SIZE = 122

# filename = "test.stl"

def Chuncker(filename):
    f = open(filename, 'rb')
    chunk = f.read(CHUNK_SIZE)
    while chunk: #loop until the chunk is empty (the file is exhausted)
        CHUNK_collection.append(chunk)
        chunk = f.read(CHUNK_SIZE) #read the next chunk
    f.close()
    return CHUNK_collection

# print(len(Chuncker(filename)), type(Chuncker(filename)[1]))
