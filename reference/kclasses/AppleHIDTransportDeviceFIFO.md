# `AppleHIDTransportDeviceFIFO`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHIDTransportFIFO`](../kexts/com.apple.driver.AppleHIDTransportFIFO.md)
- Object size: `0x158` (344 bytes)
- Metaclass: `0xfffffe000b94de40`; metaclass vtable `0xfffffe00080e9dd8`; class vtable `0xfffffe00080e95f0`
- Registration (init): `0xfffffe0008ef9310`
- Superclasses: [`AppleHIDTransportDevice`](AppleHIDTransportDevice.md) → [`AIDService`](AIDService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHIDTransportDeviceFIFO` in [`com.apple.driver.AppleHIDTransportFIFO`](../kexts/com.apple.driver.AppleHIDTransportFIFO.md): `IOProviderClass` = `AppleDockChannelDevice`, `IONameMatch` = `['hid-transport,dc']`

## Strings in its kext that name it (3)

- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/FIFO/AppleHIDTransportDeviceFIFO.cpp`
- `AppleHIDTransportDeviceFIFO`
- `site.AppleHIDTransportDeviceFIFO`
