# `/usr/lib/libSMC.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,030,544 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 2040)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/usr/lib/libSMC.dylib (compatibility version 1.0.0, current version 40.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (66)

```
[%{public}s:%d] 1ms Channel count type failed\n
[%{public}s:%d] Populate 1ms channel info failed\n
[%{public}s:%d] Connection to %s failed\n
[%{public}s:%d] Invalid input\n
[%{public}s:%d] Input handle is NULL\n
[%{public}s:%d] IOConnectCallScalarMethod failed: %d\n
[%{public}s:%d] io_connect_t handle is NULL\n
[%{public}s:%d] Populate 1s channel info failed\n
[%{public}s:%d] Read MSXA key failed\n
[%{public}s:%d] smcObject is NULL\n
[%{public}s:%d] SMC OSAccum 1ms look up table is NULL\n
[%{public}s:%d] Read MSXN key failed\n
[%{public}s:%d] IOServiceOpen failed with %s: %d\n
[%{public}s:%d] 1s Channel count type failed\n
[%{public}s:%d] Unable to allocate: smc_connect_t\n
[%{public}s:%d] Unable to allocate: SMCRegInfo\n
[%{public}s:%d] Failed to create notification port\n
[%{public}s:%d] Could not find service: %s\n
[%{public}s:%d] Read RPlt failed\n
[%{public}s:%d] SMC OSAccum is not initialized via SMCOSAccumIsSupported\n
[%{public}s:%d] Read MSXn key failed\n
[%{public}s:%d] AE fetch request format failed: %d\n
[%{public}s:%d] AE fetch channel index failed: %d\n
[%{public}s:%d] AE fetch request size failed: %d\n
[%{public}s:%d] AE fetch request key failed: %d\n
[%{public}s:%d] Unsupported notification type: %s\n
[%{public}s:%d] SMC OSAccum 1s look up table is NULL\n
[%{public}s:%d] SMC Accumulator Exposer populate platform failed\n
[%{public}s:%d] Read MSXA key failed: %d\n
[%{public}s:%d] KeyInfo data size > SMC_MAX_KEY_SIZE [%u > %u]\n
[%{public}s:%d] SMCConvertNumericToBytes failed: type: %u, expected bits: %u\n
[%{public}s:%d] Accumulator Exposer not found, so populating legacy config\n
'%s' (pid %d) opened %d '%s' user clients (%d total)\n
[%{public}s:%d] IOMainPort failed: %d\n
[%{public}s:%d] Failed to register notification with %s: %d\n
SMCOpenAppleSMC
IOUserClientCreator
NULL
SMCAccumGetChannelInfoForKey
SMCOpenConnection
_unregisterForNotification
SMCOSAccumIsSupported
SMCKextCall
SMCOpenConnectionWithDefaultService
SMCCloseConnection
SMCAEPopulateAccumKeys
AppleSMC
SMCCloseAppleSMC
IOUserClient
SMC gNotifications
SMCRegisterForSubTypeNotification
SMCParseAccumOutputToNumeric
SMCFunctions.c
SMCAEPopulatePlatform
IOService
IOGeneralInterest
0 == 1
power-state-notify
SMCRegisterForSubTypeNotification_block_invoke
pid %d, %128s
SMCConvertNumericToBytes
SMCAccumIsSupported
v8@?0
SMCAEPopulateChannelInfo
system-state-notify
hid-event-notify
```
