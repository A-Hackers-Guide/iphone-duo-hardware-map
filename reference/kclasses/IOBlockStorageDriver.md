# `IOBlockStorageDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOStorageFamily`](../kexts/com.apple.iokit.IOStorageFamily.md)
- Object size: `0x158` (344 bytes)
- Metaclass: `0xfffffe000ba1ac88`; metaclass vtable `0xfffffe00083f41d8`; class vtable `0xfffffe00083f3b20`
- Registration (init): `0xfffffe000a3da9a0`
- Superclasses: [`IOStorage`](IOStorage.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOBlockStorageDriver` in [`com.apple.iokit.IOStorageFamily`](../kexts/com.apple.iokit.IOStorageFamily.md): `IOProviderClass` = `IOBlockStorageDevice`, `IOPropertyMatch` = `{'device-type': 'Generic'}`

## Strings in its kext that name it (13)

- `IOBlockStorageDriver`
- `%s[IOBlockStorageDriver]::handleStart: err '%s' from checkForMedia\n`
- `%s[IOBlockStorageDriver]::mediaStateHasChanged: err '%s' from recordMediaParameters\n`
- `%s[IOBlockStorageDriver]; executeRequest: request failed to start!\n`
- `site.IOBlockStorageDriver::Context`
- `%s[IOBlockStorageDriver]::handleStart; err '%s' from reportRemovability\n`
- `%s[IOBlockStorageDriver]::checkForMedia; err '%s' from reportMediaState\n`
- `%s[IOBlockStorageDriver]::mediaStateHasChanged; err '%s' from acceptNewMedia\n`
- `%s[IOBlockStorageDriver]::mediaStateHasChanged; err '%s' from decommissionNewMedia\n`
- `site.IOBlockStorageDriver::ExpansionData`
- `site.IOBlockStorageDriver`
- `%s[IOBlockStorageDriver]::systemWillShutdown, shutdown thread timed out\n`
- `%s[IOBlockStorageDriver]::handleStart; err '%s' from reportEjectability\n`
