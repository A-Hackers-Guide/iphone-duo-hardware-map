# `AUC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AUC`](../kexts/com.apple.AUC.md)
- Object size: `0x130` (304 bytes)
- Metaclass: `0xfffffe000b931fd0`; metaclass vtable `0xfffffe0007f93d90`; class vtable `0xfffffe0007f93820`
- Registration (init): `0xfffffe00086665b4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AUC` in [`com.apple.AUC`](../kexts/com.apple.AUC.md): `IOProviderClass` = `IOResources`

## Strings in its kext that name it (39)

- `<<<< AUC >>>>`
- `IOReturn AUC::DPRemovedNotificationGated(IOService *)`
- `virtual IOReturn AUC::hdcp_get_reply(uint8_t *, size_t *)`
- `IOReturn AUC::hdcp_send_request_gated(const uint8_t *, size_t, ConnectionWatchdog *)`
- `AUC`
- `AUCUUID`
- `AUC:%s`
- `AUCWorkloop`
- `site.AUCAsynchronousScheduler`
- `AUCWorkloop[%p] released.`
- `site.AUCLock`
- `site.AUC`
- `void AUC::InterfaceStatusAndType(IOAVVideoInterface *, UInt32 *, UInt32 *)`
- `bool AUC::DPPluggedNotification(void *, IOService *)`
- `void AUC::DPRemovedNotificationAsync(void *, void *)`
- `AUCAsynchronousScheduler`
- `bool AUC::DPRemovedNotification(void *, IOService *)`
- `site.AUCRecursiveLock`
- `site.AUCTimer`
- `site.AUCScheduler`
- `void AUC::protectedIOSurfaceSeen(IOAVVideoInterface *)`
- `void AUC::aucUpstreamConnectionStatusChanged()`
- `AUC.cpp`
- `AUCUserClient`
- `site.AUCWorkloop`
- `IOReturn AUC::DPPluggedNotificationGated(IOService *)`
- `AUCWorkLoop`
- `site.AUCUserClient*`
- `/Library/Caches/com.apple.xbs/C57CF2F6-5552-405F-94A7-90D29015B482/TemporaryDirectory.HbIjCG/Sources/CoreAUCKext/Kernel/Embedded/AUC.cpp`
- `site.AUCUserClient`
- `%s [%p] In AUC::InterfaceCapable\n`
- `%s [%p]::%s: upstreamConnectionSendMessage result r = %d,  mAUCDriver = %p, loopCount = %d.\n`
- `%s [%p] In AUC::InterfaceCapable: returning false EARLY because AVVideoInterface is inactive`
- `%s [%p] In AUC::InterfaceForDisplayType(%u)\n`
- `%s [%p] Could not cast param0: %p to AUCOUT instance\n`
- `<<<< AUC >>>> loggingLevel = %d`
- `%s [%p] In AUC::DisplayCapable\n`
- `%s [%p]::%s, Could not cast param0: %p to AUCOUT instance\n`
- `%s [%p] In AUC::InterfaceCapable: returning true EARLY because ioSurface is not protected\n`
