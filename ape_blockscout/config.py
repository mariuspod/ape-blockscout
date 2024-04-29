from ape.api.config import PluginConfig
from pydantic import AnyHttpUrl, model_validator
from pydantic_settings import SettingsConfigDict

class NetworkConfig(PluginConfig):
    uri: Optional[AnyHttpUrl] = None

class EcosystemConfig(PluginConfig):
    model_config = SettingsConfigDict(extra="allow")

    rate_limit: int = 5  # Requests per second
    retries: int = 5  # Number of retries before giving up

    @model_validator(mode="after")
    def verify_extras(self) -> "EcosystemConfig":
        if self.__pydantic_extra__:
            for aname in self.__pydantic_extra__.keys():
                self.__pydantic_extra__[aname] = NetworkConfig.model_validate(
                    self.__pydantic_extra__[aname]
                )
        return self


class BlockscoutConfig(PluginConfig):
    model_config = SettingsConfigDict(extra="allow")
    base: EcosystemConfig = EcosystemConfig()
    ethereum: EcosystemConfig = EcosystemConfig()
    gnosis: EcosystemConfig = EcosystemConfig()
    optimism: EcosystemConfig = EcosystemConfig()
    polygon: EcosystemConfig = EcosystemConfig()
