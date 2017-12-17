import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import mplcursors

fig, ax = plt.subplots()

rtgs = []
for i in range(4):
    rtgs.append(ax.add_patch(Rectangle((i/10 + 0.1, i/10 + 0.1), 0.2, 0.2, ec='black', label=i)))
c = mplcursors.cursor(rtgs, hover=True)

c.connect("add", lambda sel: sel.annotation.set_text(sel.artist.get_label()))

plt.show()
