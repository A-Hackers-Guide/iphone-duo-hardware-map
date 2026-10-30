# `AFKTightbeamEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b945908`; metaclass vtable `0xfffffe00080a2528`; class vtable `0xfffffe00080a1f58`
- Registration (init): `0xfffffe0008cba994`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleAOP2KextTightbeamEndpoint`](AppleAOP2KextTightbeamEndpoint.md) — `com.apple.driver.AppleAOP2`
- [`RTKitNetKernelPacketCapture`](RTKitNetKernelPacketCapture.md) — `com.apple.iokit.RTKitNet`

## IOKit personalities that instantiate it (3)

- `AFKTightbeamEndpoint` in [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md): `IOProviderClass` = `AFKEndpointInterface`, `IOPropertyMatch` = `{'KEXTTBSupport': True}`
- `RTKitPCIeTBClient0` in [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md): `IOProviderClass` = `AFKEndpointInterface`, `IONameMatch` = `com.apple.aop2.afksmplkext-0-com.apple.aop2.afksmplkext-0.ap.client-fwd`
- `RTKitPCIeTBClient1` in [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md): `IOProviderClass` = `AFKEndpointInterface`, `IONameMatch` = `com.apple.aop2.afksmplkext-1-com.apple.aop2.afksmplkext-1.ap.client-fwd`

## Strings in its kext that name it (3)

- `site.AFKTightbeamEndpoint`
- `AFKTightbeamEndpoint`
- `AFKTightbeamEndpoint.cpp`
