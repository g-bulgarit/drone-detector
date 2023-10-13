from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class BaseMessage:
    sender: "str"

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class NewFileFound(BaseMessage):
    path: Path
