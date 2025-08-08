## Challenge — Image XOR Decryption

### Problem Description
In this challenge, you are given two images: `flag.png` and `parrot.png`.  
Both images have been XOR-encrypted using the **same random key image**.  
The flag is in the format `{flag{MERCER...}}`.  

Your goal is to recover the flag using the two provided images.

**Hint:** Each image is composed of three color channels — Red, Green, and Blue (RGB).

---

### Solution Code

```python
from PIL import Image

def xor_images(image1, image2):
    """XOR two images of the same size."""
    result_image = Image.new("RGB", image1.size)
    pixels_result = result_image.load()

    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            pixels_result[i, j] = tuple(
                a ^ b for a, b in zip(image1.getpixel((i, j)),
                                      image2.getpixel((i, j)))
            )
    return result_image

# Load the two XORed images
image1 = Image.open("parrot.png")  # Replace with your image path
image2 = Image.open("flag.png")    # Replace with your image path

# XOR the two images to recover the original hidden flag image
result_image = xor_images(image1, image2)

# Save or display the result
result_image.save("recovered_flag.png")  # Replace with desired output path
result_image.show()  # This will display the image
