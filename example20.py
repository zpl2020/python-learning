import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
fig.set_facecolor('r')
plt.axis('off')
circ = plt.Circle((0.5,0.5), 0.15, color = 'b', alpha = 0.5)
circ1 = plt.Circle((0.4,0.5), 0.15, color = 'r', alpha = 1.0)
ax.add_patch(circ)
ax.add_patch(circ1)
plt.show()