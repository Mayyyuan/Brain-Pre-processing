from util import *
import re
########################################################## 获取id ######################################################
path = "../data/trans4_brainSD"
L = file_name(path)
new_L = []
for filename in L:
    filename = re.sub("\D", "", filename)
    new_L.append(filename[2:8])
print(new_L)
index = 0
########################################################## 获取mean ####################################################
img_mean, img_list, affine = mean_list(path)
#################################################### 与平均值相减 ######################################################
for fileid in new_L:
    print(index, "is start")
    fsi = load_nii('../data/trans4_brainSD/trans4SD_' + fileid + '.nii').get_data()
    img_arr = np.squeeze(fsi)
    new_arr = np.zeros(img_arr.shape)
    for i in range(len(img_arr)):
        for j in range(len(img_arr[0])):
            for z in range(len(img_arr[0][0])):
                new_arr[i][j][z] = img_arr[i][j][z] - img_mean[i][j][z]
    affine = load_nii('../data/trans4_brainSD/trans4SD_' + fileid + '.nii').affine
    vol_mean = nib.Nifti1Image(new_arr, affine)
    nib.save(vol_mean, '../data/trans4_brainSD_con/trans4SDcon_' + fileid + '.nii')
    index += 1
    print(index, "OK")
    if index == 1:
        break
vol_mean = nib.Nifti1Image(img_mean, affine)
nib.save(vol_mean, '../data/trans4_brainSD_con/trans4SDcon_mean.nii')
