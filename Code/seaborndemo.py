import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
sns.lineplot(x='age',y='charges',data=ins_df)
plt.savefig('sns.png')
plt.close()