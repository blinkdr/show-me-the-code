#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
import os



def add_num_on_image(in_path, num, font):
    '''
    给指定的图片右上角添加红色的数字，类似微信未读信息的提示效果
    给图片加水印的常用套路：
    1. 打开图片，做相应的转换
    2. 新建一幅同样大小的图片（水印）
    3. 载入字体文件
    4. 在水印上添加画笔
    5. 在水印上添加文字
    6. 两张图片相加
    7. 显示或保存
    '''
    size = (100, 100)
    # 1. 打开图片
    try:
        img = Image.open(in_path).convert('RGBA')
    except IOError:
        return 0
    img = img.resize(size)
    
    # 2. 新建图片
    water = Image.new('RGBA', size, (255, 255, 255, 0))

    # 3. 载入字体
    fnt = ImageFont.truetype(font, 24)
    
    # 4. 添加画笔
    pen = ImageDraw.Draw(water)

    # 5. 写字
    pen.text((80, 0), str(num), font=fnt, fill=(255, 0, 0, 255))

    # 6. 相加
    out = Image.alpha_composite(img, water)

    # 7. 显示
    # out.show()
    out.save('result.png')

if __name__ == "__main__":
    in_path = 'test.jpeg'
    font = 'DroidNaskhUI-Regular.ttf'
    num = 4

    add_num_on_image(in_path, num, font)
