from minddocker.common.objects import base
from minddocker.common.objects import common


class RunnerDescription(base.StandardObject):
    SCHEMA_TYPE = "md_runner"
    SCHEMA_VERSION = "0.1.0"
    fields = {
        "platform": base.ObjectField(common.PlatformMetadata)
    }
