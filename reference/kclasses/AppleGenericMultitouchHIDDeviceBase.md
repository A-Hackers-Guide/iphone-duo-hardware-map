# `AppleGenericMultitouchHIDDeviceBase`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md)
- Object size: `0xe0` (224 bytes)
- Metaclass: `0xfffffe000b9467d0`; metaclass vtable `0xfffffe00080b9668`; class vtable `0xfffffe00080b8fc8`
- Registration (init): `0xfffffe0008d14670`
- Superclasses: [`IOHIDDevice`](IOHIDDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleGenericMultitouchHIDSPI`](AppleGenericMultitouchHIDSPI.md) — `com.apple.driver.AppleGenericMultitouch`

## Strings in its kext that name it (10)

- `virtual bool AppleGenericMultitouchHIDDeviceBase::handleStart(IOService *)`
- `void AppleGenericMultitouchHIDDeviceBase::setExtraProperties()`
- `static OSSharedPtr<OSString> AppleGenericMultitouchHIDDeviceBase::copyPersonality(IOService *)`
- `/Library/Caches/com.apple.xbs/18870140-AD72-47E9-90F7-D7C84661AAD4/TemporaryDirectory.zANmYd/Sources/AppleGenericMultitouch/Kext/hiddevice/AppleGenericMultitouchHIDDeviceBase.cpp`
- `site.AppleGenericMultitouchHIDDeviceBase`
- `virtual void AppleGenericMultitouchHIDDeviceBase::inputReport(uint8_t, const void *, size_t)`
- `virtual bool AppleGenericMultitouchHIDDeviceBase::init(OSDictionary *)`
- `virtual IOReturn AppleGenericMultitouchHIDDeviceBase::getReport(IOMemoryDescriptor *, IOHIDReportType, IOOptionBits)`
- `AppleGenericMultitouchHIDDeviceBase`
- `virtual IOReturn AppleGenericMultitouchHIDDeviceBase::newReportDescriptor(IOMemoryDescriptor **) const`
