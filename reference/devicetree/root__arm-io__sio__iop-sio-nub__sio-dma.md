# `/arm-io/sio/iop-sio-nub/sio-dma`

- Name: `sio-dma`
- Parent: [`/arm-io/sio/iop-sio-nub`](root__arm-io__sio__iop-sio-nub.md)
- phandle: `137`
- compatible: `sio-dma-controller`
- device_type: `sio-dma`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Referenced by (1) [DT]

- [`/arm-io/spi1`](root__arm-io__spi1.md): `dma-parent`

## All properties (4) [DT]

- **`AAPL,phandle`**: `137` (`0x89`) → phandle of [`/arm-io/sio/iop-sio-nub/sio-dma`](root__arm-io__sio__iop-sio-nub__sio-dma.md)
- **`compatible`**: `sio-dma-controller`
- **`device_type`**: `sio-dma`
- **`name`**: `sio-dma`
