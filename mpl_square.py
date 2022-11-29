import matplotlib.pyplot as plt
import os 

path=os.path.dirname(__file__)
path_dir=os.path.join(path,'ploted_images')
sample_file_name='mpl_sqaures'
os.makedirs(path_dir,exist_ok=True)

x_values = range(1,1000)
y_values = [x**2 for x in x_values]

plt.style.use('tableau-colorblind10')
fig, ax = plt.subplots()
ax.scatter(x_values ,y_values,c=y_values,cmap=plt.cm.Blues,s=10)
ax.axis([0,1100,0,1100000])
ax.set_title('square NUmbers',fontsize=24)
ax.set_xlabel('Value',fontsize=24)
ax.set_ylabel('square NUmbers',fontsize=24)

ax.tick_params('both',labelsize=14)
# plt.show()
plt.savefig(os.path.join(path_dir,sample_file_name),bbox_inches='tight')
plt.close()