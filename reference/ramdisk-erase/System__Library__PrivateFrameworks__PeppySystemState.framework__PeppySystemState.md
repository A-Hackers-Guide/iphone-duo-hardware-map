# `/System/Library/PrivateFrameworks/PeppySystemState.framework/PeppySystemState`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 113,376 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 3032)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/PeppySystemState.framework/PeppySystemState (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (3 classes, 0 protocols)

Classes: `PSSInterface`, `PSSInterfacePSOC`, `PeppySystemState`

## Strings (85)

```
FirmwareUpdate
default
OOBFlag
FactoryResetAnimation
SerialNumber
peppy-mcu0
IOClass
PeppyHIDDevice
DeviceUsagePage
DeviceUsage
v24@?0Q8^B16
com.apple.PeppySystemState
v8@?0
ApplePeppyDriver
IOServiceOpen(kApplePeppyUserClientType): 0x%x
IOConnectGetService(kApplePeppyUserClientType): 0x%x
PSSInterface
PSSInterfacePSOC
PeppySystemState
_client
_hasIOService:
interface
setBrightness:ALSOverride:withColor:forIndices:error:
dataWithContentsOfFile:
errorWithDomain:code:userInfo:
getPropertyForKey:completion:
numberWithInt:
_getUserClient
dealloc
anyObject
setState:withColor:withRate:forIndices:completion:
_getDevice
_queue
init
setProperty:forKey:completion:
_hidReport:withState:withColor:forIndices:
_driver
_connect
boolValue
bytes
count
dictionaryWithObjects:forKeys:count:
factoryResetAnimation:
copySerialNumber:error:
getPropertyForKey:error:
length
setOutOfBoxFlag:error:
updateFirmwareFromPath:error:
_interface
numberWithBool:
_hasPSOC
enumerateIndexesUsingBlock:
getOutOfBoxFlag:error:
setBrightness:withColor:forIndices:completion:
setOverrideBrightness:withColor:forIndices:completion:
setState:withColor:withRate:forIndices:error:
_device
_hidReport:withBrightness:ALSOverride:withColor:forIndices:
setProperty:forKey:error:
updateFirmware:error:
B28@0:8B16^@20
v40@0:8@16@24@?32
@16@0:8
B16@0:8
^{__IOHIDDevice=}16@0:8
v48@0:8d16Q24@32@?40
B32@0:8^B16^@24
B24@0:8^@16
@\"NSObject<OS_dispatch_queue>\"
B56@0:8Q16Q24d32@40^@48
I16@0:8
B48@0:8^{LEDStateRpt=C{LEDData=CCS}}16Q24Q32@40
I
B32@0:8^@16^@24
v32@0:8@16@?24
@\"PSSInterface\"
B52@0:8d16B24Q28@36^@44
@32@0:8@16^@24
v16@0:8
^{__IOHIDDevice=}
v56@0:8Q16Q24d32@40@?48
B24@0:8r*16
B40@0:8@16@24^@32
B32@0:8@16^@24
B52@0:8^{LEDStateRpt=C{LEDData=CCS}}16d24B32Q36@44
```
