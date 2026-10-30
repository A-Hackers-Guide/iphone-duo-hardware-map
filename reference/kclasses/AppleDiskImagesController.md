# `AppleDiskImagesController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDiskImages2`](../kexts/com.apple.driver.AppleDiskImages2.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000b940fa8`; metaclass vtable `0xfffffe0008051cb0`; class vtable `0xfffffe0008051758`
- Registration (init): `0xfffffe0008b77178`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleDiskImageDevice` in [`com.apple.driver.AppleDiskImages2`](../kexts/com.apple.driver.AppleDiskImages2.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `AppleDiskImageDevice`

## Strings in its kext that name it (7)

- `virtual void AppleDiskImagesController::free()`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/AppleDiskImagesController.cpp`
- `site.AppleDiskImagesController`
- `IOReturn AppleDiskImagesController::FindExistingDevice(DICreateDeviceParams *, DICreateDeviceReply *)`
- `IOReturn AppleDiskImagesController::CreateDevice(DICreateDeviceParams *, DICreateDeviceReply *, OSSharedPtr<AppleDiskImageDevice> &)`
- `virtual bool AppleDiskImagesController::start(IOService *)`
- `AppleDiskImagesController`
