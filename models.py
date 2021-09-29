from dataclasses import dataclass


@dataclass
class RequestModel:
    type: str
    body: str


@dataclass
class PubModel:
    type: str
    body: str
