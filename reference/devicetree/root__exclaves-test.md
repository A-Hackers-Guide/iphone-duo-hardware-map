# `/exclaves-test`

- Name: `exclaves-test`
- Parent: [`/`](root.md)
- phandle: `550`
- compatible: `exclaves-test`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleExclaveExampleKext` | `IOService` | [`com.apple.ExclaveKextClient`](../kexts/com.apple.ExclaveKextClient.md) | `exclaves-test` |
| `AppleExclaveExampleKext` | `IOService` | [`com.apple.ExclaveKextClient`](../kexts/com.apple.ExclaveKextClient.md) | `exclaves-test` |

## All properties (6) [DT]

- **`AAPL,phandle`**: `550` (`0x226`) → phandle of [`/exclaves-test`](root__exclaves-test.md)
- **`compatible`**: `exclaves-test`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.ExclaveDriverKit`
- **`exclave-service`**: `com.apple.service.HelloDrivers`
- **`name`**: `exclaves-test`
