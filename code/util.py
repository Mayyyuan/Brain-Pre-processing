import os
import numpy as np
import nibabel as nib
from nibabel import load as load_nii


# 获取文件夹中的文件名
def file_name(file_dir):
    filelist = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            filelist.append(os.path.join(root, file))
    return filelist


# 获取单个图片的mean和sd
def mean_sd(img_arr):
    num = []
    for vol in img_arr:
        for line in vol:
            for p in line:
                if p != 0:
                    num.append(p)
    num_mean = np.mean(num)
    num_sd = np.std(num)
    return num_mean, num_sd


# 获取一组图片的mean和arr数组
def mean_list(filename):
    filelist = file_name(filename)
    # img_arr = []
    img_sum = []
    img_list = []
    for filename in filelist:
        fsi = load_nii(filename).get_data()
        img_arr = np.squeeze(fsi)
        if len(img_list) == 0:
            img_sum = img_arr
            affine = load_nii(filename).affine
        else:
            img_sum += img_arr
        img_list.append(img_arr)
    img_mean = img_sum/len(img_list)
    img_list = np.array(img_list)
    print('img_list', img_list.shape)
    print(img_mean.shape)
    return img_mean, img_list, affine


# def T_low():
    # img_mean, img_list, affine = mean_list("../data/c1wr_brain")
    # img_sd = np.std(img_list, axis=0)  # 灰质标准差
    # T_low = np.zeros(img_mean.shape)  # 阈值low(gray)
    # for i in range(len(img_mean)):
    #     for j in range(len(img_mean[0])):
    #         for z in range(len(img_mean[0][0])):
    #             T_low[i][j][z] = img_mean[i][j][z] + img_sd[i][j][z] * 0.5
    # vol_mean = nib.Nifti1Image(T_low, affine)  # 存储
    # nib.save(vol_mean, 'T_low.nii')
    # vol_mean = nib.Nifti1Image(img_mean, affine)
    # nib.save(vol_mean, 'c1_mean.nii')
    # return T_low, img_mean


# def T_high():
    # img_mean, img_list, affine = mean_list("../data/c2wr_brain")
    # img_sd = np.std(img_list, axis=0)  # 白质标准差
    # T_high = np.zeros(img_mean.shape)  # 阈值high(white)
    # for i in range(len(img_mean)):
    #     for j in range(len(img_mean[0])):
    #         for z in range(len(img_mean[0][0])):
    #             T_high[i][j][z] = img_mean[i][j][z] - img_sd[i][j][z] * 0.5
    # vol_mean = nib.Nifti1Image(T_high, affine)  # 存储
    # nib.save(vol_mean, 'T_high.nii')
    # vol_mean = nib.Nifti1Image(img_mean, affine)
    # nib.save(vol_mean, 'c2_mean.nii')
    # return T_high, img_mean
