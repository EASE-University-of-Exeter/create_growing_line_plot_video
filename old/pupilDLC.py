# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# data selection
path = input('C:\\Users\\steve\\Anaconda3\\envs\\ease_dog_emotions\\dev\\pupilTracking\\') #C:\Users\Windows\Desktop
path = os.path.normpath(path)
os.chdir(path)
files = [os.path.join(path, file) for file in os.listdir(path)
			if file.endswith('.csv')]
print(files)
i = input('which file to selecet (eg: 0 or 1) ?')
i = int(i)


# dataset
df = pd.read_csv(files[i])  # store the csv file in dataframe df
#print(len(df.index))
#df = df.iloc[2:len(df.index), np.r_[0,1,2,4,5,7,8,10,11]]  # subselect dataframe
df = df.iloc[2:len(df.index), np.r_[0,1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29]]  # subselect dataframe
#df.columns = ['frame','x1x','x1y','x2x','x2y','y1x','y1y','y2x','y2y']
df.columns = ['frame','mouth_corner_left_x','mouth_corner_left_y','mouth_corner_right_x','mouth_corner_right_y','inner_brow_left_x','inner_brow_left_y','inner_brow_right_x','inner_brow_right_y','upper_lip_x','upper_lip_y','lower_lip_x','lower_lip_y','nose_corner_left_x','nose_corner_left_y','nose_corner_right_x','nose_corner_right_y','pinna_ear_left_x','pinna_ear_left_y','pinna_ear_right_x','pinna_ear_right_y']
df = df.convert_objects(convert_numeric=True)

#df = df.assign(diamH = ((df.x2x-df.x1x)**2 + (df.x2y-df.x1y)**2)**0.5, diamV = ((df.y2x-df.y1x)**2 + (df.y2y-df.y1y)**2)**0.5) #obtain horizontal and vertucak pupil diameters respectively diamH and diamV 

df = df.assign(mouth_corner_left = df.mouth_corner_left_x + df.mouth_corner_left_y,mouth_corner_right = df.mouth_corner_right_x + df.mouth_corner_right_y,inner_brow_left = df.mouth_corner_left_x + df.mouth_corner_left_y,inner_brow_right = df.inner_brow_left_x + df.inner_brow_left_y,upper_lip = df.upper_lip_x + df.upper_lip_y,lower_lip = df.lower_lip_x + df.lower_lip_y,nose_corner_left = df.nose_corner_left_x + df.nose_corner_left_y,nose_corner_right = df.nose_corner_right_x + df.nose_corner_right_y,pinna_ear_left = df.pinna_ear_left_x + df.pinna_ear_left_y,pinna_ear_right = df.pinna_ear_right_x + df.pinna_ear_right_y)


#print (df)

# plot
figure = plt.figure()
#plt.plot('frame','diamH', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
#plt.plot('frame','diamV', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)

plt.plot('frame','mouth_corner_left', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
plt.plot('frame','mouth_corner_right', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
plt.plot('frame','inner_brow_left', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
plt.plot('frame','inner_brow_right', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
plt.plot('frame','upper_lip', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
plt.plot('frame','lower_lip', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
plt.plot('frame','nose_corner_left', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
plt.plot('frame','nose_corner_right', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
plt.plot('frame','pinna_ear_left', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)
plt.plot('frame','pinna_ear_right', data=df, linestyle='none', marker='o', markersize=1, alpha=1.0)



plt.xlim(0,len(df.index))
plt.axis('off')
plt.box(False)
#plt.show()

figure.savefig(files[i]+'.png', bbox_inches='tight', transparent=True, dpi=300)