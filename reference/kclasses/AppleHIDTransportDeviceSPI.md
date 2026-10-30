# `AppleHIDTransportDeviceSPI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHIDTransportSPI`](../kexts/com.apple.driver.AppleHIDTransportSPI.md)
- Object size: `0x2a0` (672 bytes)
- Metaclass: `0xfffffe000b94e260`; metaclass vtable `0xfffffe00080effd8`; class vtable `0xfffffe00080ef780`
- Registration (init): `0xfffffe0008f4b998`
- Superclasses: [`AppleHIDTransportDevice`](AppleHIDTransportDevice.md) → [`AIDService`](AIDService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHIDTransportDeviceSPI` in [`com.apple.driver.AppleHIDTransportSPI`](../kexts/com.apple.driver.AppleHIDTransportSPI.md): `IOProviderClass` = `AppleARMSPIDevice`, `IONameMatch` = `['hid-transport,k1', 'hid-transport,spi']`

## Strings in its kext that name it (3)

- `site.AppleHIDTransportDeviceSPI`
- `AppleHIDTransportDeviceSPI`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/SPI/AppleHIDTransportDeviceSPI.cpp`
