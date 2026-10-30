# `/arm-io/apcie/pci-bridge0`

- Name: `pci-bridge0`
- Parent: [`/arm-io/apcie`](root__arm-io__apcie.md)
- phandle: `415`
- compatible: `apcie-bridge`
- Children (3): [`/arm-io/apcie/pci-bridge0/centauri-control`](root__arm-io__apcie__pci-bridge0__centauri-control.md), [`/arm-io/apcie/pci-bridge0/centauri-alpha`](root__arm-io__apcie__pci-bridge0__centauri-alpha.md), [`/arm-io/apcie/pci-bridge0/centauri-beta`](root__arm-io__apcie__pci-bridge0__centauri-beta.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `APCIECoreRCGen5p1HostBridge` | `IOPCIDevice` | [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md) | `apcie-bridge` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `dart_force_active` | [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md) | `Fact` | `` |
| `dart_self` | [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md) | `Self` | `` |
| `dart_release_sid` | [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md) | `SRel` | `` |
| `warm_reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW4` | `0x62706c69 0x1000000` |
| `reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x800000 0x80000` |
| `pcie_port_control` | [`/arm-io/apcie`](root__arm-io__apcie.md) | `PrtC` | `0x19f` |
| `dart_request_sid` | [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md) | `SReq` | `` |
| `perst` | [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md) | `GPIO` | `0x42 0x0` |

## All properties (37) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#msi-vectors`**: `32` (`0x20`)
- **`#size-cells`**: `0` (`0x0`)
- **`AAPL,phandle`**: `415` (`0x19f`) → phandle of [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md)
- **`AAPL,unit-string`**: `00000000`
- **`apcie-piodma`**: `427` (`0x1ab`)
- **`apcie-piodma-sid`**: `17` (`0x11`)
- **`apcie-plce`**: `428` (`0x1ac`)
- **`apcie-plce-sid`**: `19` (`0x13`)
- **`apcie-port`**: `0` (`0x0`)
- **`built-in`**: (present, empty)
- **`centauri-builtin`**: (present, empty)
- **`compatible`**: `apcie-bridge`
- **`corr-err-period-us`**: `0` (`0x0`)
- **`default-apcie-options`**: `1928593408` (`0x72f40000`)
- **`enable-ptm`**: (present, empty)
- **`function-dart_force_active`**: `0x46616374000001a5` (u64; as two u32: `0x1a5`, `0x46616374`)
- **`function-dart_release_sid`**: `0x5352656c000001a5` (u64; as two u32: `0x1a5`, `0x5352656c`)
- **`function-dart_request_sid`**: `0x53526571000001a5` (u64; as two u32: `0x1a5`, `0x53526571`)
- **`function-dart_self`**: `0x53656c66000001a5` (u64; as two u32: `0x1a5`, `0x53656c66`)
- **`function-pcie_port_control`**: 12 bytes
  - u32: `0x19e 0x50727443 0x19f`
  - text inside: `CtrP`
  ```
  000000  9e 01 00 00 43 74 72 50 9f 01 00 00              ....CtrP....
  ```
- **`function-perst`**: `r`, `OIPGB`
- **`function-reset`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x7063494f 0x800000 0x80000`
  - text inside: `8WKpOIcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 4f 49 63 70 00 00 80 00  ....8WKpOIcp....
  000010  00 00 08 00                                      ....
  ```
- **`function-warm_reset`**: 16 bytes
  - u32: `0x9f 0x704b5734 0x62706c69 0x1000000`
  - text inside: `4WKpilpb`
  ```
  000000  9f 00 00 00 34 57 4b 70 69 6c 70 62 00 00 00 01  ....4WKpilpb....
  ```
- **`ignore-link-speed-mismatch`**: `1` (`0x1`)
- **`keep-root-port-on`**: (present, empty)
- **`manual-enable`**: (present, empty)
- **`manual-enable-defer-scan`**: (present, empty)
- **`maximum-link-speed`**: `3` (`0x3`)
- **`msi-vector-base`**: `0` (`0x0`)
- **`name`**: `pci-bridge0`
- **`pci-aspm-default`**: `2` (`0x2`)
- **`pci-l1ss-enable`**: `1079312399` (`0x4055000f`)
- **`pci-max-latency`**: `268963848` (`0x10081008`)
- **`perst-to-config`**: `1` (`0x1`)
- **`t-refclk-to-perst`**: `100` (`0x64`)
- **`terminate-missing-endpoint`**: (present, empty)
