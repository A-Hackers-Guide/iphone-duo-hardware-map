# `AppleS8000DWI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleS8000DWI`](../kexts/com.apple.driver.AppleS8000DWI.md)
- Object size: `0x140` (320 bytes)
- Metaclass: `0xfffffe000b994308`; metaclass vtable `0xfffffe00081c70c8`; class vtable `0xfffffe00081c6b70`
- Registration (init): `0xfffffe0009486ad4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleS8000DWI` in [`com.apple.driver.AppleS8000DWI`](../kexts/com.apple.driver.AppleS8000DWI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `dwi,s8000`

## Strings in its kext that name it (9)

- `AppleS8000DWI`
- `AppleS8000DWI.cpp`
- `AppleS8000DWIBacklightFunction`
- `site.AppleS8000DWIVoltageFunction`
- `site.AppleS8000DWIBacklightFunction`
- `site.AppleS8000DWI`
- `AppleS8000DWI::%s v%u _dwiBaseAddress: %#lx, buck mask = 0x%08x\n`
- `\"AppleS8000DWI::sendWLED: version: %x is unsupported\\n\" @%s:%d`
- `AppleS8000DWIVoltageFunction`
