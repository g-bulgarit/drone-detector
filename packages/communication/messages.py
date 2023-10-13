from dataclasses import dataclass, asdict


@dataclass
class BaseMessage:
    sender: "str"

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class NewFileFoundMsg(BaseMessage):
    path: str
