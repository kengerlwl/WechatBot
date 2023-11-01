import json
from typing import Any, Dict, Type, TypeVar

T = TypeVar('T')


def to_json(entity: T) -> str:
    # 已经是json就不用转换了
    if (type(entity) == dict) or (type(entity) == str)or (type(entity) == list):
        return entity


    data: Dict[str, Any] = {}
    for attr in vars(entity):
        data[attr] = getattr(entity, attr)
    return data



def from_json(json_str: str, entity_type: Type[T]) -> T:
    data = json.loads(json_str)
    return entity_type(**data)
