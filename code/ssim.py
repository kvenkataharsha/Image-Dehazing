from SSIM_PIL import compare_ssim
from PIL import Image

image1 = Image.open("data/Natural hazy images/39.jpg")
image2 = Image.open("data/Natural Dehazed images/39.jpg")
value = compare_ssim(image1, image2)
print(value)

#python3 -m pip install SSIM-PIL use this library