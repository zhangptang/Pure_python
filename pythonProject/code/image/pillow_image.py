# -*-coding:utf-8-*-
import requests
from PIL import Image, ImageFilter


def download_file():
    resp = requests.get('https://s.cn.bing.net/th?id=OHR.CommonDolphin_ZH-CN3524729916_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&qlt=30')
    with open('../../files/first.jpg', 'wb') as f:
        f.write(resp.content)


def rect_image(image):
    """剪裁照片"""
    rect = (80, 20, 310, 360)
    image.crop(rect).show()


def thumbnail_image(image):
    """缩略图"""
    size = (128, 128)
    image.thumbnail(size)
    image.show()


def rotate_image(image):
    image.rotate(180).show()
    image.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show()


def filter_image(image):
    """滤镜效果"""
    image.filter(ImageFilter.CONTOUR).show()


def open_image():
    image = Image.open('../../files/first.jpg')
    print(f'{image.format}, {image.size} {image.mode}')
    # thumbnail_image(image)
    # rotate_image(image)
    filter_image(image)


def main():
    # download_file()
    open_image()


if __name__ == '__main__':
    main()
