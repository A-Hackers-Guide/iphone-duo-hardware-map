# `/arm-io/pmp/iop-pmp-nub/:borneo_h19a_0`

- Name: `:borneo_h19a_0`
- Parent: [`/arm-io/pmp/iop-pmp-nub`](root__arm-io__pmp__iop-pmp-nub.md)
- phandle: `120`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (3) [DT]

- **`AAPL,phandle`**: `120` (`0x78`) → phandle of [`/arm-io/pmp/iop-pmp-nub/:borneo_h19a_0`](root__arm-io__pmp__iop-pmp-nub___borneo_h19a_0.md)
- **`fast-die-ctrl-ce-map`**: 88 bytes
  - u32: `0x1 0x0 0x0 0x1 0x0 0x0 0x0 0x43434145 0x0 0x0 0x0 0x2 0x0 0x1 0x2 0x3 0x0 0x0 0x43434150 0x454e415f 0x30 0x0`
  - text inside: `EACC`, `PACC_ANE0`
  ```
  000000  01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00  ................
  000010  00 00 00 00 00 00 00 00 00 00 00 00 45 41 43 43  ............EACC
  000020  00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00  ................
  000030  00 00 00 00 01 00 00 00 02 00 00 00 03 00 00 00  ................
  000040  00 00 00 00 00 00 00 00 50 41 43 43 5f 41 4e 45  ........PACC_ANE
  000050  30 00 00 00 00 00 00 00                          0.......
  ```
- **`name`**: `:borneo_h19a_0`
