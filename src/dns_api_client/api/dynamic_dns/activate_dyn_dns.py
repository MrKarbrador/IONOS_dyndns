from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.dyn_dns_request import DynDnsRequest
from ...models.dynamic_dns import DynamicDns
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Dict[str, Any]:
    url = "{}/v1/dyndns".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[DynamicDns, List[Error]]]:
    if response.status_code == 200:
        response_200 = DynamicDns.from_dict(response.json())

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
    if response.status_code == 500:
        response_500 = []
        _response_500 = response.json()
        for response_500_item_data in _response_500:
            response_500_item = Error.from_dict(response_500_item_data)

            response_500.append(response_500_item)

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DynamicDns, List[Error]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Response[Union[DynamicDns, List[Error]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Optional[Union[DynamicDns, List[Error]]]:
    """Activate Dynamic Dns for a bundle of (sub)domains. The url from response will be used to update the ips of the (sub)domains."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Response[Union[DynamicDns, List[Error]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: DynDnsRequest,
) -> Optional[Union[DynamicDns, List[Error]]]:
    """Activate Dynamic Dns for a bundle of (sub)domains. The url from response will be used to update the ips of the (sub)domains."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
