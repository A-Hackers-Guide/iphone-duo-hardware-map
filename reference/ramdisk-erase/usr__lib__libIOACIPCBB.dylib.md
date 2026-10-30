# `/usr/lib/libIOACIPCBB.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 85,008 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2000)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libIOACIPCBB.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libIOACIPC.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (48)

```
IOACIPCBBNetCfgClass::%s: Requesting FilterRule data failed (0x%x)\n
IOACIPCBBNetCfgClass::%s: Completing FilterRule (rule-id = %u)\n
IOACIPCBBNetCfgClass::%s: FilterRule was completed after Timeout or Baseband was reset meanwhile (0x%x)\n
IOACIPCBBNetCfgClass::%s: AppleCellularDataPlane Offloading Request Received, rule-id: %u\n
IOACIPCBBNetCfgClass::%s: Service selected with sim-context: %d\n
IOACIPCBBNetCfgClass::%s: Adding Network Interface (id = %u, prioUL = %u, rss = %u)\n
IOACIPCBBNetCfgClass::%s: AppleCellularDataPlane Notification received: 0x%x\n
IOACIPCBBNetCfgClass::%s: AppleCellularDataPlane terminated\n
IOACIPCBBNetCfgClass::%s: Retrieving Filter Rule Data, rule-id: %u\n
IOACIPCBBNetCfgClass::%s: ERROR: AppleCellularDataPlane Offloading Request has no Data, rule-id: %u, result: 0x%x\n
IOACIPCBBNetCfgClass::%s: SIM context: %d\n
IOACIPCBBNetCfgClass::%s: Service already available\n
IOACIPCBBNetCfgClass::%s: kACDPNetCfgUserClientOpen failed: 0x%x\n
IOACIPCBBNetCfgClass::%s: open failed: 0x%x\n
IOACIPCBBNetCfgClass::%s: \n
IOACIPCBBNetCfgClass::%s: IOService has no SIM context assigned\n
IOACIPCBBNetCfgClass::%s: ERROR: unable to read SIM context\n
IOACIPCBBNetCfgClass::%s: --done\n
IOACIPCBBNetCfgClass::%s: no service\n
IOACIPCBBNetCfgClass::%s: Requesting FilterRule data (rule-id = %u)\n
IOACIPCBBNetCfgClass::%s: Cancelling FilterRule Completion (rule-id = %u)\n
IOACIPCBBNetCfgClass::%s: Testing Offload FilterRule (interface-id = %u)\n
IOACIPCBBNetCfgClass::%s: ERROR: SIM context wrong type\n
IOACIPCBBNetCfgClass::%s: is open\n
IOACIPCBBNetCfgClass::%s: Adding Network Interface failed (0x%x)\n
Unable to allocate DispatchQueue
!fNotificationObject
setNotificationPort
cancelFilterRuleCompletion
stop
open
IOACIPCBBNetCfgClass
~IOACIPCBBNetCfgClass
IOGeneralInterest
fNotificationPort
v8@?0
kr == KERN_SUCCESS
open_nl
addNetIf
completeFilterRule
testOffload
v20@?0I8^v12
AppleCellularDataPlaneNotification
sim-context
start
IOACIPCBBNetCfgClass.cpp
close
getFilterRule
```
