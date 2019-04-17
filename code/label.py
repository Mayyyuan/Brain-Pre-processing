from util import *

## 输出病灶顶点坐标以及大小
fsi = load_nii('../data/FCD_06-label.nii').get_data()
img_arr = np.squeeze(fsi)
i_min, i_length, j_min, j_length, z_min, z_length = 0, 0, 0, 0, 0, 0
for i in range(len(img_arr)):
    for j in range(len(img_arr[0])):
        for z in range(len(img_arr[0][0])):
            if img_arr[i][j][z] == 1:
                if i < i_min or i_min == 0:
                    i_min = i
                elif i - i_min > i_length:
                    i_length = i - i_min
                if j < j_min or j_min == 0:
                    j_min = j
                elif j - j_min > j_length:
                    j_length = j - j_min
                if z < z_min or z_min == 0:
                    z_min = z
                elif z - z_min > z_length:
                    z_length = z - z_min
print(i_min, i_length, j_min, j_length, z_min, z_length)
