from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.customer_zone import CustomerZone
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    zone_id: str,
    *,
    client: Client,
    suffix: Union[Unset, None, str] = UNSET,
    record_name: Union[Unset, None, str] = UNSET,
    record_type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/zones/{zoneId}".format(client.base_url, zoneId=zone_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "suffix": suffix,
        "recordName": record_name,
        "recordType": record_type,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CustomerZone, List[Error]]]:
    if response.status_code == 200:
        response_200 = CustomerZone.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = []
        _response_401 = response.json()
        for response_401_item_data in _response_401:
            response_401_item = Error.from_dict(response_401_item_data)

            response_401.append(response_401_item)

        return response_401
    if response.status_code == 500:
        response_500 = []
        _response_500 = response.json()
        for response_500_item_data in _response_500:
            response_500_item = Error.from_dict(response_500_item_data)

            response_500.append(response_500_item)

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CustomerZone, List[Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    zone_id: str,
    *,
    client: Client,
    suffix: Union[Unset, None, str] = UNSET,
    record_name: Union[Unset, None, str] = UNSET,
    record_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[CustomerZone, List[Error]]]:
    kwargs = _get_kwargs(
        zone_id=zone_id,
        client=client,
        suffix=suffix,
        record_name=record_name,
        record_type=record_type,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    zone_id: str,
    *,
    client: Client,
    suffix: Union[Unset, None, str] = UNSET,
    record_name: Union[Unset, None, str] = UNSET,
    record_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[CustomerZone, List[Error]]]:
    """Returns a customer zone."""

    return sync_detailed(
        zone_id=zone_id,
        client=client,
        suffix=suffix,
        record_name=record_name,
        record_type=record_type,
    ).parsed


async def asyncio_detailed(
    zone_id: str,
    *,
    client: Client,
    suffix: Union[Unset, None, str] = UNSET,
    record_name: Union[Unset, None, str] = UNSET,
    record_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[CustomerZone, List[Error]]]:
    kwargs = _get_kwargs(
        zone_id=zone_id,
        client=client,
        suffix=suffix,
        record_name=record_name,
        record_type=record_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    zone_id: str,
    *,
    client: Client,
    suffix: Union[Unset, None, str] = UNSET,
    record_name: Union[Unset, None, str] = UNSET,
    record_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[CustomerZone, List[Error]]]:
    """Returns a customer zone."""

    return (
        await asyncio_detailed(
            zone_id=zone_id,
            client=client,
            suffix=suffix,
            record_name=record_name,
            record_type=record_type,
        )
    ).parsed
