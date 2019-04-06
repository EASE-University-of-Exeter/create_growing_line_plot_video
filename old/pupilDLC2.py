# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from matplotlib.animation import FFMpegWriter

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
df = df.iloc[2:len(df.index), np.r_[0,1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29]]  # subselect dataframe
df.columns = ['frame','mouth_corner_left_x','mouth_corner_left_y','mouth_corner_right_x','mouth_corner_right_y','inner_brow_left_x','inner_brow_left_y','inner_brow_right_x','inner_brow_right_y','upper_lip_x','upper_lip_y','lower_lip_x','lower_lip_y','nose_corner_left_x','nose_corner_left_y','nose_corner_right_x','nose_corner_right_y','pinna_ear_left_x','pinna_ear_left_y','pinna_ear_right_x','pinna_ear_right_y']
df = df.convert_objects(convert_numeric=True)


df = df.assign(mouth_corner_left = df.mouth_corner_left_x + df.mouth_corner_left_y,mouth_corner_right = df.mouth_corner_right_x + df.mouth_corner_right_y,inner_brow_left = df.mouth_corner_left_x + df.mouth_corner_left_y,inner_brow_right = df.inner_brow_left_x + df.inner_brow_left_y,upper_lip = df.upper_lip_x + df.upper_lip_y,lower_lip = df.lower_lip_x + df.lower_lip_y,nose_corner_left = df.nose_corner_left_x + df.nose_corner_left_y,nose_corner_right = df.nose_corner_right_x + df.nose_corner_right_y,pinna_ear_left = df.pinna_ear_left_x + df.pinna_ear_left_y,pinna_ear_right = df.pinna_ear_right_x + df.pinna_ear_right_y)

#print (df)

# plot
figure,ax = plt.subplots()

mouth_corner_left_line, = ax.plot(df.frame,df.mouth_corner_left, linestyle='-', marker='o', markersize=1, alpha=1.0)
mouth_corner_right_line, = ax.plot(df.frame,df.mouth_corner_right, linestyle='-', marker='o', markersize=1, alpha=1.0)
inner_brow_left_line, = ax.plot(df.frame,df.inner_brow_left, linestyle='-', marker='o', markersize=1, alpha=1.0)
inner_brow_right_line, = ax.plot(df.frame,df.inner_brow_right, linestyle='-', marker='o', markersize=1, alpha=1.0)
upper_lip_line, = ax.plot(df.frame,df.upper_lip, linestyle='-', marker='o', markersize=1, alpha=1.0)
lower_lip_line, = ax.plot(df.frame,df.lower_lip, linestyle='-', marker='o', markersize=1, alpha=1.0)
nose_corner_left_line, = ax.plot(df.frame,df.nose_corner_left, linestyle='-', marker='o', markersize=1, alpha=1.0)
nose_corner_right_line, = ax.plot(df.frame,df.nose_corner_right, linestyle='-', marker='o', markersize=1, alpha=1.0)
pinna_ear_left_line, = ax.plot(df.frame,df.pinna_ear_left, linestyle='-', marker='o', markersize=1, alpha=1.0)
pinna_ear_right_line, = ax.plot(df.frame,df.pinna_ear_right, linestyle='-', marker='o', markersize=1, alpha=1.0)



plt.xlim(0,len(df.index))
plt.axis('off')
plt.box(False)
#plt.show()



for n in range(len(df.index)):
	#line.set_data(x[:n], y[:n])
	mouth_corner_left_line.set_data(df.frame[:n],df.mouth_corner_left[:n])
	mouth_corner_right_line.set_data(df.frame[:n],df.mouth_corner_right[:n])
	inner_brow_left_line.set_data(df.frame[:n],df.inner_brow_left[:n])
	inner_brow_right_line.set_data(df.frame[:n],df.inner_brow_right[:n])
	upper_lip_line.set_data(df.frame[:n],df.upper_lip[:n])
	lower_lip_line.set_data(df.frame[:n],df.lower_lip[:n])
	nose_corner_left_line.set_data(df.frame[:n],df.nose_corner_left[:n])
	nose_corner_right_line.set_data(df.frame[:n],df.nose_corner_right[:n])
	pinna_ear_left_line.set_data(df.frame[:n],df.pinna_ear_left[:n])
	pinna_ear_right_line.set_data(df.frame[:n],df.pinna_ear_right[:n])
	figure.savefig('.\\frames\\Frame%03d.png' %n,bbox_inches='tight', transparent=True, dpi=300)
	


  
	
	
	
	


