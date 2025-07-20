import matplotlib.pyplot as plt  

import pickle

with open("keydata.pkl","rb") as f:
    keycount = pickle.load(f)


keyboard_layout = {
    'q': (0, 2), 'w': (1, 2), 'e': (2, 2), 'r': (3, 2), 't': (4, 2),
    'y': (5, 2), 'u': (6, 2), 'i': (7, 2), 'o': (8, 2), 'p': (9, 2),
    'a': (0.5, 1), 's': (1.5, 1), 'd': (2.5, 1), 'f': (3.5, 1), 'g': (4.5, 1),
    'h': (5.5, 1), 'j': (6.5, 1), 'k': (7.5, 1), 'l': (8.5, 1),
    'z': (1, 0), 'x': (2, 0), 'c': (3, 0), 'v': (4, 0), 'b': (5, 0),
    'n': (6, 0), 'm': (7, 0)
}

x,y,colors, labels = [] ,[] ,[] ,[]

for key , pos in keyboard_layout.items():
    count =keycount.get(key,0)
    x.append(pos[0])
    y.append(pos[1])
    colors.append(count)
    labels.append(f"{key}\n{count}")

plt.figure(figsize=(10, 4))
sc = plt.scatter(x, y, c=colors, cmap='hot', s=2000, edgecolors='black')

for i, label in enumerate(labels):
    plt.text(x[i], y[i], label, ha='center', va='center', fontsize=10, color='white')

plt.colorbar(sc, label='Key Press Count')
plt.title("Keyboard Heatmap")
plt.axis('off')
plt.tight_layout()
plt.show()