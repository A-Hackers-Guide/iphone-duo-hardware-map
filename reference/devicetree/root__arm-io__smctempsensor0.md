# `/arm-io/smctempsensor0`

- Name: `smctempsensor0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `435`
- compatible: `smc-tempsensor`
- device_type: `smctempsensor`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSMCSensorDispatcher` | `AppleARMIODevice` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | `smc-tempsensor` |

## All properties (6) [DT]

- **`AAPL,phandle`**: `435` (`0x1b3`) → phandle of [`/arm-io/smctempsensor0`](root__arm-io__smctempsensor0.md)
- **`compatible`**: `smc-tempsensor`
- **`device_type`**: `smctempsensor`
- **`name`**: `smctempsensor0`
- **`sensor`**: 12 bytes
  - u32: `0x4c50546d 0x4c4c546d 0x5754456d`
  - text inside: `mTPLmTLLmETW`
  ```
  000000  6d 54 50 4c 6d 54 4c 4c 6d 45 54 57              mTPLmTLLmETW
  ```
- **`timerInterval`**: `1000` (`0x3e8`)
