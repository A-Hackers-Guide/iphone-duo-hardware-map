# `AppleARMLightEmUp`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b934920`; metaclass vtable `0xfffffe0007fc43d0`; class vtable `0xfffffe0007fc3e78`
- Registration (init): `0xfffffe0008724458`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMLightEmUp` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `IOService`, `IONameMatch` = `cpu-debug-interface`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/cpu-debug-interface`](../devicetree/root__arm-io__cpu-debug-interface.md) on `cpu-debug-interface`

## Strings in its kext that name it (9)

- `virtual void AppleARMLightEmUp::stop(IOService *)`
- `void AppleARMLightEmUp::ignite() const`
- `static unsigned int AppleARMLightEmUp::CPUHalter::Expression::init(Expression &, const OSData *, unsigned int)`
- `AppleARMLightEmUpIgnite`
- `site.AppleARMLightEmUp`
- `virtual bool AppleARMLightEmUp::start(IOService *)`
- `void AppleARMLightEmUp::halt(unsigned int) const`
- `AppleARMLightEmUp.cpp`
- `AppleARMLightEmUp`
