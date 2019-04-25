#!/usr/bin/env python3
# coding: UTF-8

from typing import Optional, Union, Iterable
from iso_type import IsoType
from iso_param import IsoParam
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

    @property
    def iso_type(self) -> IsoType:
        return self._iso_type

    @property
    def iso_param(self) -> IsoParam:
        return self._iso_param

    @abstractmethod
    def init_iso(self) -> None:
        pass

    @abstractmethod
    def perform_iso(self) -> None:
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




