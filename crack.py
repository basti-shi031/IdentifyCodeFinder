from PIL import Image
import os

im = Image.open("captcha.gif")
print(im.mode)
# (将图片转换为8位像素模式)
# im2 = im.convert("P")
# 打印颜色直方图
print(im.histogram())

result = im.histogram();

values = {}
for i in range(256):
    values[i] = result[i]

print(values.items())
# 根据颜色值进行排序 选取前十个
for j, k in sorted(values.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(j, k)

im2 = Image.new("P", im.size, 255)

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        if pix == 220 or pix == 227:  # these are the numbers to get
            im2.putpixel((y, x), 0)
# im2.show()

inletter = False
foundletter = False
start = 0
end = 0

letters = []

print(im2.size[0])
print(im2.size[1])

# 沿y轴切割,获得每个字母开始和结束的x轴坐标值
for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y, x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start, end))

    inletter = False
print(letters)

# 加载训练集
imageSet = []
iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for icon in iconset:
    for img in os.listdir('./iconset/%s/' % (icon)):
        temp = []

# 根据坐标值切割图片
count = 0
for letter in letters:
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
    im3.save("./%s.gif" % count)
    count += 1
