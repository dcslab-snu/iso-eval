#!/usr/bin/env python3
# coding: UTF-8

import time
from typing import Optional, Union, Iterable
from iso_type import IsoType
from iso_param import IsoParam, IsoStep, IsoSeq
from abc import *

from utils import DVFS, ResCtrl, numa_topology
from utils.cgroup import Cpu, CpuSet


class IsoSetting(metaclass=ABCMeta):
    """
    This class contains all information for the setting of isolation techniques used to measure their performance effects.
    """
    def __init__(self, iso_type: IsoType, iso_param: IsoParam) -> None:
        self._iso_type = iso_type
        self._iso_param = iso_param
        self._first_interval = self.iso_step.first_time
        self._interval = self.iso_step.interval
        self._num_of_steps = self.iso_step.num_of_steps

    @property
    def iso_type(self) -> IsoType:
        return self._iso_type

    @property
    def iso_param(self) -> IsoParam:
        return self._iso_param

    @property
    def iso_step(self) -> IsoStep:
        return self.iso_param.iso_step

    @property
    def iso_seq(self) -> IsoSeq:
        return self.iso_param.iso_seq

    @property
    def first_interval(self) -> int:
        return self._first_interval

    @property
    def interval(self) -> int:
        return self._interval

    @property
    def num_of_steps(self) -> int:
        return self._num_of_steps

    def perform_iso(self) -> None:
        print(f'starting perform_iso...')
        counts = 0
        print(f'waiting first interval...')
        time.sleep(self.first_interval)
        print(f'perform isolation... (counts: {counts})')
        self._perform_iso(self.iso_step.start_param)
        counts += 1

        # Perform isolations
        while counts < self.num_of_steps:
            time.sleep(self.interval)
            next_param = self._next_param()
            print(f'perform isolation... (counts: {counts})')
            self._perform_iso(next_param)

    @abstractmethod
    def _perform_iso(self, next_param: Union[int, str]) -> None:
        pass

    @abstractmethod
    def _next_param(self) -> Union[int, str]:
        pass


class ProcSetting:
    """
    This class contains all information for the setting of processes to be evaluated and manipulated.
    """
    def __init__(self, wl_name: str, wl_type: str, pid: int, perf_pid: int, perf_interval: int) -> None:
        self._wl_name = wl_name
        self._wl_type = wl_type
        self._pid = pid
        self._perf_pid = perf_pid
        self._perf_interval = perf_interval

        self._cgroup_cpuset = CpuSet(self.group_name)
        self._cgroup_cpu = Cpu(self.group_name)
        self._resctrl = ResCtrl(self.group_name)
        self._dvfs = DVFS(self.group_name)

    @property
    def wl_name(self) -> str:
        return self._wl_name

    @property
    def wl_type(self) -> str:
        return self._wl_type

    @property
    def pid(self) -> int:
        return self._pid

    @property
    def perf_pid(self) -> int:
        return self._perf_pid

    @property
    def perf_interval(self) -> int:
        return self._perf_interval

    @property
    def group_name(self) -> str:
        return f'{self._wl_name}_{self._pid}'




