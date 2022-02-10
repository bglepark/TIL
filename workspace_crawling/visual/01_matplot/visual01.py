import matplotlib.pyplot as plt
# pip install matplotlib

fig = plt.figure() #figure는 도화지 전체를 나타낸다

ax = fig.subplots()

ax.plot([1, 2, 3, 4, 5])

plt.show()


