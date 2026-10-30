# `IOWorkLoop`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: `com.apple.kernel` (kernel core)
- Object size: `0x48` (72 bytes)
- Metaclass: `0xfffffe000b835560`; metaclass vtable `0xfffffe0007f0a6e8`; class vtable `0xfffffe0007f0a5b8`
- Registration (init): `0xfffffe000b3b6110`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (6; 6 in total)

- [`ANEWorkLoop`](ANEWorkLoop.md) — `com.apple.driver.AppleH16ANEInterface`
- [`AppleCLPCWorkLoop`](AppleCLPCWorkLoop.md) — `com.apple.driver.AppleT8160CLPC`
- [`AppleCameraWorkLoop`](AppleCameraWorkLoop.md) — `com.apple.driver.AppleCamera`
- [`AppleCellularDataPlaneWorkLoop`](AppleCellularDataPlaneWorkLoop.md) — `com.apple.driver.AppleConvergedIPCBBControl`
- [`AppleNVMeWorkLoop`](AppleNVMeWorkLoop.md) — `com.apple.iokit.IONVMeFamily`
- [`IOThunderboltWorkLoop`](IOThunderboltWorkLoop.md) — `com.apple.iokit.IOThunderboltFamily`
