from ninja import Schema, Field
from typing import List, Optional

class RegionOut(Schema):
    name: str

class TrustOut(Schema):
    id: int
    name: str
    region: RegionOut

class TrustsOut(Schema):
    trusts: List[TrustOut]