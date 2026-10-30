# `AppleHIDTransportDeviceMailbox`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHIDTransportMailbox`](../kexts/com.apple.driver.AppleHIDTransportMailbox.md)
- Object size: `0x178` (376 bytes)
- Metaclass: `0xfffffe000b94df70`; metaclass vtable `0xfffffe00080eb4a8`; class vtable `0xfffffe00080eac98`
- Registration (init): `0xfffffe0008f0d548`
- Superclasses: [`AppleHIDTransportDevice`](AppleHIDTransportDevice.md) → [`AIDService`](AIDService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleHIDTransportDeviceMailbox (MTP)` in [`com.apple.driver.AppleHIDTransportMailbox`](../kexts/com.apple.driver.AppleHIDTransportMailbox.md): `IOProviderClass` = `RTBuddyEndpointService`, `IONameMatch` = `['MTPEndpoint1']`
- `AppleHIDTransportDeviceMailbox (RTP)` in [`com.apple.driver.AppleHIDTransportMailbox`](../kexts/com.apple.driver.AppleHIDTransportMailbox.md): `IOProviderClass` = `RTBuddyEndpointService`, `IONameMatch` = `['RTPEndpoint1']`

## Strings in its kext that name it (3)

- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/Mailbox/AppleHIDTransportDeviceMailbox.cpp`
- `site.AppleHIDTransportDeviceMailbox`
- `AppleHIDTransportDeviceMailbox`
