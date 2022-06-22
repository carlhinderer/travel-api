from marshmallow import Schema, fields, validate


class HotelSchema(Schema):        
    class Meta:
        ordered = True

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=[validate.Length(max=200)])