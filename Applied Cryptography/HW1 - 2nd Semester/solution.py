# -----------------------------------------------------------------------------
# Copyright (c) [2024] [milad_mercer]
# All Rights Reserved.
# -----------------------------------------------------------------------------

import imageio

# Load the images
flag = imageio.imread('PATH TO FLAG IMAGE')
parrot = imageio.imread('PATH TO PARROT IMAGE')

# Perform XOR operation on the images
result = parrot ^ flag

# Save the resulting image
imageio.imwrite("parrot_xor_flag.png", result)

# Answer: MERCER{0ne_T1me_us@ble}
