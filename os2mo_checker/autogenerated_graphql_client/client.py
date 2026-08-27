from .async_base_client import AsyncBaseClient
from .get_address_uuuid import GetAddressUuuid
from .input_types import AddressFilter
from .version import Version


def gql(q: str) -> str:
    return q


class GraphQLClient(AsyncBaseClient):

    async def version(self) -> Version:
        query = gql("""
            query Version {
              version {
                mo_version
                mo_hash
              }
            }
            """)
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Version.parse_obj(data)

    async def get_address_uuuid(self, filter: AddressFilter) -> GetAddressUuuid:
        query = gql("""
            query getAddressUuuid($filter: AddressFilter!) {
              addresses(filter: $filter) {
                objects {
                  current {
                    uuid
                    ituser_response {
                      current {
                        user_key
                        uuid
                        validity {
                          from
                          to
                        }
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"filter": filter}
        # print(f"Executing query with filter: {filter}")

        response = await self.execute(query=query, variables=variables)
        print(f"Response: {response}")

        data = self.get_data(response)
        return GetAddressUuuid.parse_obj(data)
