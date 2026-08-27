from pydantic import BaseSettings, AnyHttpUrl, SecretStr, parse_obj_as
from fastramqpi.config import ClientSettings

class SimpleSettings(BaseSettings):
    # If outside the mo docker network, use the external URL
    # mo_base_url: str = "http://localhost:5000"
    # Otherwise, use the internal URL
    mo_base_url: str = "http://mo:5000"
    graphql_version: str = "v30"
    mo_url_str: str = f"{mo_base_url}/graphql/{graphql_version}"
    mo_url: AnyHttpUrl = parse_obj_as(AnyHttpUrl, mo_url_str)
    # If outside the keycloak docker network, use the external URL
    #auth_base_url: str = "http://localhost:8090"
    # Otherwise, use the internal URL
    auth_base_url: str = "http://keycloak:8080"
    auth_server_str: str = (f"{auth_base_url}/auth")
    auth_server: AnyHttpUrl = parse_obj_as(AnyHttpUrl, auth_server_str)

    auth_realm: str = "mo"

    client_id: str = "dipex"
    client_secret: str = "49d427ce-ad66-467a-a72e-76c7b5d3f500"
    graphql_timeout: int = 600

def get_client_settings() -> ClientSettings:
    settings = SimpleSettings()
    return ClientSettings(
        mo_url=parse_obj_as(AnyHttpUrl, settings.mo_base_url),
        client_id=settings.client_id,
        client_secret=SecretStr(settings.client_secret),
        auth_realm=settings.auth_realm,
        auth_server=settings.auth_server,
        graphql_timeout=settings.graphql_timeout,
    )
