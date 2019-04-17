from util import *
import re

########################################################## 获取id ######################################################
path = "../data/Extension/GRAY/sc1wr_brainSD"
file_list = file_name(path)
file_id = []
for filename in file_list:
    filename = re.sub("\D", "", filename)
    file_id.append(filename[2:8])
print(file_id)

########################################################## 获取mean ####################################################
img_mean, img_list, affine = mean_list(path)
img_sd = np.std(img_list, axis=0)
vol_mean = nib.Nifti1Image(img_mean, affine)
nib.save(vol_mean, '../data/Extension/GRAY/ExtensionMapGSD/extensionMapGSD_mean.nii')
vol_sd = nib.Nifti1Image(img_sd, affine)
nib.save(vol_sd, '../data/Extension/GRAY/ExtensionMapGSD/extensionMapGSD_sd.nii')

##################################################### 获取ExtensionMap #################################################
index = 0
for fileid in file_id:
    fsi = load_nii(path + '/' + 'sc1GSD_' + fileid + '.nii').get_data()
    img_arr = np.squeeze(fsi)
    img_arr_trans = np.zeros(img_arr.shape)
    for i in range(len(img_arr)):
        for j in range(len(img_arr[0])):
            for z in range(len(img_arr[0][0])):
                # img_arr_trans[i][j][z] = img_arr[i][j][z] - img_mean[i][j][z]
                if img_sd[i][j][z] != 0:
                    img_arr_trans[i][j][z] = ((img_arr[i][j][z] - img_mean[i][j][z]) / img_sd[i][j][z])
                else:
                    img_arr_trans[i][j][z] = 0
    vol_arr = nib.Nifti1Image(img_arr_trans, affine)
    nib.save(vol_arr, '../data/Extension/GRAY/ExtensionMapGSD/extensionGSD_'+fileid+'.nii')
    index += 1
    print(index, "OK")
    # if index == 1:
    #     break
