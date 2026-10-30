# `IOCommandGate`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: `com.apple.kernel` (kernel core)
- Object size: `0x50` (80 bytes)
- Metaclass: `0xfffffe000b835588`; metaclass vtable `0xfffffe0007f0a9e0`; class vtable `0xfffffe0007f0a8a8`
- Registration (init): `0xfffffe000b3b96e0`
- Superclasses: [`IOEventSource`](IOEventSource.md)

## Direct subclasses (6; 6 in total)

- [`AHTHSWorkLoop`](AHTHSWorkLoop.md) — `com.apple.driver.AppleHIDTransportSPI`
- [`AppleHPMCommandGate`](AppleHPMCommandGate.md) — `com.apple.driver.AppleHPM`
- [`IOAVCommandGate`](IOAVCommandGate.md) — `com.apple.iokit.IOAVFamily`
- [`IOSCSICommandGate`](IOSCSICommandGate.md) — `com.apple.iokit.IOSCSIArchitectureModelFamily`
- [`IOThunderboltCommandGate`](IOThunderboltCommandGate.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOUSBArbitratorCommandGate`](IOUSBArbitratorCommandGate.md) — `com.apple.driver.AppleEmbeddedUSB`
