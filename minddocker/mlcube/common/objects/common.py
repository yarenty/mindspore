from minddocker.common.objects import base


class PlatformMetadata(base.StandardObject):
    SCHEMA_TYPE = "md_platform_metadata"
    SCHEMA_VERSION = "0.1.0"
    fields = {
        "name": base.PrimitiveField(),
        "version": base.PrimitiveField()
    }
