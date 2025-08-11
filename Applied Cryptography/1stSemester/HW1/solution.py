import numpy as np
from PIL import Image
from itertools import product
from collections import Counter

# Load the encrypted image
cipher_image = np.array(Image.open("cipher.png"))
image_size = cipher_image.shape[0]  # height of the image

# Calculate IC for different key lengths
for key_length in range(1, 21):
    ics = []
    for block_index in range(key_length * key_length):
        counts = Counter(
            cipher_image[i * key_length + block_index // key_length, j * key_length + block_index % key_length]
            for i, j in product(range(image_size // key_length), range(image_size // key_length))
        )
        ic_value = sum((count / (image_size // key_length) ** 2) ** 2 for count in counts.values())
        ics.append(ic_value)
    print(f"Key Length: {key_length}, Mean IC: {np.mean(ics)}, Sum IC: {sum(ics)}")
    # First peak on m = 7 shows that key length was 7

# Assuming key length is determined to be 7
key_length = 7
key = []
for block_index in range(key_length * key_length):
    counts = Counter(
        cipher_image[i * key_length + block_index // key_length, j * key_length + block_index % key_length]
        for i, j in product(range(image_size // key_length), range(image_size // key_length))
    )
    # Most redundant pixel assumed to be 180
    key.append(counts.most_common(1)[0][0] ^ 180)
key = np.array(key, dtype=np.uint8).reshape(key_length, key_length)

# Decrypt the image
for i, j in product(range(image_size // key_length), range(image_size // key_length)):
    cipher_image[i * key_length : (i + 1) * key_length, j * key_length : (j + 1) * key_length] ^= key

# Save the decrypted image
Image.fromarray(cipher_image).save("solved.png")
