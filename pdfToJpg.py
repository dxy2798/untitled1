from wand.image import Image

with Image(filename="k:/Scan1.pdf", resolution=300) as img:
    img.format = 'jpeg'
    img.save(filename='k:/Scan1.jpg')

    print('导出成功！')