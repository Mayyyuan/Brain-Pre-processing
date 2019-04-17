from util import *
import re

########################################################## 获取id ######################################################
L = file_name("../data/swr_brainSD")
new_L = []
for filename in L:
    filename = re.sub("\D", "", filename)
    new_L.append(filename)
print(new_L)
index = 0
################################################## 转化为灰白质的灰度图片 ##############################################
for id in new_L:
    fsi = load_nii('../data/swr_brainSD/swrSD_' + id + '.nii').get_data()
    img_arr = np.squeeze(fsi)
    img_arr1 = np.zeros(img_arr.shape)
    img_arr2 = np.zeros(img_arr.shape)
    fsi1 = load_nii('../data/c1wr_brain/c1wr' + id + '_brain.nii').get_data()
    c1_arr = np.squeeze(fsi1)
    fsi2 = load_nii('../data/c2wr_brain/c2wr' + id + '_brain.nii').get_data()
    c2_arr = np.squeeze(fsi2)
    for i in range(len(img_arr)):
        for j in range(len(img_arr[0])):
            for z in range(len(img_arr[0][0])):
                if c1_arr[i][j][z] > 0.5:
                    img_arr1[i][j][z] = img_arr[i][j][z]
                if c2_arr[i][j][z] > 0.5:
                    img_arr2[i][j][z] = img_arr[i][j][z]
    print('-----GET img_arr1,img_arr2 OK-----')
    #################################################### 计算阈值 ######################################################
    c1_mean, c1_sd = mean_sd(img_arr1)
    c2_mean, c2_sd = mean_sd(img_arr2)
    Tlow = c1_mean + c1_sd * 0.5
    Thigh = c2_mean - c2_sd * 0.5
    print(c1_mean, c2_mean, c1_sd, c2_sd, Tlow, Thigh)
    for i in range(len(img_arr)):
        for j in range(len(img_arr[0])):
            for z in range(len(img_arr[0][0])):
                if Tlow < img_arr[i][j][z] < Thigh:
                    img_arr[i][j][z] = 1
                else:
                    img_arr[i][j][z] = 0
    affine = load_nii('../data/swr_brainSD/swrSD_' + id + '.nii').affine
    vol_mean = nib.Nifti1Image(img_arr, affine)
    nib.save(vol_mean, '../data/trans3_brainSD/trans3SD_' + id + '.nii')
    vol_mean = nib.Nifti1Image(img_arr1, affine)
    nib.save(vol_mean, '../data/c1_brainSD/c1SD_'+id+'.nii')
    vol_mean = nib.Nifti1Image(img_arr2, affine)
    nib.save(vol_mean, '../data/c2_brainSD/c2SD_'+id+'.nii')
    index += 1
    print(index, "OK")
