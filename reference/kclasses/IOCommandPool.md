# `IOCommandPool`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: `com.apple.kernel` (kernel core)
- Object size: `0x38` (56 bytes)
- Metaclass: `0xfffffe000b8355b0`; metaclass vtable `0xfffffe0007f0abd0`; class vtable `0xfffffe0007f0ab10`
- Registration (init): `0xfffffe000b3bae64`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (12; 20 in total)

- [`AppleNVMeRequestPool`](AppleNVMeRequestPool.md) — `com.apple.iokit.IONVMeFamily`
- [`AppleOnboardSerialPool`](AppleOnboardSerialPool.md) — `com.apple.driver.AppleOnboardSerial`
- [`ApplePIODMARequestPool`](ApplePIODMARequestPool.md) — `com.apple.driver.ApplePIODMA`
- [`AppleSEPCommandPool`](AppleSEPCommandPool.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSmartIOCommandPool`](AppleSmartIOCommandPool.md) — `com.apple.driver.AppleSmartIO2`
- [`AppleUSBEthernetDeviceCommandPool`](AppleUSBEthernetDeviceCommandPool.md) — `com.apple.driver.AppleUSBEthernetDevice`
- [`AppleUSBNetworkingCommandPool`](AppleUSBNetworkingCommandPool.md) — `com.apple.driver.usb.networking`
- [`AppleUSBRequestPool`](AppleUSBRequestPool.md) — `com.apple.driver.usb.AppleUSBCommon`
- [`HSAIDReceivePacketPool`](HSAIDReceivePacketPool.md) — `com.apple.iokit.IOAccessoryManager`
- [`HSAIDTransmitCommandPool`](HSAIDTransmitCommandPool.md) — `com.apple.iokit.IOAccessoryManager`
- [`HSAIDTransmitPacketPool`](HSAIDTransmitPacketPool.md) — `com.apple.iokit.IOAccessoryManager`
- [`IOAppleConvergedIPCPool`](IOAppleConvergedIPCPool.md) — `com.apple.driver.IOACIPCFamily`
