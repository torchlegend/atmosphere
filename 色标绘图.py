import os
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

levels = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
cmp = mpl.colors.ListedColormap(['#FFFFFF', '#48A0F0', '#64DBDD', '#5AC839', '#3F8E27', '#FFFE54', '#E1C141',
                                 '#F09637', '#EA3323', '#C5291C', '#B12418', '#EB3AEA', '#8920AD'], 'indexed')

log_dir = r""  # 日志文件夹
save_folder = r""  # 保存文件夹
input_seq_len = 10  # 序列长度
save_mode = ""  # 保存模式
input = ""  # 应该是一个tensor
# levels = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

# cmp = mpl.colors.ListedColormap(['white', 'lightskyblue', 'cyan', 'lightgreen', 'limegreen', 'green',
#                                  'yellow', 'orange', 'chocolate', 'red', 'firebrick', 'darkred', 'fuchsia',
#                                  'purple'], 'indexed')
if not os.path.exists(os.path.join(log_dir, save_folder)):
    os.makedirs(os.path.join(log_dir, save_folder))


# 随机生成x,y
def f(x, y):
    return (1 - x / 2 + x ** 3 + y ** 5) * np.exp(-x ** 2 - y ** 2)


x = np.linspace(-3, 3, 251)
y = np.linspace(-3, 3, 201)
X, Y = np.meshgrid(x, y)

# print(input.shape)
for i in range(input_seq_len):
    img = input[i].squeeze().cpu().numpy()
    # print(img.shape)
    plt.contourf(X, Y, img, levels=levels, extend='both', cmap=cmp)  # 绘制等高线
    save_fig_path = os.path.join(log_dir, save_folder, 'input' + str(i + 1))
    if save_mode == 'simple':
        plt.xticks([])
        plt.yticks([])
        plt.savefig(save_fig_path, bbox_inches='tight', dpi=600)
    elif save_mode == 'integral':
        plt.title('Input')
        plt.xlabel('Timestep' + str(i + 1))
        plt.colorbar()
        plt.savefig(save_fig_path, dpi=600)
    plt.clf()
