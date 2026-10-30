# `/System/Library/PrivateFrameworks/MiniDisplay.framework/MiniDisplay`

From the upgrade restore ramdisk (141-29011-104.dmg). 142,928 bytes.

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
B28@0:8B16^@20
f24@0:8Q16
B44@0:8Q16Q24f32f36f40
@16@0:8
B16@0:8
B32@0:8@16^@24
@\"NSArray\"
B48@0:8Q16Q24Q32Q40
@\"NSObject<OS_dispatch_semaphore>\"
Q
B24@0:8f16f20
B36@0:8Q16f24f28f32
B
@32@0:8@16@24
B32@0:8Q16Q24
v16@0:8
Q16@0:8
S20@0:8f16
@\"NSMutableArray\"
C
B56@0:8Q16Q24Q32Q40Q48
^{LEDMDStateRptHeader=CQ}16@0:8
B64@0:8r^v16Q24@32Q40Q48^@56
B40@0:8@16@24^@32
@\"MDInterface\"
@\"NSMutableData\"
^{__IOHIDDevice=}
B36@0:8@16B24^@28
v24@0:8^{__IOHIDDevice=}16
@32@0:8@16^@24
Q
-[MDFrame setElementForDisplay:atIndex:red:green:blue:]
v8@?0
-[MDInterfaceHID deviceAdded:]
IOClass
MDXCoords
MDBitDepth
-[MDController submitFrame:error:]
-[MDFrame setPixelForDisplay:atIndex:red:green:blue:]
Drawing
PeppyHIDDevice
-[MDInterfaceHID setOutOfBoxFlag:error:]
YES
MDDisplayProcessClear
-[MDController close]
MDDisplayLUT
NO
OOBFlag
RegisterLUTData
-[MDFrame setPixelForDisplayAtIndex:red:green:blue:]
MDRingCoords
MDElementIndex
-[MDInterfaceHID _readRegistryProperties]
-[MDController newFrame]
-[MDController setOutOfBoxFlag:error:]
DeviceUsage
-[MDInterfaceHID open]
MDHWVersion
VersionInfo
MDDisplayProcessSet
-[MDFrame setElementAtIndex:red:green:blue:]
-[MDFrame setLEDPixelPlus:minus:]
com.apple.MiniDisplay
MiniDisplayDriver
-[MDInterfaceHID registerLUT:gammaCount:brightnessBins:entrySize:forType:error:]
-[MDController init]
-[MDFrame initWithInterface:pixelInfo:]
MDXCoord
MDYCoord
MDDisplayBrightness
DeviceUsagePage
MDYCoords
+[MDController sharedInstance]
-[MDController open]
-[MDFrame setLEDPlus:minus:]
default
RegisterLUTInfo
-[MDController registerLUT:gammaCount:brightnessBins:entrySize:forType:error:]
%s failed!
%s %lu %f %f %f
%s %lu %lu %lu %lu
%s %lu %lu %lu %lu %lu
%s error: invalid entry size %zu
%s error: invalid version data.
HID Interface registry read. status: %d count:%lu HWVersion:%lu
setDisplayProperty status: %d error:%@
%s device open error 0x%x
%s
%s error: already open
%s error!
%s error: not open
%s error: %@
%s %s
%s %f %f
%s %lu %lu %f %f %f
%s %lu %lu
%s device regID: 0x%llx
%s error: can't find device.
%s gammaCount:%zu brightnessBins:%@ entrySize:%zu forType:%u
MDInterface
MDFrame
MDInterfaceHID
MDController
floatValue
_isOpen
getBytes:range:
TQ,R,N,V_displayCount
_setProperty:forKey:error:
objectForKeyedSubscript:
_owner
close
copy
dictionaryWithObjects:forKeys:count:
frameSize
hwVersion
numberWithUnsignedInt:
objectAtIndexedSubscript:
numberWithBool:
interface
sharedInstance
submitFrame:error:
T@\"NSArray\",R,N
T@\"NSArray\",R,N,V_pixelInfo
TQ,R,N
_interface
registerLUT:gammaCount:brightnessBins:entrySize:forType:error:
setOutOfBoxFlag:error:
T^{LEDMDStateRptHeader=CQ},R,N
.cxx_destruct
isEqual:
isOpen
length
pixelInfo
unsignedIntValue
_findDevice
_ledBrightnessFromNormalizedValue:
count
newFrame
normalizedYCoordForIndex:
numberWithInt:
dataWithLength:
TB,R,N,V_isOpen
TQ,R,N,V_hwVersion
setDisplayProperty:value:error:
_getPropertyForKey:error:
_sema
bitDepth
setElementAtIndex:red:green:blue:
numberWithUnsignedChar:
addObject:
TQ,R,N,V_elementCount
_managerCanceled
_ringCoords
_version
setValue:forKey:
TQ,R,N,V_bitDepth
dealloc
_xCoords
_displayCount
_elementCount
_pixelInfo
_readRegistryProperties
deviceAdded:
elementCount
setLEDPlus:minus:
_device
setLEDPixelPlus:minus:
_bitDepth
countByEnumeratingWithState:objects:count:
dataWithBytesNoCopy:length:
displayCount
initWithInterface:pixelInfo:
mutableBytes
normalizedXCoordForIndex:
open
hidReportHeader
_frame
_hwVersion
dataWithBytesNoCopy:length:freeWhenDone:
isEqualToString:
setElementForDisplay:atIndex:red:green:blue:
setPixelForDisplayAtIndex:red:green:blue:
init
getBytes:length:
numberWithFloat:
setPixelForDisplay:atIndex:red:green:blue:
_yCoords
errorWithDomain:code:userInfo:
```
