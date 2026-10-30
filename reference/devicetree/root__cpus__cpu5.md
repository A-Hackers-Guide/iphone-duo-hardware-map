# `/cpus/cpu5`

- Name: `cpu5`
- Parent: [`/cpus`](root__cpus.md)
- phandle: `37`
- compatible: `apple,everest`, `ARM,v8`
- device_type: `cpu`
- Children (2): [`/cpus/cpu5/:borneo_h19a_4`](root__cpus__cpu5___borneo_h19a_4.md), [`/cpus/cpu5/:borneo_h19p_4`](root__cpus__cpu5___borneo_h19p_4.md)

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x101` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`73`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `error_handler` | [`/arm-io`](root__arm-io.md) | `ErrH` | `0x7` |
| `enable_core` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `Core` | `0x80` |
| `cpu_idle` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `cpuI` | `` |

## Referenced by (11) [DT]

- [`/arm-io/dart-sep`](root__arm-io__dart-sep.md): `dart-options`
- [`/arm-io/dart-sio`](root__arm-io__dart-sio.md): `dart-options`
- [`/arm-io/dart-disp0-isoc`](root__arm-io__dart-disp0-isoc.md): `dart-options`
- [`/arm-io/dart-dispext0-isoc`](root__arm-io__dart-dispext0-isoc.md): `dart-options`
- [`/arm-io/dart-scaler`](root__arm-io__dart-scaler.md): `dart-options`
- [`/arm-io/dart-jpeg`](root__arm-io__dart-jpeg.md): `dart-options`
- [`/arm-io/dart-isp`](root__arm-io__dart-isp.md): `dart-options`
- [`/arm-io/dart-ave`](root__arm-io__dart-ave.md): `dart-options`
- [`/arm-io/dart-avd`](root__arm-io__dart-avd.md): `dart-options`
- [`/arm-io/dart-ane0`](root__arm-io__dart-ane0.md): `dart-options`
- [`/arm-io/dart-ane1`](root__arm-io__dart-ane1.md): `dart-options`

## All properties (22) [DT]

- **`AAPL,phandle`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`acc-impl-reg`**: 16 bytes
  - u32: `0x11f00000 0x2 0x40088 0x0`
  ```
  000000  00 00 f0 11 02 00 00 00 88 00 04 00 00 00 00 00  ................
  ```
- **`cluster-id`**: `1` (`0x1`)
- **`cluster-type`**: `P`
- **`compatible`**: `apple,everest`, `ARM,v8`
- **`coresight-reg`**: 16 bytes
  - u32: `0x11110000 0x2 0x300c8 0x0`
  ```
  000000  00 00 11 11 02 00 00 00 c8 00 03 00 00 00 00 00  ................
  ```
- **`cpm-impl-reg`**: 16 bytes
  - u32: `0x11e40000 0x2 0xc028 0x0`
  ```
  000000  00 00 e4 11 02 00 00 00 28 c0 00 00 00 00 00 00  ........(.......
  ```
- **`cpu-id`**: `5` (`0x5`)
- **`cpu-impl-reg`**: 16 bytes
  - u32: `0x11150000 0x2 0x9010 0x0`
  ```
  000000  00 00 15 11 02 00 00 00 10 90 00 00 00 00 00 00  ................
  ```
- **`cpu-uttdbg-reg`**: 16 bytes
  - u32: `0x11140000 0x2 0xc8 0x0`
  ```
  000000  00 00 14 11 02 00 00 00 c8 00 00 00 00 00 00 00  ................
  ```
- **`device_type`**: `cpu`
- **`function-cpu_idle`**: `0x6370754900000030` (u64; as two u32: `0x30`, `0x63707549`)
- **`function-enable_core`**: 12 bytes
  - u32: `0x30 0x436f7265 0x80`
  - text inside: `eroC`
  ```
  000000  30 00 00 00 65 72 6f 43 80 00 00 00              0...eroC....
  ```
- **`function-error_handler`**: 12 bytes
  - u32: `0x2c 0x45727248 0x7`
  - text inside: `HrrE`
  ```
  000000  2c 00 00 00 48 72 72 45 07 00 00 00              ,...HrrE....
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `73` (`0x49`)
- **`l2-cache-id`**: `0` (`0x0`)
- **`name`**: `cpu5`
- **`no-aic-ipi-required`**: (present, empty)
- **`reg`**: `257` (`0x101`)
- **`reg-private`**: `0x211110000` (u64; as two u32: `0x11110000`, `0x2`)
- **`state`**: `waiting`
