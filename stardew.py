import numpy as np
from fealpy.mesh import MeshFactory
from fealpy.visualization import MeshShow

# 创建一个矩形网格
domain = [0, 1, 0, 1]  # 定义矩形区域 [xmin, xmax, ymin, ymax]
nx, ny = 10, 10  # 网格划分数量
mesh = MeshFactory.boxmesh2d(domain, nx, ny, meshtype='tri')

# 可视化网格
fig = MeshShow(mesh)
fig.show()