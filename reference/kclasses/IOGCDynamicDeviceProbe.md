# `IOGCDynamicDeviceProbe`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGameControllerFamily`](../kexts/com.apple.iokit.IOGameControllerFamily.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b9f4d68`; metaclass vtable `0xfffffe000837fc00`; class vtable `0xfffffe000837f698`
- Registration (init): `0xfffffe000a148760`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `Dynamic IOHIDDevice Probe` in [`com.apple.iokit.IOGameControllerFamily`](../kexts/com.apple.iokit.IOGameControllerFamily.md): `IOProviderClass` = `IOHIDDevice`, `IOMatchCategory` = `GameController`, `IOProbeScore` = `100`

## Strings in its kext that name it (7)

- `IOGCDynamicDeviceProbe`
- `site.IOGCDynamicDeviceProbeUserClient`
- `site.IOGCDynamicDeviceProbe`
- `IOGCDynamicDeviceProbeUserClient`
- `[%#010llx] IOGCDynamicDeviceProbe::start(<IOService %#010llx>)`
- `[%#010llx] IOGCDynamicDeviceProbeUserClient::start(<IOService %#010llx>) for pid %i, %s`
- `IOGCDynamicDeviceProbe::probe(<IOHIDDevice %#010llx>)`
