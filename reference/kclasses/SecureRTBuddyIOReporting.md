# `SecureRTBuddyIOReporting`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md)
- Object size: `0x140` (320 bytes)
- Metaclass: `0xfffffe000ba39998`; metaclass vtable `0xfffffe00084a3098`; class vtable `0xfffffe00084a2b40`
- Registration (init): `0xfffffe000a995f7c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `SecureRTBuddyIOReporting` in [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md): `IOProviderClass` = `IOService`, `IONameMatch` = `iop,secure-rtbuddy-ioreporting`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (3) [DT]

- [`/arm-io/aop-exclave-ioreporting`](../devicetree/root__arm-io__aop-exclave-ioreporting.md) on `iop,secure-rtbuddy-ioreporting`
- [`/arm-io/dcp-exclave-ioreporting`](../devicetree/root__arm-io__dcp-exclave-ioreporting.md) on `iop,secure-rtbuddy-ioreporting`
- [`/arm-io/dcpsec-exclave-ioreporting`](../devicetree/root__arm-io__dcpsec-exclave-ioreporting.md) on `iop,secure-rtbuddy-ioreporting`

## Strings in its kext that name it (4)

- `SecureRTBuddyIOReporting`
- `SecureRTBuddyIOReporting.cpp`
- `SecureRTBuddyIOReporting(%s)`
- `site.SecureRTBuddyIOReporting`
