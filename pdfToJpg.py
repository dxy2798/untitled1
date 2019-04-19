from wand.image import Image

with Image(filename="d:/sys_bak/0010900115700808_099-1651807210035.pdf", resolution=300) as img:
    img.format = 'jpeg'
    img.save(filename='k:/Scan1.jpg')

    print('导出成功！')