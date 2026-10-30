# `/System/Library/PrivateFrameworks/MiniDisplay.framework/MiniDisplay`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 142,928 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 3104)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/MiniDisplay.framework/MiniDisplay (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (4 classes, 0 protocols)

Classes: `MDController`, `MDFrame`, `MDInterface`, `MDInterfaceHID`

## Strings (188)

```
%s %lu %f %f %f
%s %lu %lu %lu %lu
%s %s
%s error: already open
%s error!
%s error: not open
%s failed!
%s %lu %lu %lu %lu %lu
%s device open error 0x%x
%s error: can't find device.
%s error: invalid entry size %zu
%s error: invalid version data.
HID Interface registry read. status: %d count:%lu HWVersion:%lu
setDisplayProperty status: %d error:%@
%s %f %f
%s %lu %lu %f %f %f
%s %lu %lu
%s device regID: 0x%llx
%s gammaCount:%zu brightnessBins:%@ entrySize:%zu forType:%u
%s
%s error: %@
MDFrame
MDInterfaceHID
MDController
MDInterface
_readRegistryProperties
mutableBytes
normalizedXCoordForIndex:
getBytes:range:
_setProperty:forKey:error:
dataWithBytesNoCopy:length:
displayCount
numberWithInt:
setLEDPlus:minus:
_sema
count
errorWithDomain:code:userInfo:
getBytes:length:
numberWithUnsignedChar:
_frame
_hwVersion
_owner
init
setLEDPixelPlus:minus:
_device
elementCount
setElementForDisplay:atIndex:red:green:blue:
setOutOfBoxFlag:error:
_findDevice
_getPropertyForKey:error:
_ringCoords
addObject:
initWithInterface:pixelInfo:
open
T@\"NSArray\",R,N,V_pixelInfo
TQ,R,N,V_elementCount
.cxx_destruct
TQ,R,N,V_hwVersion
bitDepth
deviceAdded:
numberWithFloat:
sharedInstance
_bitDepth
_version
copy
countByEnumeratingWithState:objects:count:
dataWithBytesNoCopy:length:freeWhenDone:
dictionaryWithObjects:forKeys:count:
pixelInfo
setPixelForDisplay:atIndex:red:green:blue:
_managerCanceled
TQ,R,N
dealloc
interface
isEqual:
setValue:forKey:
_xCoords
isEqualToString:
length
objectAtIndexedSubscript:
registerLUT:gammaCount:brightnessBins:entrySize:forType:error:
setPixelForDisplayAtIndex:red:green:blue:
submitFrame:error:
TB,R,N,V_isOpen
T@\"NSArray\",R,N
TQ,R,N,V_bitDepth
dataWithLength:
_interface
_yCoords
hwVersion
isOpen
numberWithBool:
TQ,R,N,V_displayCount
normalizedYCoordForIndex:
_isOpen
_displayCount
hidReportHeader
setDisplayProperty:value:error:
_elementCount
frameSize
newFrame
T^{LEDMDStateRptHeader=CQ},R,N
_ledBrightnessFromNormalizedValue:
close
objectForKeyedSubscript:
setElementAtIndex:red:green:blue:
unsignedIntValue
floatValue
numberWithUnsignedInt:
_pixelInfo
@\"NSArray\"
@32@0:8@16@24
^{__IOHIDDevice=}
@16@0:8
B24@0:8f16f20
@\"NSObject<OS_dispatch_semaphore>\"
B28@0:8B16^@20
B
B48@0:8Q16Q24Q32Q40
^{LEDMDStateRptHeader=CQ}16@0:8
C
B36@0:8@16B24^@28
B16@0:8
Q16@0:8
B36@0:8Q16f24f28f32
B32@0:8Q16Q24
@\"NSMutableData\"
@\"NSMutableArray\"
Q
f24@0:8Q16
B44@0:8Q16Q24f32f36f40
@\"MDInterface\"
B32@0:8@16^@24
B64@0:8r^v16Q24@32Q40Q48^@56
B40@0:8@16@24^@32
B56@0:8Q16Q24Q32Q40Q48
S20@0:8f16
v24@0:8^{__IOHIDDevice=}16
@32@0:8@16^@24
v16@0:8
MiniDisplayDriver
-[MDInterfaceHID open]
-[MDInterfaceHID setOutOfBoxFlag:error:]
-[MDController submitFrame:error:]
-[MDController registerLUT:gammaCount:brightnessBins:entrySize:forType:error:]
-[MDFrame setLEDPlus:minus:]
-[MDInterfaceHID deviceAdded:]
IOClass
PeppyHIDDevice
NO
-[MDFrame initWithInterface:pixelInfo:]
-[MDFrame setElementAtIndex:red:green:blue:]
com.apple.MiniDisplay
MDXCoord
MDRingCoords
MDElementIndex
v8@?0
-[MDFrame setElementForDisplay:atIndex:red:green:blue:]
Drawing
MDDisplayLUT
MDHWVersion
-[MDInterfaceHID _readRegistryProperties]
MDDisplayProcessSet
+[MDController sharedInstance]
-[MDController init]
Q
MDYCoord
OOBFlag
RegisterLUTData
MDBitDepth
-[MDController setOutOfBoxFlag:error:]
-[MDFrame setLEDPixelPlus:minus:]
-[MDFrame setPixelForDisplay:atIndex:red:green:blue:]
MDDisplayBrightness
DeviceUsagePage
-[MDInterfaceHID registerLUT:gammaCount:brightnessBins:entrySize:forType:error:]
MDXCoords
-[MDController close]
-[MDController newFrame]
YES
RegisterLUTInfo
MDYCoords
-[MDController open]
-[MDFrame setPixelForDisplayAtIndex:red:green:blue:]
default
DeviceUsage
VersionInfo
MDDisplayProcessClear
```
