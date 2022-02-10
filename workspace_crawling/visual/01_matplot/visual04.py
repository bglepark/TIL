import matplotlib.pyplot as plt
import random

# 원래 이렇게 해야 하는데 더 편한 방법은 아래
# fig = plt.figure()
# ax01 = fig.add_subplot(2, 2, 1)
# ax02 = fig.add_subplot(2, 2, 2)
# ax03 = fig.add_subplot(2, 2, 3)
# ax04 = fig.add_subplot(2, 2, 4)


fig , ax = plt.subplots(2, 2, figsize = (10,10))

x = list(range(50))
y01 = list(random.randint(0, 50) for i in range(50))
y02 = list(random.randint(0, 50) for i in range(50))
y03 = list(random.randint(0, 50) for i in range(50))
y04 = list(random.randint(0, 50) for i in range(50))

print(x)
print(y01)
print(y02)
print(y03)
print(y04)

# 산점도(scatter)
ax[0, 0].scatter(x, y01, color='red')
ax[0, 1].scatter(x, y01, color='green')
ax[1, 0].scatter(x, y01, color='blue')
ax[1, 1].scatter(x, y01, color='yellow')

ax[0,0].set_title('y01')
ax[0,1].set_title('y02')
ax[1,0].set_title('y03')
ax[1,1].set_title('y04')

fig.tight_layout() # 간격들을 조절

plt.show()