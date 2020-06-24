import numpy as np
import mindspore.context as context
import mindspore.nn as nn
from mindspore import Tensor
from mindspore.ops import operations as P
from mindspore.ops import functional as F

context.set_context(mode=context.GRAPH_MODE, device_target="CPU")

#help(F)


class NewAddN(nn.Cell):
    def __init__(self):
        super(NewAddN, self).__init__()
        self.addN = P.AddN()

    def construct(self, *x):
        return self.addN(x)

x = Tensor(np.array([1,3,3,4]).astype(np.float32))
y = Tensor(np.array([1,3,3,4]).astype(np.float32))

addn = NewAddN()
print(addn(x, y))

