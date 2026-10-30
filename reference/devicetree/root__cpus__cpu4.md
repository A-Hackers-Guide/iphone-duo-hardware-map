# `/cpus/cpu4`

- Name: `cpu4`
- Parent: [`/cpus`](root__cpus.md)
- phandle: `34`
- compatible: `apple,everest`, `ARM,v8`
- device_type: `cpu`
- Children (2): [`/cpus/cpu4/:borneo_h19a_4`](root__cpus__cpu4___borneo_h19a_4.md), [`/cpus/cpu4/:borneo_h19p_4`](root__cpus__cpu4___borneo_h19p_4.md)

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x100` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`70`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `error_handler` | [`/arm-io`](root__arm-io.md) | `ErrH` | `0x6` |
| `enable_core` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `Core` | `0x40` |
| `cpu_idle` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `cpuI` | `` |

## All properties (22) [DT]

- **`AAPL,phandle`**: `34` (`0x22`) → phandle of [`/cpus/cpu4`](root__cpus__cpu4.md)
- **`acc-impl-reg`**: 16 bytes
  - u32: `0x11f00000 0x2 0x40088 0x0`
  ```
  000000  00 00 f0 11 02 00 00 00 88 00 04 00 00 00 00 00  ................
  ```
- **`cluster-id`**: `1` (`0x1`)
- **`cluster-type`**: `P`
- **`compatible`**: `apple,everest`, `ARM,v8`
- **`coresight-reg`**: 16 bytes
  - u32: `0x11010000 0x2 0x300c8 0x0`
  ```
  000000  00 00 01 11 02 00 00 00 c8 00 03 00 00 00 00 00  ................
  ```
- **`cpm-impl-reg`**: 16 bytes
  - u32: `0x11e40000 0x2 0xc028 0x0`
  ```
  000000  00 00 e4 11 02 00 00 00 28 c0 00 00 00 00 00 00  ........(.......
  ```
- **`cpu-id`**: `4` (`0x4`)
- **`cpu-impl-reg`**: 16 bytes
  - u32: `0x11050000 0x2 0x9010 0x0`
  ```
  000000  00 00 05 11 02 00 00 00 10 90 00 00 00 00 00 00  ................
  ```
- **`cpu-uttdbg-reg`**: 16 bytes
  - u32: `0x11040000 0x2 0xc8 0x0`
  ```
  000000  00 00 04 11 02 00 00 00 c8 00 00 00 00 00 00 00  ................
  ```
- **`device_type`**: `cpu`
- **`function-cpu_idle`**: `0x6370754900000030` (u64; as two u32: `0x30`, `0x63707549`)
- **`function-enable_core`**: `0`, `eroC@`
- **`function-error_handler`**: 12 bytes
  - u32: `0x2c 0x45727248 0x6`
  - text inside: `HrrE`
  ```
  000000  2c 00 00 00 48 72 72 45 06 00 00 00              ,...HrrE....
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `70` (`0x46`)
- **`l2-cache-id`**: `0` (`0x0`)
- **`name`**: `cpu4`
- **`no-aic-ipi-required`**: (present, empty)
- **`reg`**: `256` (`0x100`)
- **`reg-private`**: `0x211010000` (u64; as two u32: `0x11010000`, `0x2`)
- **`state`**: `waiting`
