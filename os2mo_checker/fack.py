from os2mo_checker.utils import Utils
from os2mo_checker.config import get_client_settings
from fastramqpi.main import construct_mo_client

async def main():
    settings = get_client_settings()
    mo_client = construct_mo_client(settings)
    print(mo_client.base_url)
    response = await mo_client.get("/graphql/v30/schema.graphql")
    print(response.status_code)
    print(response.text[:500])

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
