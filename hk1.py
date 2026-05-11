import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Status': ['Yes', 'No', None, 'Yes', 'No', 'Yes']
})

df['Status'] = df['Status'].fillna('No')

c = df['Status'].value_counts()
print(c)

c.plot(kind='pie', autopct='%1.1f%%')
plt.title('Course Completion Status')
plt.show()