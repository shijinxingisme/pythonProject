from PIL import Image, ImageDraw, ImageFont
import random
 # 定义验证码字符集
CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
 # 定义验证码图片大小
WIDTH, HEIGHT = 100, 100
 # 定义验证码长度
LENGTH = 4
 # 定义字体
FONT = ImageFont.truetype('arial.ttf', 50)
 # 生成验证码图片
def generate_captcha():
    # 创建空白图片
    img = Image.new('RGB', (WIDTH, HEIGHT), 'white')
     # 获取绘图对象
    draw = ImageDraw.Draw(img)
     # 随机生成验证码
    captcha = ''
    for i in range(LENGTH):
        char = random.choice(CHARACTERS)
        captcha += char
        x = i * WIDTH // LENGTH + random.randint(-10, 10)
        y = random.randint(-10, 10)
        draw.text((x, y), char, font=FONT, fill=(0, 0, 0))
     # 添加干扰线
    for i in range(random.randint(1, 5)):
        x1 = random.randint(0, WIDTH // 2)
        y1 = random.randint(0, HEIGHT)
        x2 = random.randint(WIDTH // 2, WIDTH)
        y2 = random.randint(0, HEIGHT)
        draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=2)
     # 返回验证码图片和对应的验证码
    return img, captcha


if __name__ == '__main__':
    # 生成多个验证码图片
    for i in range(2):
        img, captcha = generate_captcha()
        img.save('train/{}.jpg'.format(captcha))