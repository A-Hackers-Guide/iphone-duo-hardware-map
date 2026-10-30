# `IOPearlFrame`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePearlSEPDriver`](../kexts/com.apple.driver.ApplePearlSEPDriver.md)
- Object size: `0x20` (32 bytes)
- Metaclass: `0xfffffe000b9887d0`; metaclass vtable `0xfffffe00081a02c8`; class vtable `0xfffffe00081a0208`
- Registration (init): `0xfffffe00093b61e4`
- Superclasses: [`IOBioShareableMemoryObject`](IOBioShareableMemoryObject.md)

## Direct subclasses (2; 4 in total)

- [`IOPearlCameraFrameInterface`](IOPearlCameraFrameInterface.md) — `com.apple.driver.ApplePearlSEPDriver`
- [`IOPearlFrameDebug`](IOPearlFrameDebug.md) — `com.apple.driver.ApplePearlSEPDriver`

## Strings in its kext that name it (21)

- `IOPearlFrameQueue`
- `site.IOPearlFrameQueue`
- `ERROR: IOPearlFrameDebug::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n`
- `_frameQueue->enqueueObject(OSDynamicPtrCast<IOPearlFrame>(frame))`
- `IOPearlFrameSupport`
- `_faceDetectQueue->enqueueObject(OSDynamicPtrCast<IOPearlFrame>(frame))`
- `IOPearlFrame::init()`
- `ERROR: IOPearlFrameQueue::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n`
- `site.IOPearlFrame`
- `site.IOPearlFrameDebug`
- `IOPearlFrame`
- `IOPearlFrameDebug`
- `/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/ApplePearlSEPDriver/IOPearlFrameSupport.cpp`
- `IOPearlFrameQueue::%s -> <%d:%s> -X-> frameId:[%d:%d] (queued:%d)\n`
- `IOPearlFrameQueue::%s -> frameId:[%d:%d] -(%d)-> <%d:%s> (queued:%d)\n`
- `IOPearlFrameDebug::%s: frameId:[%d:%d], _frameDebugCount:%d\n`
- `Couldn't create OS Log for 'com.apple.BiometricKit.IOPearlFrameSupport'!\n`
- `IOPearlFrameQueue::%s <- <%d:%s> queued:%u ->-> <%d:%s> queued:%u\n`
- `IOPearlFrameQueue::%s: <%d:%s> [QUEUED] frameId:[%d:%d]\n`
- `IOPearlFrameDebug::%s -> result:%d (frameId:[%d:%d], ppCount:%d, _frameDebugCount:%d)\n`
- `IOPearlFrameQueue::%s: <%d:%s> frameId:[%d:%d] -(%d)-> <%d:%s>\n`
