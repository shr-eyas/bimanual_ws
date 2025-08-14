import numpy as np
from scipy.spatial.transform import Rotation as R

# Sample O_T_EE matrix as a flat list (row-major order)
O_T_EE =  [0.5998307274071316, 0.026512080281287508, -0.7996875690276736, 0.0,
           0.7991356913931997, 0.02988302836016337, 0.6004074877593869, 0.0,
           0.03981513782148727, -0.9992017384968784, -0.0032619909674540537, 0.0,
           0.36850847735259445, -0.5489570623978788, 0.42590475703749486, 1.0]


# Step 1: Convert to 4x4 matrix (column-major order)
M = np.array(O_T_EE).reshape((4, 4), order='F')

# Step 2: Extract translation
position = M[:3, 3]

# Step 3: Extract rotation matrix
R_mat = M[:3, :3]

# Step 4: Convert to quaternion [x, y, z, w]
quat = R.from_matrix(R_mat).as_quat()

# Step 5: Output as numpy arrays in specified format
position_array = np.array([round(p, 6) for p in position])
quat_array = np.array([round(q, 6) for q in quat])

print("Position array:")
print(position_array)
print("Quaternion array:")
print(quat_array)
