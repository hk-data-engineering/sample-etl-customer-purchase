from dataclasses import dataclass
from typing import *


@dataclass
class InputOptions:
    file_name: str
    file_path: str
    file_format: Optional[str] = 'parquet'


@dataclass
class InputPortConfig:
    name: str
    type: str
    options: InputOptions


@dataclass
class DPConfig:
    name: str
    owner: str
    domain: str
    input: List[InputPortConfig]
