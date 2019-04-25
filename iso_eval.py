#!/usr/bin/env python3.7
# coding: UTF-8

from typing import
from setting.base import IsoSetting, ProcSetting

class Evaluation:
    def __init__(self, iso_setting: IsoSetting, proc_setting: ProcSetting) -> None:
        self._iso_setting = iso_setting
        self._proc_setting = proc_setting

    @property
    def iso_setting(self) -> IsoSetting:
        return self._iso_setting

    @property
    def proc_setting(self) -> ProcSetting:
        return self._proc_setting

    def call_eval(self) -> None:
        print(f'Ready for testing isolations...')
        target_iso = self.iso_setting
        target_proc = self.proc_setting

        print(f'starting to isolation test...')


