# `H11ANEIn`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md)
- Object size: `0xe698` (59,032 bytes)
- Metaclass: `0xfffffe000b94c1f8`; metaclass vtable `0xfffffe00080bfd38`; class vtable `0xfffffe00080bf5a0`
- Registration (init): `0xfffffe0008d6eec4`
- Superclasses: [`ANEHWDevice`](ANEHWDevice.md) → [`ANEDeviceInterface`](ANEDeviceInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (4)

- `RTBuddyBringup` in [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'ANE'}`
- `RTBuddyBringup1` in [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'ANE1'}`
- `t8020` in [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `ane,t8020`
- `t8132exclave` in [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `ane,t8132exclave`, `IOProbeScore` = `10000`

## Strings in its kext that name it (18)

- `H11ANEInUserClient`
- `site.H11ANEInUserClient`
- `/Library/Caches/com.apple.xbs/70A4E9C2-1C56-444D-A0B3-52B7A0DE6814/TemporaryDirectory.Q2tBzn/Sources/AppleH11ANEInterface/ANEResource/ANERTGraphProgramMetaData.h`
- `com.apple.driver.AppleH11ANEInterface.%s`
- `/Library/Caches/com.apple.xbs/70A4E9C2-1C56-444D-A0B3-52B7A0DE6814/TemporaryDirectory.Q2tBzn/Sources/AppleH11ANEInterface/ANEResource/ANERTGraphRuntime.h`
- `H11ANEIn`
- `/Library/Caches/com.apple.xbs/70A4E9C2-1C56-444D-A0B3-52B7A0DE6814/TemporaryDirectory.Q2tBzn/Sources/AppleH11ANEInterface/polymer/anecommon/ane_loader/ZinComputeProgramLoader.cpp`
- `\nH11ANEIn - DART Exception @ 0x%08X\n`
- `/Library/Caches/com.apple.xbs/70A4E9C2-1C56-444D-A0B3-52B7A0DE6814/TemporaryDirectory.Q2tBzn/Sources/AppleH11ANEInterface/ANEScheduler/ANEEvent.cpp`
- `site.H11ANEIn`
- `H11ANEInDirectPathClient`
- `site.H11ANEInDirectPathClient`
- `DEBUG: H11ANEIn: SegProperty[%d] : segmentId %d , numofTdInSeg: %d, firstTd: %d, offset %llu len %llu\n`
- `DEBUG: H11ANEIn:procedure[%d] contentOffset=%llu type %d opIdx=%d seg_num=%d\n`
- `%s: %s: H11ANEInUserClient(%p): External Method Call with selector %u result %u [Client: %s, PID: %d]\n`
- `DEBUG: H11ANEIn:generic->totalBufferNbr = %d CalculatedSize=%ld\n`
- `DEBUG:H11ANEIn: barSetup[%d] barIndex=%d bufferIndex=%d \n`
- `DEBUG: H11ANEIn: tds_operations->tot = %d\n`
