# `PSVR2SenseDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGameControllerFamily`](../kexts/com.apple.iokit.IOGameControllerFamily.md)
- Object size: `0x198` (408 bytes)
- Metaclass: `0xfffffe000b9f4bd8`; metaclass vtable `0xfffffe000837c228`; class vtable `0xfffffe000837bbd0`
- Registration (init): `0xfffffe000a14274c`
- Superclasses: [`IOHIDGCDevice`](IOHIDGCDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `PSVR2 Sense Left Controller Personality` in [`com.apple.iokit.IOGameControllerFamily`](../kexts/com.apple.iokit.IOGameControllerFamily.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `PSVR2 Sense Right Controller Personality` in [`com.apple.iokit.IOGameControllerFamily`](../kexts/com.apple.iokit.IOGameControllerFamily.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`

## Strings in its kext that name it (33)

- `site.PSVR2SenseDeviceFastPathUserClientInputQueue`
- `site.PSVR2SenseDeviceFastPathUserClientTrackingQueue`
- `site.PSVR2SenseDeviceHIDEventServerUserClient`
- `site.PSVR2SenseDeviceFastPathUserClientQueue`
- `PSVR2SenseDeviceFastPathUserClientQueue`
- `PSVR2SenseDeviceHIDEventServerUserClient`
- `PSVR2SenseDeviceFastPathUserClientHapticsQueue`
- `PSVR2SenseDeviceFastPathUserClientTrackingQueue`
- `site.PSVR2SenseDeviceFastPathUserClient`
- `PSVR2SenseDevice`
- `site.PSVR2SenseDevice`
- `PSVR2SenseDeviceFastPathUserClient`
- `site.PSVR2SenseDeviceFastPathUserClientHapticsQueue`
- `PSVR2SenseDeviceFastPathUserClientInputQueue`
- `[%#010llx] PSVR2SenseDevice::didTerminate(<IOHIDInterface %#010llx>)`
- `[%#010llx] PSVR2SenseDevice::handleProviderClosed(%llu)`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClient::start(<PSVR2SenseDevice %#010llx>) for pid %i, %s`
- `[%#010llx] PSVR2SenseDevice::handleStart(<IOHIDInterface %#010llx>)`
- `[%#010llx] PSVR2SenseDevice::handleProviderOpened(%llu)`
- `[%#010llx] openHapticsControl(<PSVR2SenseDevice %#010llx>) denied: %x.`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientHapticsQueue::stop(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDevice::openHapticsControl(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientInputQueue::stop(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientHapticsQueue::start(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientTrackingQueue::stop(<IOService %#010llx>)`
- `[%#010llx] openTrackingControl(<PSVR2SenseDevice %#010llx>) denied: %x.`
- `[%#010llx] PSVR2SenseDevice::openTrackingControl(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientInputQueue::start(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientTrackingQueue::start(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDevice::handleStop(<IOHIDInterface %#010llx>)`
- `[%#010llx] PSVR2SenseDevice::closeHapticsControl(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDeviceHIDEventServerUserClient::start(<PSVR2SenseDevice %#010llx>) for pid %i, %s`
- `[%#010llx] PSVR2SenseDevice::closeTrackingControl(<IOService %#010llx>)`
