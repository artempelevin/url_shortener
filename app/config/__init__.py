from typing import Any

import toml
from pydantic import BaseModel, validator


class Config(BaseModel):
    deploy: "DeployParams"
    server: "ServerParams"
    database: "DatabaseParams"


class DeployParams(BaseModel):
    debug: bool


class ServerParams(BaseModel):
    host: str
    port: int

    @validator('host')
    def host_validate(cls, host: str) -> str:
        digits = host.split('.')
        assert len(digits) == 4, "Host in must have 4 digits! (example mask: 'xxx.xxx.xxx.xxx')"
        for digit in digits:
            assert digit.isdigit(), f"'{digit}' is not digit in host string!"
            assert 0 <= int(digit) <= 255, f"'{digit}' not included in the range [1; 255]"
        return host


class DatabaseParams(BaseModel):
    url: str


def load_config() -> dict[str, Any]:
    with open('app/config/config.toml', 'r', encoding='utf-8') as file:
        return dict(toml.load(file))


Config.update_forward_refs()
config = Config(**load_config())
