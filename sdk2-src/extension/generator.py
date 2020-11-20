from azure.ml._schema import ModelSchema, CommandJobSchema, CodeAssetSchema, OnlineEndpointDeploymentSchema, \
    OnlineEndpointSchema, EnvironmentSchema, AssetSchema, SweepJobSchema, YamlFileSchema
from marshmallow_jsonschema import JSONSchema
from marshmallow import fields
from pathlib import Path
import json
from azure.ml._schema import UnionField, YamlFileSchema


class PatchedJSONSchema(JSONSchema):
    def __init__(self, *args, **kwargs):
        """Setup internal cache of nested fields, to prevent recursion.
        :param bool props_ordered: if `True` order of properties will be save as declare in class,
                                   else will using sorting, default is `False`.
                                   Note: For the marshmallow scheme, also need to enable
                                   ordering of fields too (via `class Meta`, attribute `ordered`).
        """
        self._nested_schema_classes = {}
        self.nested = kwargs.pop("nested", False)
        self.props_ordered = kwargs.pop("props_ordered", False)
        setattr(self.opts, "ordered", self.props_ordered)
        super(PatchedJSONSchema, self).__init__(*args, **kwargs)

    def _from_python_type(self, obj, field, pytype):
        metadata = field.metadata.get("metadata", {})
        metadata.update(field.metadata)
        values = metadata.get("values", {})
        if pytype == dict and values:
            json_schema = {"title": field.attribute or field.name}
            json_schema["type"] = "object"
            json_schema["additionalProperties"] = self._get_schema_for_field(obj, values)
            return json_schema
        else:
            return super(PatchedJSONSchema, self)._from_python_type(obj, field, pytype)


    def _get_schema_for_field(self, obj, field):
        """Get schema and validators for field."""
        if hasattr(field, "_jsonschema_type_mapping"):
            schema = field._jsonschema_type_mapping()
        elif "_jsonschema_type_mapping" in field.metadata:
            schema = field.metadata["_jsonschema_type_mapping"]
        else:
            if isinstance(field, UnionField):
                has_yaml_option = False
                schemas = []
                for field_item in field._union_fields:
                    if isinstance(field_item, fields.Nested):
                        field_item.parent = field.parent
                        context = getattr(field_item.parent, "context", {})
                        field_item.schema.context.update(context)
                        if isinstance(field_item.schema, YamlFileSchema):
                            has_yaml_option = True
                    schemas.append(self._get_schema_for_field(obj, field_item))
                if has_yaml_option:
                    schemas.append({
                        "type": "string",
                        "pattern": "^file:.*"
                    })
                schema = { 
                    "anyOf": schemas
                }
            else: 
                schema = super(PatchedJSONSchema, self)._get_schema_for_field(obj, field)
        return schema


schemas = {
    "model": ModelSchema,
    "commandJob": CommandJobSchema,
    "codeAsset": CodeAssetSchema,
    "environment": EnvironmentSchema,
    "deployment": OnlineEndpointDeploymentSchema,
    "onlineEndpoint": OnlineEndpointSchema,
    "sweepJob": SweepJobSchema,
    "asset": AssetSchema
}

for name, schema in schemas.items():
    path = Path("./schema", name + ".schema.json")
    with open(path, mode="w") as f:
        obj = PatchedJSONSchema().dump(schema(context={"base_path": "./"}))
        json.dump(obj, f, indent=4)

