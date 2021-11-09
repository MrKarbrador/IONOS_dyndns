from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordUpdate")


@attr.s(auto_attribs=True)
class RecordUpdate:
    """ """

    disabled: Union[Unset, bool] = False
    content: Union[Unset, str] = UNSET
    ttl: Union[Unset, int] = UNSET
    prio: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disabled = self.disabled
        content = self.content
        ttl = self.ttl
        prio = self.prio

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
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
        disabled = d.pop("disabled", UNSET)

        content = d.pop("content", UNSET)

        ttl = d.pop("ttl", UNSET)

        prio = d.pop("prio", UNSET)

        record_update = cls(
            disabled=disabled,
            content=content,
            ttl=ttl,
            prio=prio,
        )

        record_update.additional_properties = d
        return record_update

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
