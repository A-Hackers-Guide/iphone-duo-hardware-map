# `/System/Library/PrivateFrameworks/PeppySystemState.framework/PeppySystemState`

From the upgrade restore ramdisk (141-29011-104.dmg). 113,376 bytes.

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
numberWithBool:
setOverrideBrightness:withColor:forIndices:completion:
_hidReport:withState:withColor:forIndices:
dataWithContentsOfFile:
getPropertyForKey:error:
setProperty:forKey:completion:
setBrightness:withColor:forIndices:completion:
_getUserClient
anyObject
copySerialNumber:error:
dictionaryWithObjects:forKeys:count:
length
setOutOfBoxFlag:error:
setProperty:forKey:error:
_getDevice
dealloc
_hasPSOC
_interface
bytes
enumerateIndexesUsingBlock:
getPropertyForKey:completion:
interface
_hidReport:withBrightness:ALSOverride:withColor:forIndices:
count
errorWithDomain:code:userInfo:
factoryResetAnimation:
init
numberWithInt:
setBrightness:ALSOverride:withColor:forIndices:error:
_driver
_connect
updateFirmware:error:
updateFirmwareFromPath:error:
_client
_device
_queue
boolValue
getOutOfBoxFlag:error:
setState:withColor:withRate:forIndices:completion:
setState:withColor:withRate:forIndices:error:
_hasIOService:
^{__IOHIDDevice=}
I
B32@0:8^@16^@24
@32@0:8@16^@24
B32@0:8^B16^@24
v40@0:8@16@24@?32
v32@0:8@16@?24
B56@0:8Q16Q24d32@40^@48
v48@0:8d16Q24@32@?40
B28@0:8B16^@20
@\"NSObject<OS_dispatch_queue>\"
@\"PSSInterface\"
B40@0:8@16@24^@32
B32@0:8@16^@24
v16@0:8
I16@0:8
B48@0:8^{LEDStateRpt=C{LEDData=CCS}}16Q24Q32@40
B52@0:8^{LEDStateRpt=C{LEDData=CCS}}16d24B32Q36@44
v56@0:8Q16Q24d32@40@?48
B24@0:8^@16
@16@0:8
B16@0:8
B24@0:8r*16
B52@0:8d16B24Q28@36^@44
^{__IOHIDDevice=}16@0:8
FactoryResetAnimation
SerialNumber
peppy-mcu0
PeppyHIDDevice
DeviceUsagePage
DeviceUsage
ApplePeppyDriver
v24@?0Q8^B16
com.apple.PeppySystemState
OOBFlag
IOClass
FirmwareUpdate
default
v8@?0
IOConnectGetService(kApplePeppyUserClientType): 0x%x
IOServiceOpen(kApplePeppyUserClientType): 0x%x
PeppySystemState
PSSInterface
PSSInterfacePSOC
```
