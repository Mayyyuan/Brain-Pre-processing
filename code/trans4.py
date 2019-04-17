from util import *
import re
########################################################## 获取id ######################################################
L = file_name("../data/trans3_brainSD")
new_L = []
for filename in L:
    filename = re.sub("\D", "", filename)
    new_L.append(filename[2:8])
print(new_L)
index = 0
################################################## 与(5,5,5)ones进行卷积 ###############################################
for id in new_L:
    print(index, "is start")
    fsi = load_nii('../data/trans3_brainSD/trans3SD_' + id + '.nii').get_data()
    img_arr = np.squeeze(fsi)
    new_arr = np.zeros(img_arr.shape)
    for i in range(2, len(img_arr) - 2):
        print(i)
        for j in range(2, len(img_arr[0]) - 2):
            for z in range(2, len(img_arr[0][0]) - 2):
                for i1 in range(i - 2, i + 3):
                    for j1 in range(j - 2, j + 3):
                        for z1 in range(z - 2, z + 3):
                            new_arr[i][j][z] += img_arr[i1][j1][z1]
    affine = load_nii('../data/trans3_brainSD/trans3SD_' + id + '.nii').affine
    vol_arr = nib.Nifti1Image(new_arr, affine)
    nib.save(vol_arr, '../data/trans4_brainSD/trans4SD_' + id + '.nii')
    print(index, "is OK")
    index += 1
    if index == 1:
        break
