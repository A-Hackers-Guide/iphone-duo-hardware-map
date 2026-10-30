# `/arm-io/pmp/iop-pmp-nub/:borneo_h19p_0`

- Name: `:borneo_h19p_0`
- Parent: [`/arm-io/pmp/iop-pmp-nub`](root__arm-io__pmp__iop-pmp-nub.md)
- phandle: `121`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Firmware with a matching name [FW]

- [`Firmware/avd/AppleAVDFW_H19P.im4p`](../firmware/Firmware__avd__AppleAVDFW_H19P.im4p.md) (107,464 B) Tag: IM4P  Type: avdf  Version: 280d6e11

## All properties (3) [DT]

- **`AAPL,phandle`**: `121` (`0x79`) → phandle of [`/arm-io/pmp/iop-pmp-nub/:borneo_h19p_0`](root__arm-io__pmp__iop-pmp-nub___borneo_h19p_0.md)
- **`fast-die-ctrl-ce-map`**: 88 bytes
  - u32: `0x1 0x0 0x0 0x1 0x0 0x0 0x0 0x43434145 0x0 0x0 0x0 0x2 0x0 0x1 0x2 0x3 0x4 0x0 0x43434150 0x454e415f 0x4e415f30 0x3145`
  - text inside: `EACC`, `PACC_ANE0_ANE1`
  ```
  000000  01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00  ................
  000010  00 00 00 00 00 00 00 00 00 00 00 00 45 41 43 43  ............EACC
  000020  00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00  ................
  000030  00 00 00 00 01 00 00 00 02 00 00 00 03 00 00 00  ................
  000040  04 00 00 00 00 00 00 00 50 41 43 43 5f 41 4e 45  ........PACC_ANE
  000050  30 5f 41 4e 45 31 00 00                          0_ANE1..
  ```
- **`name`**: `:borneo_h19p_0`
