import os
import random
import string
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
from torchvision import transforms
from PIL import Image, ImageFont, ImageDraw


# 定义卷积神经网络模型
class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(128 * 4 * 4, 512)
        self.fc2 = nn.Linear(512, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 128 * 4 * 4)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# 生成验证码图片
def generate_captcha(text, width=120, height=60, font_size=36):
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('arial.ttf', font_size)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(text, font)
    draw.text(((width - text_width) / 2, (height - text_height) / 2), text, font=font, fill=(0, 0, 0))
    return image


# 生成随机字符串
def generate_random_string(length=4):
    return ''.join(random.choice(string.digits) for _ in range(length))


# 生成数据集
def generate_dataset(size=10000):
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/train1'):
        os.mkdir('data/train1')
    if not os.path.exists('data/val'):
        os.mkdir('data/val')
    if not os.path.exists('data/test'):
        os.mkdir('data/test')
    font = ImageFont.truetype('arial.ttf', 36)  # 将字体对象创建移至循环外部
    for i in range(size):
        text = generate_random_string()
        image = generate_captcha(text, font=font)
        if i < 7000:
            image.save(f'data/train1/{text}.jpg')
        elif i < 8000:
            image.save(f'data/val/{text}.jpg')
        else:
            image.save(f'data/test/{text}.jpg')


# 训练模型
def train_model():
    # 定义数据预处理函数
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    # 加载数据集
    train_dataset = ImageFolder('data/train1', transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_dataset = ImageFolder('data/val', transform=transform)
    val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
    # 定义模型和优化器
    model = CNNModel()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    # 训练模型
    for epoch in range(10):
        model.train()
        for i, (images, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(images)
            loss = F.cross_entropy(outputs, labels)
            loss.backward()
            optimizer.step()
        # 评估模型
        model.eval()
        total = 0
        correct = 0
        with torch.no_grad():
            for images, labels in val_loader:
                outputs = model(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        accuracy = correct / total
        print(f'Epoch {epoch + 1}, Accuracy: {accuracy:.4f}')
    # 保存模型
    torch.save(model.state_dict(), 'model.pth')


def test_model():
    #   定义数据预处理函数
    transform = transforms.Compose([transforms.Resize((32, 32)),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    # 加载测试集
    test_dataset = ImageFolder('data/test', transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
    # 加载模型
    model = CNNModel()
    model.load_state_dict(torch.load('model.pth'))
    # 测试模型
    model.eval()
    with torch.no_grad():
        total = 0
        correct = 0
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        accuracy = correct / total * 100
        print(f'Test Accuracy: {accuracy:.2f}%')


if __name__ == '__main__':
    # 生成数据集
    generate_dataset()
    # 训练模型
    train_model()
    # 测试模型
    test_model()
