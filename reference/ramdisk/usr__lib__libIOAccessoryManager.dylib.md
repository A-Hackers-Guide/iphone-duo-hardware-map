# `/usr/lib/libIOAccessoryManager.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 146,288 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 3072)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libIOAccessoryManager.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (2 classes, 0 protocols)

Classes: `BaseResourceArbiterClient`, `ResourceArbiterClient`

## Strings (172)

```
IOAccessoryManagerType
IOService
IOAccessoryID
IOAccessoryPowerMode
IOAccessoryManagerSleepPower
DeviceVendorName
DeviceActiveOOBPairingType
CategoryID
FeaturesSupported
IOAccessoryAccessoryVersionInfo
IOAccessoryUSBChargingVoltage
IOAccessorySupportedPowerModes
TransportType
DeviceModelNumber
IOAccessoryConfigStreamCategoryList
B24@?0q8^{__CFDictionary=}16
IOPropertyExistsMatch
IOAccessoryAccessoryName
IOAccessoryAccessoryHardwareVersion
IOAccessoryUSBConnectTypePublished
IOAccessoryConfigStreamInterfaceGetCategoryProperties
PropertyList
PropertyID
__findCategoryEntry
IOAccessoryUSBConnectType
IOAccessory
IOAccessoryAccessorySerialNumber
IOAccessoryPortManagerPrimaryPort
DevicePlatformID
__iterateDictionaryList
outSignature is NULL
CFDataCreate failed
IOAccessoryInterfaceModuleSerialNumber
IOAccessoryUSBActive
IOAccessoryPowerCurrentLimits
DeviceFirmwareRevision
v24@?0q8^{__CFDictionary=}16
AppleAuthCP
IOAccessoryInterfaceDeviceSerialNumber
IOAccessoryDevicePort
com.apple.ioamlib
ioamlib
VADResourceArbiter
IOAccessoryConfigStreamInterfaceGetCategories
v8@?0
invalid outRsp
outSignature is empty
ProtocolString
IOAccessoryPrimaryDevicePort
IOAccessoryInterfaceDeviceInfo
IOAccessoryAccessoryManufacturer
IOAccessoryUSBCurrentLimitMaximum
IOAccessoryBatteryPack
IOAccessoryConfigStreamInterfaceGetCategories_block_invoke
IOAccessoryConfigStreamInterfaceRequestGetProperty
IOAccessoryDetect
IOAccessorySleepPowerCurrentLimit
IOAccessoryUSBCurrentLimitBase
IOServiceOpen failed: 0x%x\n
IOAccessoryIDBusTransportMaxTransmit
numberref is NULL
outSignatureDer is empty
IOAccessoryTransportType
DeviceHardwareRevision
__findPropertyEntry
DeviceProductName
DeviceDockType
outSignature length is invalid
IOPropertyMatch
IOAccessoryAccessoryFirmwareVersion
IOAccessoryDock9Pin
cpCreateSignature failed: 0x%x\n
IOAccessoryPort
IOAccessoryIDBusTransportMaxReceive
IOAccessoryUSBCurrentLimit
IOAccessoryIDBusTransport
DeviceSerialNumber
DeviceSupportedOOBPairingTypes
v32@?0q8q16^{__CFDictionary=}24
IOAccessoryConfigStreamInterfaceSetProperty
IOAccessoryAccessoryModelNumber
IOAccessoryPortStreamType
flags
IOGeneralInterest
IOAccessoryManager
IOAccessoryDigitalID
IOAccessoryAccessoryPPID
IOAccessoryActivePowerMode
IOAccessoryManagerAccessoryDeviceUID
IOAccessoryUSBCurrentLimitOffset
DeviceSupportsSupports2Way
IOAccessoryConfigStreamInterfaceGetProperty
PropertyData
invalid inCmd
vaduserclient-queue
%s: service %d, categoryList %@ 
%s: service %d, *outDataCount %u, ret %x
%s: service %d, categoryID 0x%x, found catIndex %ld, categoryCount %ld, categoryItem %@
%s: service %d, categoryID 0x%x, propertyID 0x%x, outDataSize %lu
%s: service %d, connect %d, arg [%llx  %llx]
%s: service %d, connect %d, after call, ret %x
%s: service %d, connect %d, arg [%llx  %llx  %llx], dataSize %zu / %d
%s: service %d, outDataCount %u
%s: callback, index %ld / %d, entry %ld values
%s: service %d, categoryID 0x%x, outDataCount %u, ret %x
%s: service %d, categoryID 0x%x, propertyID 0x%x, found catIndex %ld, propIndex %ld, propertyItem %@
%s: service %d, category 0x%x / %ld, property 0x%x / %ld, found data %@
%s: service %d, categoryID 0x%x, propertyID 0x%x, outDataSize %lu, ret %x
%s: service %d, categoryID 0x%x, propertyID 0x%x
%s: array %ld values, upToCount %ld, handler %d
%s: service %d, categoryID 0x%x, outDataCount %u
%s: service %d, category 0x%x / %ld, found propertyList %@
%s: service %d, categoryID 0x%x, propertyID 0x%x, dataSize %zu
%s: service %d, categoryID 0x%x, propertyID 0x%x, dataSize %zu, ret %x
%s: call handler, i %ld, item %ld values
%s: categoryList %ld, categoryID %d, handler %d
%s: service %d, categoryCount %d
%s: service %d, category 0x%x / %ld, propertyCount %d
%s: service %d, categoryID 0x%x, propertyID 0x%x, ret %x
%s: categoryList %ld, categoryID %d, propertyID %d, handler %d
BaseResourceArbiterClient
ResourceArbiterClient
_resourceAccessStatus
ioService
synchRequestResourceAccess
clientPriority
delegate
_clientPriority
T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_sema
TB,R,N,V_resourceAccessStatus
TI,R,N,V_ioService
_pendingResourceRequest
_ioNotificationPort
initWithID:
releaseResourceAccess
resourceAccessResult:
_ioService
T@\"<ResourceArbiterClientDelegate>\",W,N,V_delegate
_processResourceAccessStatus:
setDelegate:
Ti,R,N,V_pendingResourceRequest
_ioConnect
_notificationPortQueue
resourceAccessGranted
resourceAccessStatus
init
dealloc
_delegate
_ioNotificationObject
resourceAccessRevoked
sema
.cxx_destruct
Ti,R,N,V_clientPriority
asynchRequestResourceAccess:
pendingResourceRequest
_sema
@20@0:8i16
I
B
B16@0:8
v24@0:8@16
@\"<ResourceArbiterClientDelegate>\"
@\"NSObject<OS_dispatch_semaphore>\"
B20@0:8B16
v20@0:8B16
i16@0:8
^{IONotificationPort=}
v16@0:8
@16@0:8
I16@0:8
@\"NSObject<OS_dispatch_queue>\"
i
```
