from minddocker.common.objects import base
from minddocker.common.objects import common


class Container(base.StandardObject):
    SCHEMA_TYPE = "md_platform_container"
    SCHEMA_VERSION = "0.1.0"
    fields = {
        "runtime": base.PrimitiveField(),
        "image": base.PrimitiveField()
    }


class PlatformConfig(base.StandardObject):
    SCHEMA_TYPE = "md_platform"
    SCHEMA_VERSION = "0.1.0"
    fields = {
        "platform": base.ObjectField(common.PlatformMetadata),
        "container": base.ObjectField(Container)
    }
