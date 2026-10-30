# `AppleHIDTransportDeviceDummy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHIDTransport`](../kexts/com.apple.driver.AppleHIDTransport.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b94dc10`; metaclass vtable `0xfffffe00080e8420`; class vtable `0xfffffe00080e7c48`
- Registration (init): `0xfffffe0008ece0ac`
- Superclasses: [`AppleHIDTransportDevice`](AppleHIDTransportDevice.md) → [`AIDService`](AIDService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHIDTransportDeviceDummy` in [`com.apple.driver.AppleHIDTransport`](../kexts/com.apple.driver.AppleHIDTransport.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `['hid-transport,dummy']`

## Strings in its kext that name it (3)

- `site.AppleHIDTransportDeviceDummy`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/AppleHIDTransportDeviceDummy.cpp`
- `AppleHIDTransportDeviceDummy`
