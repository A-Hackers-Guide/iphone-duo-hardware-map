# `/memory`

- Name: `memory`
- Parent: [`/`](root.md)
- phandle: `41`
- device_type: `memory`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x0 0x0` | | |

## All properties (4) [DT]

- **`AAPL,phandle`**: `41` (`0x29`) → phandle of [`/memory`](root__memory.md)
- **`device_type`**: `memory`
- **`name`**: `memory`
- **`reg`**: `0x0` (u64; as two u32: `0x0`, `0x0`)
