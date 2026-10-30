# `AppleUSBAudioComposite`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBAudio`](../kexts/com.apple.driver.AppleUSBAudio.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b9d4210`; metaclass vtable `0xfffffe000829b930`; class vtable `0xfffffe000829b3c8`
- Registration (init): `0xfffffe0009ac5f80`
- Superclasses: [`AppleUSBHostCompositeDevice`](AppleUSBHostCompositeDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleUSBAudioComposite` in [`com.apple.driver.AppleUSBAudio`](../kexts/com.apple.driver.AppleUSBAudio.md): `IOProviderClass` = `IOUSBHostDevice`
- `InterfaceAssociationClass` in [`com.apple.driver.AppleUSBAudio`](../kexts/com.apple.driver.AppleUSBAudio.md): `IOProviderClass` = `IOUSBHostDevice`

## Strings in its kext that name it (2)

- `site.AppleUSBAudioComposite`
- `AppleUSBAudioComposite`
