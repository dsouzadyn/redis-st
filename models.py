from dataclasses import dataclass

@dataclass
class RequestModel:
    type: str
    body: str