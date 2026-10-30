# `IOInterruptController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: `com.apple.kernel` (kernel core)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b835bf0`; metaclass vtable `0xfffffe0007f13498`; class vtable `0xfffffe0007f14228`
- Registration (init): `0xfffffe000b3f7290`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (11; 19 in total)

- [`AppleARMSPMIController`](AppleARMSPMIController.md) — `com.apple.driver.AppleARMPlatform`
- [`AppleDialogPMU`](AppleDialogPMU.md) — `com.apple.driver.AppleDialogPMU`
- [`AppleEmbeddedPCIEPort`](AppleEmbeddedPCIEPort.md) — `com.apple.driver.AppleEmbeddedPCIE`
- [`AppleGPIOICController`](AppleGPIOICController.md) — `com.apple.driver.AppleGPIOICController`
- [`AppleInterruptControllerV3`](AppleInterruptControllerV3.md) — `com.apple.driver.AppleInterruptControllerV3`
- [`ApplePTD`](ApplePTD.md) — `com.apple.driver.ApplePTD`
- [`AppleSMCPMU`](AppleSMCPMU.md) — `com.apple.driver.AppleSMC`
- [`IOCPUInterruptController`](IOCPUInterruptController.md) — `com.apple.kernel`
- [`IOPCIMessagedInterruptController`](IOPCIMessagedInterruptController.md) — `com.apple.iokit.IOPCIFamily`
- [`IOSharedInterruptController`](IOSharedInterruptController.md) — `com.apple.kernel`
- [`PassthruInterruptController`](PassthruInterruptController.md) — `com.apple.kernel`
