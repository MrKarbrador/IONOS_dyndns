from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    bulk_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/dyndns/{bulkId}".format(client.base_url, bulkId=bulk_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Error]]]:
    if response.status_code == 200:
        response_200 = None

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
) -> Response[Union[Any, List[Error]]]:
    kwargs = _get_kwargs(
        bulk_id=bulk_id,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    bulk_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, List[Error]]]:
    """Disable Dynamic Dns for bulk id. The following quota applies: 1 request per minute per IP address."""

    return sync_detailed(
        bulk_id=bulk_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bulk_id: str,
    *,
    client: Client,
) -> Response[Union[Any, List[Error]]]:
    kwargs = _get_kwargs(
        bulk_id=bulk_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    bulk_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, List[Error]]]:
    """Disable Dynamic Dns for bulk id. The following quota applies: 1 request per minute per IP address."""

    return (
        await asyncio_detailed(
            bulk_id=bulk_id,
            client=client,
        )
    ).parsed
