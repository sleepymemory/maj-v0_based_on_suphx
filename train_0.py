import os

import tqdm
from torch import nn, optim
import torch
from torch.utils.data import DataLoader
from dataloader import *
from Net import *
from torchvision.utils import save_image

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

train_path = r'C:\Users\Paradox\Desktop\maj\train'
train_list = []
files = os.listdir(os.path.join(train_path, "img"))
for i in files:
    train_list.append(i)
datasets_train = DataLoader(MyDataset(train_path, train_list), batch_size=128, shuffle=True)

val_path = r'C:\Users\Paradox\Desktop\maj\val'
val_list = []
files = os.listdir(os.path.join(val_path, "img"))
for i in files:
    val_list.append(i)
datasets_val = DataLoader(MyDataset(val_path, val_list), batch_size=128, shuffle=True)

train_len_data = len(datasets_train)
val_len_data = len(datasets_val)

model = myNet1().to(device)

weight_path = r'params\Suphx_G_15.pth'

if os.path.exists(weight_path):
    model.load_state_dict(torch.load(weight_path))
    print('successful load weight！')
else:
    print('not successful load weight')

opt = optim.Adam(
    model.parameters(),
)
loss_fun = nn.CrossEntropyLoss()

epoch = 0
while epoch <= 100:
    model.train()
    loop1 = tqdm.tqdm(datasets_train)
    train_accurancy = 0
    # 训练集
    for i, (image, label) in enumerate(loop1):
        image = image.squeeze(1)
        # print(image.shape)
        image = image.to(device)
        label = label.squeeze(1)
        # print(label)
        label = label.to(device)

        out = model(image)

        loss = loss_fun(out, label.long())
        # print(loss.item())
        out_0 = out.argmax(axis=1).cpu().numpy()
        label_0 = label.detach().cpu().numpy()
        x = label_0 == out_0
        accurancy = sum(x) / x.size
        train_accurancy += accurancy
        loop1.set_postfix(loss_=loss.item(), accurancy_=accurancy)

        opt.zero_grad()
        loss.backward()
        opt.step()
    print(train_accurancy / train_len_data)
    # 验证集
    if epoch % 1 == 0:
        model.eval()
        val_accuracy = 0.0
        loop2 = tqdm.tqdm(datasets_val)
        for i, (image, label) in enumerate(loop2):
            image = image.squeeze(1)
            image = image.to(device)
            label = label.squeeze(1)
            label = label.to(device)

            out = model(image)
            label.long()

            out_0 = out.argmax(axis=1).cpu().numpy()
            label_0 = label.detach().cpu().numpy()
            x = label_0 == out_0
            accurancy = sum(x) / x.size
            val_accuracy += accurancy
            loop2.set_postfix(accurancy_=accurancy)

        print(val_accuracy / val_len_data)

    if epoch % 1 == 0:
        weight_path = os.path.join("params", "Suphx_G_{}.pth".format(epoch))
        torch.save(model.state_dict(), weight_path)
        print('save successfully!')
    epoch += 1
