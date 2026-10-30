# `AppleLockdownMode`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleLockdownMode`](../kexts/com.apple.driver.AppleLockdownMode.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000b955c00`; metaclass vtable `0xfffffe0008132a58`; class vtable `0xfffffe0008132500`
- Registration (init): `0xfffffe0009099a30`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleLockdownMode` in [`com.apple.driver.AppleLockdownMode`](../kexts/com.apple.driver.AppleLockdownMode.md): `IOProviderClass` = `IOResources`, `IOMatchCategory` = `AppleLockdownMode`

## Strings in its kext that name it (19)

- `[AppleLockdownMode - %s] setting state to off in nvram because state in ACM is also off (not rebooting)\n`
- `[AppleLockdownMode - %s] ProtectedData check failed\n`
- `[AppleLockdownMode - %s] restoreOS check failed\n`
- `[AppleLockdownMode - %s] could not get environment variable from ACM: %d\n`
- `[AppleLockdownMode - %s] ProtectedData check passed\n`
- `[AppleLockdownMode - %s] setting state to on in nvram because state in ACM is also on (not rebooting)\n`
- `[AppleLockdownMode - %s] MobileObliteration check passed\n`
- `[AppleLockdownMode - %s] restoreOS check passed\n`
- `[AppleLockdownMode - %s] SEP check passed\n`
- `AppleLockdownMode`
- `[AppleLockdownMode - %s] enforcing parity check\n`
- `site.AppleLockdownMode`
- `[AppleLockdownMode - %s] state in ACM: %d, in nvram: %d\n`
- `[AppleLockdownMode - %s] MobileObliteration check failed\n`
- `[AppleLockdownMode - %s] skipping parity check\n`
- `[AppleLockdownMode - %s] SEP check failed\n`
- `[AppleLockdownMode - %s] failed to start IOService\n`
- `[AppleLockdownMode - %s] unable to start LDMCheckParity thread: %d\n`
- `[AppleLockdownMode - %s] started\n`
