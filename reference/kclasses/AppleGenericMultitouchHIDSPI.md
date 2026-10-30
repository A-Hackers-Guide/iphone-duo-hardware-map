# `AppleGenericMultitouchHIDSPI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000b9467a8`; metaclass vtable `0xfffffe00080b8d58`; class vtable `0xfffffe00080b86b8`
- Registration (init): `0xfffffe0008d1389c`
- Superclasses: [`AppleGenericMultitouchHIDDeviceBase`](AppleGenericMultitouchHIDDeviceBase.md) → [`IOHIDDevice`](IOHIDDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (9)

- `site.AppleGenericMultitouchHIDSPI`
- `auto AppleGenericMultitouchHIDSPI::performChallengeSequence()::(anonymous class)::operator()(bool &) const`
- `void AppleGenericMultitouchHIDSPI::logAck(const AGMFemtoHIDSPI::AckPacket &, const AGMFemtoHIDSPI::AckPacket &)`
- `void AppleGenericMultitouchHIDSPI::handleHIDRxGated(const AGMFemtoHIDSPI::HIDPacket &)`
- `void AppleGenericMultitouchHIDSPI::interrupt(IOInterruptEventSource *, int)`
- `void AppleGenericMultitouchHIDSPI::logTransfer(const AGMFemtoHIDSPI::LLPacket &, const AGMFemtoHIDSPI::LLPacket &)`
- `bool AppleGenericMultitouchHIDSPI::performChallengeSequence()`
- `AppleGenericMultitouchHIDSPI`
- `void AppleGenericMultitouchHIDSPI::handleRxGated(const AGMFemtoHIDSPI::LLPacket &)`
