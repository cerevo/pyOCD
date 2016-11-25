"""
TOSHIBA TZ10xx serias
"""
from .coresight_target import CoreSightTarget
from .memory_map import (FlashRegion, RamRegion, MemoryMap)
from time import sleep

class TZ10xx(CoreSightTarget):

    has_fpu = True
    memoryMap = MemoryMap(
        FlashRegion(    start=0,           length=0x00100000,   blocksize=0x100, isBootMemory=True),   #On package NOR Flash
        RamRegion(      start=0x10000000,  length=0x00040000),                                          #Code region
        RamRegion(      start=0x20000000,  length=0x00008000)                                           #Data region
        )

    def __init__(self, link):
        super(TZ10xx, self).__init__(link, self.memoryMap)

    def reset(self, software_reset=True):
        super(TZ10xx, self).reset(True)

