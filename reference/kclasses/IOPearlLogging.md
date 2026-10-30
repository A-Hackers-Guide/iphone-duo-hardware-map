# `IOPearlLogging`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePearlSEPDriver`](../kexts/com.apple.driver.ApplePearlSEPDriver.md)
- Object size: `0x70` (112 bytes)
- Metaclass: `0xfffffe000b9888f8`; metaclass vtable `0xfffffe00081a0cd0`; class vtable `0xfffffe00081a0c38`
- Registration (init): `0xfffffe00093ba030`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (37)

- `ERROR: IOPearlLogging::%s: BOOT-ARG WARNING: pearl-logging-state-override:0x%x, final state:0x%x !!!\n\n`
- `/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/ApplePearlSEPDriver/IOPearlLogging.cpp`
- `site.IOPearlLogging`
- `ERROR: IOPearlLogging::%s: CameraFramesHeld: %d > %d :_cameraFramesHeldLimit, dropping %u logging frames...\n\n`
- `ERROR: IOPearlLogging::%s: Unexpected messageType:%u received!\n\n`
- `ERROR: IOPearlLogging::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n`
- `ERROR: IOPearlLogging::%s: Unexpected command:%u received!\n\n`
- `ERROR: IOPearlLogging::%s: Unexpected camSequenceType:%d for frameId:[%d:%d]!\n\n`
- `ERROR: IOPearlLogging::%s: Frames present in hold queue! Flushing ...\n\n`
- `IOPearlLogging`
- `ERROR: IOPearlLogging::%s: Failed to log all held frames! Flushing the hold queue ...\n\n`
- `IOPearlLogging::%s: WARNING: Debug frames seems to be stuck in queue. Notifying client to flush the queue...\n`
- `IOPearlLogging::%s: kKLM_FrameDebugData frameId:[%d:%d] <-dbg- SPRL (log:%d)\n`
- `IOPearlLogging::%s <- state:0x%x, options:(enrollFaceDetectSkipCount:%d, faceDetectSkipCount:%d)\n`
- `IOPearlLogging::%s: ALS service registered: orientation:%u, placement:%u, cameraPosition:%u\n`
- `IOPearlLogging::%s -> \n`
- `IOPearlLogging::%s -> result:%d (driver:%p)\n`
- `IOPearlLogging::%s: ERROR: Cannot initialize FramesLogging! FramesLogging is disabled!\n`
- `IOPearlLogging::%s: WARNING: FaceDetectFrames logging enabled while FramesLogging is disabled. No frames will be logged until either FramesRawLogging or FramesMetaLogging is enabled.\n`
- `IOPearlLogging::%s -> err:0x%x\n`
- `IOPearlLogging::%s -> void\n`
- `Couldn't create OS Log for 'com.apple.BiometricKit.IOPearlLogging'!\n`
- `IOPearlLogging::%s: Camera frames STUCK, dumping queue states...\n`
- `IOPearlLogging::%s: frameDebugCount:%d, dropping frame...\n`
- `IOPearlLogging::%s: ERROR: Cannot initialize FramesDebugLogging! FramesDebugLogging is disabled!\n`
- `IOPearlLogging::%s -> err:0x%x, debugDataSize:%lu, debugDataProbeSize:%lu\n`
- `IOPearlLogging::%s <- \n`
- `IOPearlLogging::%s: Frames debug STUCK, dumping queue states...\n`
- `IOPearlLogging::%s -> result:%d\n`
- `IOPearlLogging::%s <- type:%d, eventTime:%llx, descriptor:%p, descriptorSize:%llu, dataTimeId:%llx, sequenceId:(number:%d)\n`
- `IOPearlLogging::%s: ERROR: Cannot initialize FaceDetectFrames logging! FaceDetectFrames logging is disabled!\n`
- `IOPearlLogging::%s: ALS service close: orientation:%u, cameraPosition:%u\n`
- `IOPearlLogging::%s: Found ALS service: orientation:%u, placement:%u, cameraPosition:%u\n`
- `IOPearlLogging::%s: WARNING: SequenceDebugLogging enabled while SequenceInfoLogging is disabled. No sequence debug data will be logged until SequenceInfoLogging is enabled.\n`
- `IOPearlLogging::%s -> err:0x%x (dbgSize:%lu)\n`
- `IOPearlLogging::%s <- type:%d, eventTime:%llu, data:%p, dataSize:%zu, dataTimeId:%llx, sequenceId:(number:%d)\n`
- `IOPearlLogging::%s: ERROR: Cannot initialize SequenceDebugLogging! SequenceDebugLogging is disabled!\n`
