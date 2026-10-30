# `/arm-io/apcie/pci-bridge1`

- Name: `pci-bridge1`
- Parent: [`/arm-io/apcie`](root__arm-io__apcie.md)
- phandle: `419`
- compatible: `apcie-bridge`
- Children (1): [`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `APCIECoreRCGen5p1HostBridge` | `IOPCIDevice` | [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md) | `apcie-bridge` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `perst` | [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md) | `GPIO` | `0x40 0x0` |
| `dart_force_active` | [`/arm-io/dart-apcie1`](root__arm-io__dart-apcie1.md) | `Fact` | `` |
| `dart_request_sid` | [`/arm-io/dart-apcie1`](root__arm-io__dart-apcie1.md) | `SReq` | `` |
| `dart_release_sid` | [`/arm-io/dart-apcie1`](root__arm-io__dart-apcie1.md) | `SRel` | `` |
| `dart_self` | [`/arm-io/dart-apcie1`](root__arm-io__dart-apcie1.md) | `Self` | `` |

## All properties (29) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#msi-vectors`**: `32` (`0x20`)
- **`#size-cells`**: `0` (`0x0`)
- **`AAPL,phandle`**: `419` (`0x1a3`) → phandle of [`/arm-io/apcie/pci-bridge1`](root__arm-io__apcie__pci-bridge1.md)
- **`AAPL,unit-string`**: `00010000`
- **`apcie-piodma`**: `433` (`0x1b1`)
- **`apcie-piodma-sid`**: `17` (`0x11`)
- **`apcie-plce`**: `434` (`0x1b2`)
- **`apcie-plce-sid`**: `19` (`0x13`)
- **`apcie-port`**: `1` (`0x1`)
- **`built-in`**: (present, empty)
- **`compatible`**: `apcie-bridge`
- **`corr-err-period-us`**: `0` (`0x0`)
- **`default-apcie-options`**: `1928593408` (`0x72f40000`)
- **`enable-ptm`**: `1` (`0x1`)
- **`function-dart_force_active`**: `0x46616374000001ad` (u64; as two u32: `0x1ad`, `0x46616374`)
- **`function-dart_release_sid`**: `0x5352656c000001ad` (u64; as two u32: `0x1ad`, `0x5352656c`)
- **`function-dart_request_sid`**: `0x53526571000001ad` (u64; as two u32: `0x1ad`, `0x53526571`)
- **`function-dart_self`**: `0x53656c66000001ad` (u64; as two u32: `0x1ad`, `0x53656c66`)
- **`function-perst`**: `r`, `OIPG@`
- **`manual-enable`**: (present, empty)
- **`manual-enable-defer-scan`**: (present, empty)
- **`manual-enable-s2r`**: (present, empty)
- **`msi-vector-base`**: `32` (`0x20`)
- **`name`**: `pci-bridge1`
- **`pci-l1ss-enable`**: `1079312399` (`0x4055000f`)
- **`pci-max-payload-size`**: `1` (`0x1`)
- **`perst-to-config`**: `1` (`0x1`)
- **`t-refclk-to-perst`**: `100` (`0x64`)
