from util import *
import re

########################################################## 获取id ######################################################
path = "../data/Extension/ExtensionTrans3SD"
file_list = file_name(path)
file_id = []
for filename in file_list:
    filename = re.sub("\D", "", filename)
    file_id.append(filename[2:8])
file_id = file_id[0:50]
print(file_id)

########################################################## 获取mean ####################################################
fsi = load_nii('../data/Extension/ExtensionTrans3SD/extensionTrans3SD_sd.nii').get_data()
affine = load_nii('../data/Extension/ExtensionTrans3SD/extensionTrans3SD_sd.nii').affine
img_sd = np.squeeze(fsi)

##################################################### 获取ExtensionMap #################################################
index = 0
for fileid in file_id:
    fsi = load_nii(path + '/' + 'extensionTrans3SD_' + fileid + '.nii').get_data()
    img_arr = np.squeeze(fsi)
    img_arr_trans = np.zeros(img_arr.shape)
    for i in range(len(img_arr)):
        for j in range(len(img_arr[0])):
            for z in range(len(img_arr[0][0])):
                if img_arr[i][j][z] > img_sd[i][j][z]:
                    img_arr_trans[i][j][z] = img_arr[i][j][z] * img_arr[i][j][z]
    vol_arr = nib.Nifti1Image(img_arr_trans, affine)
    nib.save(vol_arr, '../data/Extension/ExtensionTrans4SD/extensionTrans4SD_'+fileid+'.nii')
    index += 1
    print(index, "OK")
