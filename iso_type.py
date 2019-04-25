
from enum import IntEnum


class IsoType(IntEnum):
    HW = 0
    SW = 1


class HWIso(IntEnum):
    INTEL_CAT = 0
    PER_CORE_DVFS = 1


class SWIso(IntEnum):
    CPU_CORES = 0
    CPU_CYCLES = 1
    MIGRATION = 2   # TODO: Change Mapping Between Threads and Cores
