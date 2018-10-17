import pytesseract as pt
from PIL import Image

image = Image.open("C:\\Users\\freul\\Pictures\\111.png")
#调用pytesseract，将图片转换成文字
#返回的结果就是转换后的结果
text = pt.image_to_string(image,lang="chi_sim")
print(text)

