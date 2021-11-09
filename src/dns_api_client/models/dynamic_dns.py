from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynamicDns")


@attr.s(auto_attribs=True)
class DynamicDns:
    """ """

    bulk_id: Union[Unset, str] = UNSET
    update_url: Union[Unset, str] = UNSET
    domains: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bulk_id = self.bulk_id
        update_url = self.update_url
        domains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bulk_id is not UNSET:
            field_dict["bulkId"] = bulk_id
        if update_url is not UNSET:
            field_dict["updateUrl"] = update_url
        if domains is not UNSET:
            field_dict["domains"] = domains
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bulk_id = d.pop("bulkId", UNSET)

        update_url = d.pop("updateUrl", UNSET)

        domains = cast(List[str], d.pop("domains", UNSET))

        description = d.pop("description", UNSET)

        dynamic_dns = cls(
            bulk_id=bulk_id,
            update_url=update_url,
            domains=domains,
            description=description,
        )

        dynamic_dns.additional_properties = d
        return dynamic_dns

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
