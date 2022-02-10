import seaborn as sns
import matplotlib.pyplot as plt


car_crashes = sns.load_dataset('car_crashes')
car_crashes.sort_values("total" , ascending=False, inplace=True)

plt.figure(figsize=(15,10))
sns.barplot(data= car_crashes , x='abbrev' , y='total' , facecolor ='w' , edgecolor='black')
# 각 주별로 전체 사고난 횟수

sns.lineplot(data=car_crashes , x='abbrev' , y='speeding' , linewidth = 3, color='r', label='speeding')
sns.lineplot(data=car_crashes , x='abbrev' , y='alcohol' , linewidth = 3, color='g', label='alcohol')
sns.lineplot(data=car_crashes , x='abbrev' , y='no_previous' , linewidth = 3, color='b', label='no_previous')


plt.xlim(-1, 51)
plt.show()