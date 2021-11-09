from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.record import Record
from ..models.zone_types import ZoneTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerZone")


@attr.s(auto_attribs=True)
class CustomerZone:
    """ """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, ZoneTypes] = UNSET
    records: Union[Unset, List[Record]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        records: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()

                records.append(records_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ZoneTypes]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ZoneTypes(_type)

        records = []
        _records = d.pop("records", UNSET)
        for records_item_data in _records or []:
            records_item = Record.from_dict(records_item_data)

            records.append(records_item)

        customer_zone = cls(
            id=id,
            name=name,
            type=type,
            records=records,
        )

        customer_zone.additional_properties = d
        return customer_zone

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
