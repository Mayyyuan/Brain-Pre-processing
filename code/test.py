from util import *


fsi = load_nii('../data/w01_brain.nii').get_data()
img_arr = np.squeeze(fsi)
img_new = np.zeros(img_arr.shape)
for i in range(len(img_arr)):
    for j in range(len(img_arr[0])):
        for z in range(len(img_arr[0][0])):
            if img_arr[i][j][z] != 0:
                img_new[i][j][z] = 1
            else:
                img_new[i][j][z] = 0
affine = load_nii('../data/w01_brain.nii').affine
vol_mean = nib.Nifti1Image(img_new, affine)
nib.save(vol_mean, '../data/test_mask.nii')
