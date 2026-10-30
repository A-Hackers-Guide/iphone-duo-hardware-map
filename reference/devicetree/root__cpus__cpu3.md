# `/cpus/cpu3`

- Name: `cpu3`
- Parent: [`/cpus`](root__cpus.md)
- phandle: `31`
- compatible: `apple,sawtooth`, `ARM,v8`
- device_type: `cpu`
- Children (2): [`/cpus/cpu3/:borneo_h19a_3`](root__cpus__cpu3___borneo_h19a_3.md), [`/cpus/cpu3/:borneo_h19p_3`](root__cpus__cpu3___borneo_h19p_3.md)

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x3` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`59`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `error_handler` | [`/arm-io`](root__arm-io.md) | `ErrH` | `0x3` |
| `enable_core` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `Core` | `0x8` |
| `cpu_idle` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `cpuI` | `` |

## All properties (22) [DT]

- **`AAPL,phandle`**: `31` (`0x1f`) → phandle of [`/cpus/cpu3`](root__cpus__cpu3.md)
- **`acc-impl-reg`**: 16 bytes
  - u32: `0x10f00000 0x2 0x40088 0x0`
  ```
  000000  00 00 f0 10 02 00 00 00 88 00 04 00 00 00 00 00  ................
  ```
- **`cluster-id`**: `0` (`0x0`)
- **`cluster-type`**: `E`
- **`compatible`**: `apple,sawtooth`, `ARM,v8`
- **`coresight-reg`**: 16 bytes
  - u32: `0x10310000 0x2 0x300c8 0x0`
  ```
  000000  00 00 31 10 02 00 00 00 c8 00 03 00 00 00 00 00  ..1.............
  ```
- **`cpm-impl-reg`**: 16 bytes
  - u32: `0x10e40000 0x2 0xc028 0x0`
  ```
  000000  00 00 e4 10 02 00 00 00 28 c0 00 00 00 00 00 00  ........(.......
  ```
- **`cpu-id`**: `3` (`0x3`)
- **`cpu-impl-reg`**: 16 bytes
  - u32: `0x10350000 0x2 0x9010 0x0`
  ```
  000000  00 00 35 10 02 00 00 00 10 90 00 00 00 00 00 00  ..5.............
  ```
- **`cpu-uttdbg-reg`**: 16 bytes
  - u32: `0x10340000 0x2 0xc8 0x0`
  ```
  000000  00 00 34 10 02 00 00 00 c8 00 00 00 00 00 00 00  ..4.............
  ```
- **`device_type`**: `cpu`
- **`function-cpu_idle`**: `0x6370754900000030` (u64; as two u32: `0x30`, `0x63707549`)
- **`function-enable_core`**: 12 bytes
  - u32: `0x30 0x436f7265 0x8`
  - text inside: `eroC`
  ```
  000000  30 00 00 00 65 72 6f 43 08 00 00 00              0...eroC....
  ```
- **`function-error_handler`**: 12 bytes
  - u32: `0x2c 0x45727248 0x3`
  - text inside: `HrrE`
  ```
  000000  2c 00 00 00 48 72 72 45 03 00 00 00              ,...HrrE....
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `59` (`0x3b`)
- **`l2-cache-id`**: `0` (`0x0`)
- **`name`**: `cpu3`
- **`no-aic-ipi-required`**: (present, empty)
- **`reg`**: `3` (`0x3`)
- **`reg-private`**: `0x210310000` (u64; as two u32: `0x10310000`, `0x2`)
- **`state`**: `waiting`
