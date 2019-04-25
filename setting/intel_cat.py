# coding: UTF-8

from typing import Union
from .base import IsoType, IsoParam, IsoSetting


class IntelCat(IsoSetting):
    def __init__(self, iso_type: IsoType, iso_param: IsoParam) -> None:
        super().__init__(iso_type, iso_param)

    def _perform_iso(self, cur_param: Union[int, str]) -> None:
        print(f'cur_param: {cur_param}')
        return

    def _next_param(self) -> Union[int, str]:
        return




