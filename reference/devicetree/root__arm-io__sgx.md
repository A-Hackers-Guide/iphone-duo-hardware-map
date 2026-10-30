# `/arm-io/sgx`

- Name: `sgx`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `344`
- compatible: `gpu,t8160`
- device_type: `sgx`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AGXAcceleratorG19P` | `AppleARMIODevice` | [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md) | `gpu,t8160` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa8000000` | `0x4000000` (67,108,864 B) | `0x2a8000000`–`0x2abffffff` |
| 1 | `0xa8d00000` | `0x180000` (1,572,864 B) | `0x2a8d00000`–`0x2a8e7ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1226, 1227, 1228, 1229, 1260, 1262, 1241, 1243`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `mcc_dataset` | [`/arm-io/mcc`](root__arm-io__mcc.md) | `M$DS` | `` |

## All properties (26) [DT]

- **`AAPL,phandle`**: `344` (`0x158`) → phandle of [`/arm-io/sgx`](root__arm-io__sgx.md)
- **`agx-address-space-mgmt-mode`**: `1` (`0x1`)
- **`clock-gates`**: `3` (`0x3`)
- **`clock-ids`**: `342` (`0x156`)
- **`compatible`**: `gpu,t8160`
- **`device_type`**: `sgx`
- **`function-mcc_dataset`**: `0x4d24445300000036` (u64; as two u32: `0x36`, `0x4d244453`)
- **`gfx-qos`**: `0x100000001` (u64; as two u32: `0x1`, `0x1`)
- **`gpu-device-max-power`**: `5160` (`0x1428`)
- **`gpu-num-perf-states`**: `2` (`0x2`)
- **`gpu-power-sample-period`**: `8` (`0x8`)
- **`gpu-pwr-sample-period-aic-clks`**: `200000` (`0x30d40`)
- **`has-kf`**: `1` (`0x1`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 32 bytes
  - u32: `0x4ca 0x4cb 0x4cc 0x4cd 0x4ec 0x4ee 0x4d9 0x4db`
  ```
  000000  ca 04 00 00 cb 04 00 00 cc 04 00 00 cd 04 00 00  ................
  000010  ec 04 00 00 ee 04 00 00 d9 04 00 00 db 04 00 00  ................
  ```
- **`interrupts-valid`**: `223` (`0xdf`)
- **`meta-sw-interrupt`**: 20 bytes
  - u32: `0x81014048 0x2 0x81014248 0x2 0x4000`
  ```
  000000  48 40 01 81 02 00 00 00 48 42 01 81 02 00 00 00  H@......HB......
  000010  00 40 00 00                                      .@..
  ```
- **`metal-standard`**: `256` (`0x100`)
- **`name`**: `sgx`
- **`opengl-standard`**: `768` (`0x300`)
- **`perf-state-count`**: `0` (`0x0`)
- **`perf-states`**: 128 bytes
  - u32: `0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000040  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000050  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000060  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000070  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ```
- **`power-gates`**: `3` (`0x3`)
- **`procedural-antialiasing`**: (present, empty)
- **`reg`**: 32 bytes
  - u32: `0xa8000000 0x0 0x4000000 0x0 0xa8d00000 0x0 0x180000 0x0`
  ```
  000000  00 00 00 a8 00 00 00 00 00 00 00 04 00 00 00 00  ................
  000010  00 00 d0 a8 00 00 00 00 00 00 18 00 00 00 00 00  ................
  ```
- **`service-gates`**: `3` (`0x3`)
