import numpy as np
import mindspore.context as context
from mindspore import Tensor
from mindspore.ops import functional as F

context.set_context(mode=context.GRAPH_MODE, device_target="CPU")

x = Tensor(np.ones([1,3,3,4]).astype(np.float32))
y = Tensor(np.ones([1,3,3,4]).astype(np.float32))
print(F.tensor_add(x, y))
