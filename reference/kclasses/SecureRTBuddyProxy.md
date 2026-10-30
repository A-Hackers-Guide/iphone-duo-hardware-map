# `SecureRTBuddyProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000ba39948`; metaclass vtable `0xfffffe00084a2950`; class vtable `0xfffffe00084a23f0`
- Registration (init): `0xfffffe000a993854`
- Superclasses: [`RTBuddyRouteProvider`](RTBuddyRouteProvider.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `SecureRTBuddyProxy` in [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md): `IOProviderClass` = `IOService`, `IONameMatch` = `iop,secure-rtbuddy-proxy`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (4) [DT]

- [`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) on `iop,secure-rtbuddy-proxy`
- [`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) on `iop,secure-rtbuddy-proxy`
- [`/arm-io/dcp-exclave-mailbox`](../devicetree/root__arm-io__dcp-exclave-mailbox.md) on `iop,secure-rtbuddy-proxy`
- [`/arm-io/dcpsec-exclave-mailbox`](../devicetree/root__arm-io__dcpsec-exclave-mailbox.md) on `iop,secure-rtbuddy-proxy`

## Strings in its kext that name it (9)

- `site.SecureRTBuddyProxyEndpoint`
- `SecureRTBuddyProxy.cpp`
- `SecureRTBuddyProxyRouteAdaptor`
- `site.SecureRTBuddyProxyRouteAdaptor`
- `SecureRTBuddyProxyEndpoint.cpp`
- `SecureRTBuddyProxy(%s)`
- `site.SecureRTBuddyProxy`
- `SecureRTBuddyProxy`
- `SecureRTBuddyProxyEndpoint`
