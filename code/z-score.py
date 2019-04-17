from util import *
import re

########################################################## 获取id ######################################################
path = "../data/Extension/ExtensionMapSD"
file_list = file_name(path)
file_id = []
for filename in file_list:
    filename = re.sub("\D", "", filename)
    file_id.append(filename)
print(file_id)

##################################################### 获取ExtensionMap #################################################
index = 0
for fileid in file_id:
    fsi = load_nii(path + '/' + 'extensionSD_'+fileid+'.nii').get_data()
    img_arr = np.squeeze(fsi)
    img_arr_trans = np.zeros(img_arr.shape)
    img_mean = np.mean(img_arr)
    img_sd = np.std(img_arr)
    for i in range(len(img_arr)):
        for j in range(len(img_arr[0])):
            for z in range(len(img_arr[0][0])):
                if img_sd != 0:
                    img_arr_trans[i][j][z] = ((img_arr[i][j][z] - img_mean) / img_sd)
                else:
                    img_arr_trans[i][j][z] = 0
    affine = load_nii(path + '/' + 'extensionSD_'+fileid+'.nii').affine
    vol_arr = nib.Nifti1Image(img_arr_trans, affine)
    nib.save(vol_arr, '../data/Extension/ExtensionMapSDSD/extensionSDSD_'+fileid+'.nii')
    index += 1
    print(index, "OK")
