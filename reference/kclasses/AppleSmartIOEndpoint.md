# `AppleSmartIOEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSmartIO2`](../kexts/com.apple.driver.AppleSmartIO2.md)
- Object size: `0x1840` (6,208 bytes)
- Metaclass: `0xfffffe000b9a4c48`; metaclass vtable `0xfffffe0008234960`; class vtable `0xfffffe0008234888`
- Registration (init): `0xfffffe0009762c0c`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (3; 3 in total)

- [`AppleSmartIOControl`](AppleSmartIOControl.md) — `com.apple.driver.AppleSmartIO2`
- [`AppleSmartIODMA`](AppleSmartIODMA.md) — `com.apple.driver.AppleSmartIO2`
- [`AppleSmartIOPerf`](AppleSmartIOPerf.md) — `com.apple.driver.AppleSmartIO2`

## Strings in its kext that name it (16)

- `virtual IOReturn AppleSmartIOEndpoint::sendMessage(void *, void *, bool)`
- `bool AppleSmartIOEndpoint::initWithOptions(AppleSmartIO *, OSObject *, UInt32)`
- `virtual void AppleSmartIOEndpoint::ep_disable()`
- `AppleSmartIOEndpoint`
- `IOCommandGate *AppleSmartIOEndpoint::getCommandGate()`
- `virtual AppleSmartIOEndpoint *AppleSmartIO::endpointForHandle(OSObject *, IOSlaveEndpoint::Action, UInt32, IODMAEventSource *)`
- `virtual void AppleSmartIOEndpoint::ep_enable()`
- `IOReturn AppleSmartIOEndpoint::getParam(SmartIOParameter, UInt32 *)`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOEndpoint.cpp`
- `IOWorkLoop *AppleSmartIOEndpoint::getWorkLoop()`
- `virtual bool AppleSmartIOEndpoint::allocateCommandPool(IOWorkLoop *, unsigned int)`
- `AppleSmartIOEndpoint.cpp`
- `IOReturn AppleSmartIOEndpoint::setParam(SmartIOParameter, UInt32)`
- `site.AppleSmartIOEndpoint`
- `virtual IOReturn AppleSmartIOEndpoint::synchronousMessage(AppleSmartIOCommand *, void *)`
- `IOReturn AppleSmartIOEndpoint::send_command(UInt8)`
