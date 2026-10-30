# `AppleSEPHDCPManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPHDCPManager`](../kexts/com.apple.driver.AppleSEPHDCPManager.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b9997d8`; metaclass vtable `0xfffffe00081e9dc0`; class vtable `0xfffffe00081e9860`
- Registration (init): `0xfffffe00095da914`
- Superclasses: [`AppleHDCPManager`](AppleHDCPManager.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSEPHDCPManager` in [`com.apple.driver.AppleSEPHDCPManager`](../kexts/com.apple.driver.AppleSEPHDCPManager.md): `IOProviderClass` = `AppleSEPDeviceService`, `IONameMatch` = `sep-endpoint,hdcp`

## Strings in its kext that name it (6)

- `site.AppleSEPHDCPManager`
- `AppleSEPHDCPManager failed in super::start`
- `AppleSEPHDCPManager`
- `AppleSEPHDCPManager failed to get provider`
- `AppleSEPHDCPManager failed in super::start`
- `AppleSEPHDCPManager failed to get provider`
