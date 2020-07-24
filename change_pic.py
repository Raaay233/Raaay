from PIL import Image


def pic2ascii(pic, asciis, zoom, vscale):
    img = Image.open(pic)
    # 打开图片并转换为灰度模式
    out = img.convert("L")
    # 获取图片的宽度和高度
    width, height = out.size
    # 由于字符的宽度并不会等于高度，所以需要进行调整
    out = out.resize((int(width * zoom), int(height * zoom * vscale)))
    ascii_len = len(asciis)
    texts = ''

    for row in range(out.height):
        for col in range(out.width):
            gray = out.getpixel((col, row))
            texts += asciis[int((gray / 255) * (ascii_len - 1))]
        texts += '\n'

    return texts


def main():
    pic = input("请输入待转换的图片名称：")
    # 10个字符表示按“灰度级别”从高到低排序

    # asciis = "@%#*+=-:. "  # 10
    # asciis = "MNHQ$OC?7>!:-;. "  # 16
    asciis = 'MWH#%XD8A4wp03u?7i{+tc!<"~:,^.` '  # 32

    # 设置缩放系数 调节大小
    zoom = 1
    # 设置垂直比例系数 0.5最佳
    vscale = 0.5
    texts = pic2ascii(pic, asciis, zoom, vscale)

    with open("ascii1.txt", "w") as file:
        file.write(texts)


if __name__ == "__main__":
    # zoom = 0.5
    # vscale = 0.5
    # txt字体设置：宋体 常规 四号
    main()
