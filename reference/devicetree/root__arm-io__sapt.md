# `/arm-io/sapt`

- Name: `sapt`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `446`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (4) [DT]

- **`AAPL,phandle`**: `446` (`0x1be`) → phandle of [`/arm-io/sapt`](root__arm-io__sapt.md)
- **`apf`**: 192 bytes
  - u32: `0x111 0x200c4000 0x2 0x200dbfff 0x2 0x231 0x211 0x803c0000 0x2 0x803c3fff 0x2 0x211 0x211 0x803d0000 0x2 0x803d3fff 0x2 0x231 0x11 0x8c840000 0x2 0x8c863fff 0x2 0x11 0x44 0x83a00000 0x2 0x83bfffff 0x2 0x231 0x44 0x96000000 0x2 0x961fffff 0x2 0x231 0x11 0x80280000 0x2 0x8029ffff 0x2 0x11 0x211 0xa8000000 0x2 0xabffffff 0x2 0x231`
  ```
  000000  11 01 00 00 00 40 0c 20 02 00 00 00 ff bf 0d 20  .....@. ....... 
  000010  02 00 00 00 31 02 00 00 11 02 00 00 00 00 3c 80  ....1.........<.
  000020  02 00 00 00 ff 3f 3c 80 02 00 00 00 11 02 00 00  .....?<.........
  000030  11 02 00 00 00 00 3d 80 02 00 00 00 ff 3f 3d 80  ......=......?=.
  000040  02 00 00 00 31 02 00 00 11 00 00 00 00 00 84 8c  ....1...........
  000050  02 00 00 00 ff 3f 86 8c 02 00 00 00 11 00 00 00  .....?..........
  000060  44 00 00 00 00 00 a0 83 02 00 00 00 ff ff bf 83  D...............
  000070  02 00 00 00 31 02 00 00 44 00 00 00 00 00 00 96  ....1...D.......
  000080  02 00 00 00 ff ff 1f 96 02 00 00 00 31 02 00 00  ............1...
  000090  11 00 00 00 00 00 28 80 02 00 00 00 ff ff 29 80  ......(.......).
  0000a0  02 00 00 00 11 00 00 00 11 02 00 00 00 00 00 a8  ................
  0000b0  02 00 00 00 ff ff ff ab 02 00 00 00 31 02 00 00  ............1...
  ```
- **`name`**: `sapt`
- **`policy`**: `2` (`0x2`)
