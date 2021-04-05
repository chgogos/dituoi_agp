#%%
import sys
print(sys.version, sys.platform)

#%%
import os
print(os.name)
#%%
os.listdir()

# %%
%pylab inline
plot([0,1,2],[0,1,4])
# %%
import pandas as pd

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
df
# %%
