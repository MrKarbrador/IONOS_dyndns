from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.record_types import RecordTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@attr.s(auto_attribs=True)
class Record:
    """ """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = False
    type: Union[Unset, RecordTypes] = UNSET
    content: Union[Unset, str] = UNSET
    ttl: Union[Unset, int] = UNSET
    prio: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        disabled = self.disabled
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        content = self.content
        ttl = self.ttl
        prio = self.prio

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if type is not UNSET:
            field_dict["type"] = type
        if content is not UNSET:
            field_dict["content"] = content
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if prio is not UNSET:
            field_dict["prio"] = prio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        disabled = d.pop("disabled", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, RecordTypes]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RecordTypes(_type)

        content = d.pop("content", UNSET)

        ttl = d.pop("ttl", UNSET)

        prio = d.pop("prio", UNSET)

        record = cls(
            id=id,
            name=name,
            disabled=disabled,
            type=type,
            content=content,
            ttl=ttl,
            prio=prio,
        )

        record.additional_properties = d
        return record

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
