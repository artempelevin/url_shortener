from typing import Any

import toml
from pydantic import BaseModel, validator


class Config(BaseModel):
    deploy: "DeployParams"
    server: "ServerParams"
    api_paths: "ApiPathsParams"
    database: "DatabaseParams"
    redis: "RedisParams"


class DeployParams(BaseModel):
    debug: bool


class ServerParams(BaseModel):
    host: str
    port: int
    domain: str

    @validator('host')
    def host_checking(cls, host: str) -> str:
        digits = host.split('.')
        assert len(digits) == 4, "Host in must have 4 digits! (example mask: 'xxx.xxx.xxx.xxx')"
        for digit in digits:
            assert digit.isdigit(), f"'{digit}' is not digit in host string!"
            assert 0 <= int(digit) <= 255, f"'{digit}' not included in the range [1; 255]"
        return host


class ApiPathsParams(BaseModel):
    urls: str
    statistics: str

    @validator('urls')
    def checking_urls_path(cls, urls_path: str) -> str:
        return cls._checking_path(path=urls_path)

    @validator('statistics')
    def checking_statistics_path(cls, statistics_path: str) -> str:
        return cls._checking_path(path=statistics_path)

    @staticmethod
    def _checking_path(path: str) -> str:
        alphabet = 'zyxwvutsrqponmlkjihgfedcba0123456789/'
        if not all(True for letter in alphabet if letter in alphabet):
            raise ValueError(f"'{path}' invalid URL path")
        return path


class DatabaseParams(BaseModel):
    url: str


class RedisParams(BaseModel):
    url: str


def load_config() -> dict[str, Any]:
    with open('app/config/config.toml', 'r', encoding='utf-8') as file:
        return dict(toml.load(file))


Config.update_forward_refs()
config = Config(**load_config())
