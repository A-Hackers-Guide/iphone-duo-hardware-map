# `/cpus/cpu1`

- Name: `cpu1`
- Parent: [`/cpus`](root__cpus.md)
- phandle: `25`
- compatible: `apple,sawtooth`, `ARM,v8`
- device_type: `cpu`
- Children (2): [`/cpus/cpu1/:borneo_h19a_3`](root__cpus__cpu1___borneo_h19a_3.md), [`/cpus/cpu1/:borneo_h19p_3`](root__cpus__cpu1___borneo_h19p_3.md)

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x1` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`53`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `error_handler` | [`/arm-io`](root__arm-io.md) | `ErrH` | `0x1` |
| `enable_core` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `Core` | `0x2` |
| `cpu_idle` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `cpuI` | `` |

## All properties (22) [DT]

- **`AAPL,phandle`**: `25` (`0x19`) → phandle of [`/cpus/cpu1`](root__cpus__cpu1.md)
- **`acc-impl-reg`**: 16 bytes
  - u32: `0x10f00000 0x2 0x40088 0x0`
  ```
  000000  00 00 f0 10 02 00 00 00 88 00 04 00 00 00 00 00  ................
  ```
- **`cluster-id`**: `0` (`0x0`)
- **`cluster-type`**: `E`
- **`compatible`**: `apple,sawtooth`, `ARM,v8`
- **`coresight-reg`**: 16 bytes
  - u32: `0x10110000 0x2 0x300c8 0x0`
  ```
  000000  00 00 11 10 02 00 00 00 c8 00 03 00 00 00 00 00  ................
  ```
- **`cpm-impl-reg`**: 16 bytes
  - u32: `0x10e40000 0x2 0xc028 0x0`
  ```
  000000  00 00 e4 10 02 00 00 00 28 c0 00 00 00 00 00 00  ........(.......
  ```
- **`cpu-id`**: `1` (`0x1`)
- **`cpu-impl-reg`**: 16 bytes
  - u32: `0x10150000 0x2 0x9010 0x0`
  ```
  000000  00 00 15 10 02 00 00 00 10 90 00 00 00 00 00 00  ................
  ```
- **`cpu-uttdbg-reg`**: 16 bytes
  - u32: `0x10140000 0x2 0xc8 0x0`
  ```
  000000  00 00 14 10 02 00 00 00 c8 00 00 00 00 00 00 00  ................
  ```
- **`device_type`**: `cpu`
- **`function-cpu_idle`**: `0x6370754900000030` (u64; as two u32: `0x30`, `0x63707549`)
- **`function-enable_core`**: 12 bytes
  - u32: `0x30 0x436f7265 0x2`
  - text inside: `eroC`
  ```
  000000  30 00 00 00 65 72 6f 43 02 00 00 00              0...eroC....
  ```
- **`function-error_handler`**: 12 bytes
  - u32: `0x2c 0x45727248 0x1`
  - text inside: `HrrE`
  ```
  000000  2c 00 00 00 48 72 72 45 01 00 00 00              ,...HrrE....
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `53` (`0x35`)
- **`l2-cache-id`**: `0` (`0x0`)
- **`name`**: `cpu1`
- **`no-aic-ipi-required`**: (present, empty)
- **`reg`**: `1` (`0x1`)
- **`reg-private`**: `0x210110000` (u64; as two u32: `0x10110000`, `0x2`)
- **`state`**: `waiting`
