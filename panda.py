import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])

dates = pd.date_range("20170711",periods = 6)

df = pd.DataFrame(np.random.randn(6,4),index = dates,columns = list('ABCD'))

df2 = pd.DataFrame({'A':1,
					'B':pd.Timestamp('20170711'),
					'C':pd.Series(1,index=list(range(4)),dtype='float32'),
					'D':np.array([3]*4,dtype='int32'),
					'E':pd.Categorical(['test','train','subway','haha']),
					'F':'FOO'
	})
print df.T

x = np.linspace(0,10,1000)
y = np.sin(x)
z = np.sin(x**2)
plt.figure(figsize = (8,4))
plt.plot(x,y,label="$sin(x)$",color = "red",linewidth = 3)
plt.plot(x,z,"b-",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("pyplot first example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
