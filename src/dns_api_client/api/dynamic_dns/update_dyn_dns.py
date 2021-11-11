from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.dyn_dns_request import DynDnsRequest
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    bulk_id: str,
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Dict[str, Any]:
    url = "{}/v1/dyndns/{bulkId}".format(client.base_url, bulkId=bulk_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Error]]]:
    if response.status_code == 200:
        response_200 = None

        return response_200
    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = Error.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400
    if response.status_code == 401:
        response_401 = []
        _response_401 = response.json()
        for response_401_item_data in _response_401:
            response_401_item = Error.from_dict(response_401_item_data)

            response_401.append(response_401_item)

        return response_401
    if response.status_code == 403:
        response_403 = []
        _response_403 = response.json()
        for response_403_item_data in _response_403:
            response_403_item = Error.from_dict(response_403_item_data)

            response_403.append(response_403_item)

        return response_403
    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = Error.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404
    if response.status_code == 500:
        response_500 = []
        _response_500 = response.json()
        for response_500_item_data in _response_500:
            response_500_item = Error.from_dict(response_500_item_data)

            response_500.append(response_500_item)

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    bulk_id: str,
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Response[Union[Any, List[Error]]]:
    kwargs = _get_kwargs(
        bulk_id=bulk_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    bulk_id: str,
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Optional[Union[Any, List[Error]]]:
    """Update Dynamic Dns for bulk id. The following quota applies: 1 request per minute per IP address."""

    return sync_detailed(
        bulk_id=bulk_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    bulk_id: str,
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Response[Union[Any, List[Error]]]:
    kwargs = _get_kwargs(
        bulk_id=bulk_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    bulk_id: str,
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Optional[Union[Any, List[Error]]]:
    """Update Dynamic Dns for bulk id. The following quota applies: 1 request per minute per IP address."""

    return (
        await asyncio_detailed(
            bulk_id=bulk_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
