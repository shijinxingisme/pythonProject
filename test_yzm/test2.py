import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
from PIL import Image
import os
from sklearn.preprocessing import LabelEncoder

# 定义数据集类
class CaptchaDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.img_files = os.listdir(data_dir)
        self.transform = transforms.Compose([
            transforms.Resize((100, 100)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])

    def __len__(self):
        return len(self.img_files)

    def __getitem__(self, idx):
        img_path = os.path.join(self.data_dir, self.img_files[idx])
        img = Image.open(img_path)
        img = self.transform(img)
        label = self.img_files[idx].split('.')[0]
        return img, str(label)


# 定义模型类
class CaptchaModel(nn.Module):
    def __init__(self):
        super(CaptchaModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 25 * 25, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool1(nn.functional.relu(self.conv1(x)))
        x = self.pool2(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 64 * 25 * 25)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# 定义训练函数
def train(model, train_loader, criterion, optimizer, num_epochs):
    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, data in enumerate(train_loader, 0):
            inputs, labels = data
            optimizer.zero_grad()
            outputs = model(inputs)
            char_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            label_map = {char: idx for idx, char in enumerate(char_set)}
            lb = labels[0]
            label = [label_map[char] for char in lb]
            label = torch.tensor(label)
            # .squeeze()  todo
            loss = criterion(outputs, label)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print('Epoch [%d/%d], Loss: %.4f' % (epoch + 1, num_epochs, running_loss / len(train_loader)))





if __name__ == '__main__':
    # 准备数据集
    train_dataset = CaptchaDataset('train1/')
    train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
    # 定义模型、损失函数和优化器
    model = CaptchaModel()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    # 训练模型
    train(model, train_loader, criterion, optimizer, num_epochs=10)
    # 保存模型
    torch.save(model.state_dict(), 'captcha_model.pth')