import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import Polygon
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
fig, ax = plt.subplots(figsize=(5.12, 5.12))

ax.set_facecolor('white')

hat_base = FancyBboxPatch((0.35, 0.6), 0.3, 0.1, boxstyle="round,pad=0.1", 
                          edgecolor='black', facecolor='purple', linewidth=2)
hat_top = Polygon([[0.4, 0.7], [0.5, 0.9], [0.6, 0.7]], closed=True, 
                  edgecolor='black', facecolor='purple', linewidth=2)

dollar_sign = TextPath((0.45, 0.2), "$", size=0.5, prop=dict(weight='bold'))

transform = Affine2D().translate(-0.05, 0) + ax.transData

ax.add_patch(hat_base)
ax.add_patch(hat_top)
ax.add_patch(Polygon(dollar_sign.to_polygons()[0], closed=True, transform=transform, color='green'))

ax.axis('off')
output_path = "res/stock_sage_icon_v2.png"
plt.savefig(output_path, dpi=100, bbox_inches='tight', pad_inches=0)
plt.show()
output_path