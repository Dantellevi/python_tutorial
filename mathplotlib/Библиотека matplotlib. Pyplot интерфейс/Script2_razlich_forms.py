
import matplotlib.pyplot as plt

fig=plt.figure()
#добавление на рисинок прямоугольной области рисования
ax=fig.add_axes([0,0,1,1])
print(type(ax))
plt.scatter(1.0,1.0)
plt.savefig('example_142a.png',fmt='png')


fig=plt.figure()
# Добавление на рисунок круговой области рисования
ax=fig.add_axes([0,0,1,1],polar=True)

plt.scatter(0.0,0.5)
plt.savefig('example_142b.png',fmt='png')

plt.show()
