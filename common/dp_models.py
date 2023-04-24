from dataclasses import dataclass
from enum import Enum
from typing import *


class InputPortType(Enum):
    S3 = 's3'
    LOCAL = 'local'


class FileFormat(Enum):
    PARQUET = 'parquet'
    CSV = 'csv'
    EXCEL = 'excel'


@dataclass
class InputOptions:
    file_path: str
    file_format: Optional[FileFormat] = 'parquet'


@dataclass
class InputPortConfig:
    name: str
    type: InputPortType
    options: InputOptions


@dataclass
class DPConfig:
    name: str
    owner: str
    domain: str
    input: List[InputPortConfig]
