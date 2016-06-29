"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2009-2015 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x41f0e92d, 0xf44f2206, 0xf44f7144, 0xf0007080, 0xbb28f8f2, 0x02a52401, 0x52faf44f, 0x7c80f44f,
    0x760cf44f, 0xf04f2705, 0xf04f2340, 0xf8c3080f, 0x62ddc028, 0xf8c3631e, 0x635c7100, 0x50faf44f,
    0x10a0f8d3, 0x0f01f011, 0xb148d008, 0x80a0f8c3, 0x0200f8d3, 0x0f02f010, 0xe006d005, 0xd1ef1e40,
    0xe8bd2001, 0x1e5281f0, 0x2000d1e1, 0x81f0e8bd, 0x2000498a, 0x0154f8c1, 0xd1032a03, 0x2140f04f,
    0x65082001, 0x47702000, 0x47702000, 0x47f0e92d, 0xffb6f7ff, 0xbf082800, 0xd13e2060, 0x1e40bf00,
    0x22c7d1fc, 0x7144f44f, 0x7080f44f, 0xf8a3f000, 0xf44fbb80, 0x22007480, 0xf04f00a5, 0xf44f0c01,
    0x2705760c, 0x2340f04f, 0x080ff04f, 0x7a10f242, 0x62dd629c, 0xf8c3631e, 0xf8c37100, 0xf44fc034,
    0xf8d350fa, 0xf01110a0, 0xd0140f01, 0xf8c3b190, 0xf8d380a0, 0xf0100200, 0xbf180f01, 0x60e0f642,
    0xbf00d005, 0xd1fc1e40, 0x45521c52, 0x2000dbe0, 0x87f0e8bd, 0x1e40e001, 0x2001d1e3, 0x87f0e8bd,
    0x4604b510, 0xff6cf7ff, 0xbf082800, 0xd1102160, 0x1e49bf00, 0xba20d1fc, 0x0220f040, 0xf44f4958,
    0xf0007080, 0xb920f858, 0xf870f000, 0xbf082800, 0x2001bd10, 0xb570bd10, 0x460c4615, 0xf7ff4606,
    0x2800ff4f, 0xf04fd142, 0xf44f2340, 0x62987080, 0x62d80080, 0x1e60494b, 0x6000ea41, 0xba306318,
    0x0002f040, 0x0100f8c3, 0xf0242000, 0x2c000103, 0xf020d909, 0xf8df0203, 0x58aac110, 0x2000f84c,
    0x42841d00, 0x42a1d8f5, 0xf021d006, 0xf1010003, 0x58282140, 0x0200f8c1, 0xd2082ce0, 0xeba02008,
    0xeb001054, 0x00800040, 0x1e40bf00, 0x2001d1fc, 0xf44f6358, 0xf8d350fa, 0xf01110a0, 0xd0070f02,
    0xf000b120, 0x2800f823, 0xbd70bf08, 0xbd702001, 0xd1f01e40, 0xf04fe7fa, 0x62982340, 0x62d81518,
    0xf8c36319, 0x20012100, 0xf44f6358, 0xf8d350fa, 0xf01110a0, 0xd0050f02, 0x200fb130, 0x00a0f8c3,
    0x47702000, 0xd1f21e40, 0x47702001, 0x01f0e92d, 0xf44f2605, 0xf44f52fa, 0xf44f7c80, 0xf44f6480,
    0x2701750c, 0x2340f04f, 0x080ff04f, 0xc028f8c3, 0x631d62dc, 0x6100f8c3, 0xf44f635f, 0xf8d350fa,
    0xf01110a0, 0xd0120f01, 0xf8c3b198, 0xf8d380a0, 0xf0100200, 0xbf180f01, 0xd0042000, 0x28641c40,
    0x1e52dbfc, 0xe8bdd1e2, 0x200001f0, 0x1e404770, 0xe8bdd1e5, 0x200101f0, 0x00004770, 0x4004a000,
    0x00030310, 0x00030330, 0x40004200, 0x00000000,
    ],

    'pc_init' : 0x20000091,
    'pc_unInit': 0x200000A9,
    'pc_program_page': 0x20000177,
    'pc_erase_sector': 0x20000141,
    'pc_eraseAll' : 0x200000AD,

    'static_base' : 0x20000000 + 0x00000020 + 0x000002ac,
    'begin_stack' : 0x20000000 + 0x00000800,
    'begin_data' : 0x20000000 + 0x00000A00,
    'page_size' : 0x00000100,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000  # ITCM, Analyzer 0x00000000..0x000000600
};

class Flash_tz10xx(Flash):
    def __init__(self, target):
        super(Flash_tz10xx, self).__init__(target, flash_algo)

    def erasePage(self, flashPtr):
        # Flash memory is not inplemented PAGE ERASE command.
        # Emulate the PAGE ERASE command in the SECTOR ERASE command.
        sector_size = 0x1000    # 4kB
        page_size = 0x0100      # 256B
        page_count = int(sector_size / page_size)
        sector_addr = flashPtr & 0xfffff000
        page_index = (flashPtr & 0x00000f00) >> 8
        sector_datas = []
        # Save the sector datas.
        for i in range(0, page_count):
            data = self.target.readBlockMemoryUnaligned8(sector_addr + (i * page_size), page_size)
            sector_datas.append(data)
        # Check the target of erase page data.
        if all((x == 0xff for x in sector_datas[page_index])):
            # Already erased.
            return
        # Run SECTOR ERASE
        super(Flash_tz10xx, self).erasePage(sector_addr)
        # Restore the sector datas.
        for i in range(0, page_count):
            if i == page_index:
                # Skip the target of erase page.
                pass
            else:
                if any((x != 0xff for x in sector_datas[i])):
                    # Run PAGE PROGRAM
                    super(Flash_tz10xx, self).programPage(sector_addr + (i * page_size), sector_datas[i])
                else:
                    # Page data is all 0xff.
                    pass

    def eraseSector(self, flashPtr):
        super(Flash_tz10xx, self).erasePage(flashPtr & 0xfffff000)
