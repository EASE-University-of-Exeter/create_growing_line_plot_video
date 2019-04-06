# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys
from matplotlib.animation import FFMpegWriter

fn = sys.argv[1]


#if os.path.exists(fn):
    #print(os.path.basename(fn)) # just the filename without the path
    #print(fn)
    #print(os.path.dirname(fn))
    # file exists
	
csvFileDirName = os.path.dirname(fn)
#print(csvFileDirName) 

# dataset
df = pd.read_csv(fn)  # store the csv file in dataframe df
#print(len(df.index))
df = df.iloc[2:len(df.index), np.r_[0,1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29]]  # subselect dataframe
df.columns = ['frame','mouth_corner_left_x','mouth_corner_left_y','mouth_corner_right_x','mouth_corner_right_y','inner_brow_left_x','inner_brow_left_y','inner_brow_right_x','inner_brow_right_y','upper_lip_x','upper_lip_y','lower_lip_x','lower_lip_y','nose_corner_left_x','nose_corner_left_y','nose_corner_right_x','nose_corner_right_y','pinna_ear_left_x','pinna_ear_left_y','pinna_ear_right_x','pinna_ear_right_y']
df = df.convert_objects(convert_numeric=True)

# Next bit shows how you might combine existing columns into new processed columns
#df = df.assign(mouth_corner_left = df.mouth_corner_left_x + df.mouth_corner_left_y,mouth_corner_right = df.mouth_corner_right_x + df.mouth_corner_right_y,inner_brow_left = df.mouth_corner_left_x + df.mouth_corner_left_y,inner_brow_right = df.inner_brow_left_x + df.inner_brow_left_y,upper_lip = df.upper_lip_x + df.upper_lip_y,lower_lip = df.lower_lip_x + df.lower_lip_y,nose_corner_left = df.nose_corner_left_x + df.nose_corner_left_y,nose_corner_right = df.nose_corner_right_x + df.nose_corner_right_y,pinna_ear_left = df.pinna_ear_left_x + df.pinna_ear_left_y,pinna_ear_right = df.pinna_ear_right_x + df.pinna_ear_right_y)

#print (df)

# plot
figure,ax = plt.subplots()

mouth_corner_left_line_x, = ax.plot(df.frame,df.mouth_corner_left_x, '#06067c', linestyle='-', marker='o', markersize=1, alpha=1.0)
mouth_corner_right_line_x, = ax.plot(df.frame,df.mouth_corner_right_x, '#0a0bbd', linestyle='-', marker='o', markersize=1, alpha=1.0)
inner_brow_left_line_x, = ax.plot(df.frame,df.inner_brow_left_x, '#005ae7', linestyle='-', marker='o', markersize=1, alpha=1.0)
inner_brow_right_line_x, = ax.plot(df.frame,df.inner_brow_right_x, '#04a3c1', linestyle='-', marker='o', markersize=1, alpha=1.0)
upper_lip_line_x, = ax.plot(df.frame,df.upper_lip_x, '#48eb9c', linestyle='-', marker='o', markersize=1, alpha=1.0)
lower_lip_line_x, = ax.plot(df.frame,df.lower_lip_x, '#88c448', linestyle='-', marker='o', markersize=1, alpha=1.0)
nose_corner_left_line_x, = ax.plot(df.frame,df.nose_corner_left_x, '#dcca28', linestyle='-', marker='o', markersize=1, alpha=1.0)
nose_corner_right_line_x, = ax.plot(df.frame,df.nose_corner_right_x, '#d87718', linestyle='-', marker='o', markersize=1, alpha=1.0)
pinna_ear_left_line_x, = ax.plot(df.frame,df.pinna_ear_left_x, '#b81504', linestyle='-', marker='o', markersize=1, alpha=1.0)
pinna_ear_right_line_x, = ax.plot(df.frame,df.pinna_ear_right_x, '#760202', linestyle='-', marker='o', markersize=1, alpha=1.0)

