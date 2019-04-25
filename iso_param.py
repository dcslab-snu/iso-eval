# coding: UTF-8

from typing import Optional, Union, Iterable


class IsoStep:
    """
    This class abstracts the isolation step parameters
    """
    def __init__(self, start_param: Union[int, str], num_of_steps: int,
                 strides: int, first_time: int, interval: int) -> None:
        self._start_param = start_param
        self._num_of_steps = num_of_steps
        self._strides = strides
        self._first_time = first_time
        self._interval = interval

    @property
    def start_param(self) -> Union[int, str]:
        return self._start_param

    @property
    def num_of_steps(self) -> int:
        return self._num_of_steps

    @property
    def strides(self) -> int:
        return self._strides

    @property
    def first_time(self) -> int:
        return self._first_time

    @property
    def interval(self) -> int:
        return self._interval


class IsoSeq:
    """
    This class express the exact sequence for isolation
    """
    def __init__(self, seq: Iterable) -> None:
        self._seq = seq


class IsoParam:
    def __init__(self, iso_step: Optional[IsoStep], iso_seq: Optional[IsoSeq]) -> None:
        self._iso_step = iso_step
        self._iso_seq = iso_seq

    @property
    def iso_step(self) -> IsoStep:
        return self._iso_step

    @property
    def iso_seq(self) -> IsoSeq:
        return self._iso_seq

