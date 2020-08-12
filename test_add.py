#!/usr/lib/python

import numpy as np
import mindspore.context as context
import mindspore.nn as nn
from mindspore import Tensor
from mindspore.ops import functional as F

#context.set_context(mode=context.GRAPH_MODE, device_target="CPU")

#help(F)

x = Tensor(np.array([1,3,3,4]).astype(np.float32))
y = Tensor(np.array([1,3,3,4]).astype(np.float32))

print(F.tensor_add(x, y))