mouth_corner_left_line_y, = ax.plot(df.frame,df.mouth_corner_left_y, '#06067c', linestyle='-', marker='o', markersize=1, alpha=1.0)
mouth_corner_right_line_y, = ax.plot(df.frame,df.mouth_corner_right_y, '#0a0bbd', linestyle='-', marker='o', markersize=1, alpha=1.0)
inner_brow_left_line_y, = ax.plot(df.frame,df.inner_brow_left_y, '#005ae7', linestyle='-', marker='o', markersize=1, alpha=1.0)
inner_brow_right_line_y, = ax.plot(df.frame,df.inner_brow_right_y, '#04a3c1', linestyle='-', marker='o', markersize=1, alpha=1.0)
upper_lip_line_y, = ax.plot(df.frame,df.upper_lip_y, '#48eb9c', linestyle='-', marker='o', markersize=1, alpha=1.0)
lower_lip_line_y, = ax.plot(df.frame,df.lower_lip_y, '#88c448', linestyle='-', marker='o', markersize=1, alpha=1.0)
nose_corner_left_line_y, = ax.plot(df.frame,df.nose_corner_left_y, '#dcca28', linestyle='-', marker='o', markersize=1, alpha=1.0)
nose_corner_right_line_y, = ax.plot(df.frame,df.nose_corner_right_y, '#d87718', linestyle='-', marker='o', markersize=1, alpha=1.0)
pinna_ear_left_line_y, = ax.plot(df.frame,df.pinna_ear_left_y, '#b81504', linestyle='-', marker='o', markersize=1, alpha=1.0)
pinna_ear_right_line_y, = ax.plot(df.frame,df.pinna_ear_right_y, '#760202', linestyle='-', marker='o', markersize=1, alpha=1.0)


plt.xlim(0,len(df.index))
plt.axis('off')
plt.box(False)
#plt.show()


metadata = dict(title='DeepLabCut chart', artist='User',
                comment='Say something...')
writer = FFMpegWriter(fps=25, metadata=metadata)

with writer.saving(figure, csvFileDirName + ".\\growing_line_plot_video.mp4", 100):
	for n in range(len(df.index)):
		mouth_corner_left_line_x.set_data(df.frame[:n],df.mouth_corner_left_x[:n])
		mouth_corner_right_line_x.set_data(df.frame[:n],df.mouth_corner_right_x[:n])
		inner_brow_left_line_x.set_data(df.frame[:n],df.inner_brow_left_x[:n])
		inner_brow_right_line_x.set_data(df.frame[:n],df.inner_brow_right_x[:n])
		upper_lip_line_x.set_data(df.frame[:n],df.upper_lip_x[:n])
		lower_lip_line_x.set_data(df.frame[:n],df.lower_lip_x[:n])
		nose_corner_left_line_x.set_data(df.frame[:n],df.nose_corner_left_x[:n])
		nose_corner_right_line_x.set_data(df.frame[:n],df.nose_corner_right_x[:n])
		pinna_ear_left_line_x.set_data(df.frame[:n],df.pinna_ear_left_x[:n])
		pinna_ear_right_line_x.set_data(df.frame[:n],df.pinna_ear_right_x[:n])
		mouth_corner_left_line_y.set_data(df.frame[:n],df.mouth_corner_left_y[:n])
		mouth_corner_right_line_y.set_data(df.frame[:n],df.mouth_corner_right_y[:n])
		inner_brow_left_line_y.set_data(df.frame[:n],df.inner_brow_left_y[:n])
		inner_brow_right_line_y.set_data(df.frame[:n],df.inner_brow_right_y[:n])
		upper_lip_line_y.set_data(df.frame[:n],df.upper_lip_y[:n])
		lower_lip_line_y.set_data(df.frame[:n],df.lower_lip_y[:n])
		nose_corner_left_line_y.set_data(df.frame[:n],df.nose_corner_left_y[:n])
		nose_corner_right_line_y.set_data(df.frame[:n],df.nose_corner_right_y[:n])
		pinna_ear_left_line_y.set_data(df.frame[:n],df.pinna_ear_left_y[:n])
		pinna_ear_right_line_y.set_data(df.frame[:n],df.pinna_ear_right_y[:n])
		writer.grab_frame()
		#if not os.path.exists(csvFileDirName + '\\frames\\'):   # umcomment this and next two lines to save individual frames
		  #os.makedirs(csvFileDirName + '\\frames\\')
		#figure.savefig(csvFileDirName + '\\frames\\Frame%03d.png' %n,bbox_inches='tight', transparent=True, dpi=300) 
	


 
	
	
	
	


