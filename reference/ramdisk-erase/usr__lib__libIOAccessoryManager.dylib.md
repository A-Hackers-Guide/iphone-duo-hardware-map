# `/usr/lib/libIOAccessoryManager.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 146,288 bytes.

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
%s: service %d, categoryID 0x%x, propertyID 0x%x, dataSize %zu, ret %x
%s: service %d, categoryList %@ 
%s: service %d, category 0x%x / %ld, property 0x%x / %ld, found data %@
%s: service %d, categoryID 0x%x, propertyID 0x%x
%s: categoryList %ld, categoryID %d, handler %d
%s: categoryList %ld, categoryID %d, propertyID %d, handler %d
%s: service %d, categoryCount %d
%s: callback, index %ld / %d, entry %ld values
%s: service %d, categoryID 0x%x, propertyID 0x%x, outDataSize %lu
%s: service %d, categoryID 0x%x, propertyID 0x%x, found catIndex %ld, propIndex %ld, propertyItem %@
%s: service %d, connect %d, arg [%llx  %llx]
%s: service %d, categoryID 0x%x, propertyID 0x%x, ret %x
%s: service %d, categoryID 0x%x, propertyID 0x%x, dataSize %zu
%s: service %d, connect %d, arg [%llx  %llx  %llx], dataSize %zu / %d
%s: service %d, *outDataCount %u, ret %x
%s: service %d, categoryID 0x%x, found catIndex %ld, categoryCount %ld, categoryItem %@
%s: service %d, category 0x%x / %ld, found propertyList %@
%s: service %d, categoryID 0x%x, outDataCount %u, ret %x
%s: service %d, categoryID 0x%x, propertyID 0x%x, outDataSize %lu, ret %x
%s: service %d, connect %d, after call, ret %x
%s: array %ld values, upToCount %ld, handler %d
%s: call handler, i %ld, item %ld values
%s: service %d, outDataCount %u
%s: service %d, categoryID 0x%x, outDataCount %u
%s: service %d, category 0x%x / %ld, propertyCount %d
BaseResourceArbiterClient
ResourceArbiterClient
TI,R,N,V_ioService
_ioNotificationObject
_processResourceAccessStatus:
pendingResourceRequest
resourceAccessGranted
resourceAccessRevoked
sema
setDelegate:
Ti,R,N,V_pendingResourceRequest
T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_sema
Ti,R,N,V_clientPriority
clientPriority
TB,R,N,V_resourceAccessStatus
_notificationPortQueue
_sema
resourceAccessStatus
synchRequestResourceAccess
_delegate
_pendingResourceRequest
_resourceAccessStatus
asynchRequestResourceAccess:
releaseResourceAccess
resourceAccessResult:
_ioService
dealloc
_clientPriority
_ioNotificationPort
delegate
init
_ioConnect
T@\"<ResourceArbiterClientDelegate>\",W,N,V_delegate
.cxx_destruct
initWithID:
ioService
v20@0:8B16
@\"<ResourceArbiterClientDelegate>\"
I16@0:8
B
B16@0:8
B20@0:8B16
@16@0:8
v24@0:8@16
I
v16@0:8
i16@0:8
^{IONotificationPort=}
@\"NSObject<OS_dispatch_queue>\"
i
@\"NSObject<OS_dispatch_semaphore>\"
@20@0:8i16
IOAccessoryAccessoryManufacturer
IOAccessoryIDBusTransport
TransportType
DeviceVendorName
DeviceDockType
DeviceSupportedOOBPairingTypes
IOAccessoryConfigStreamInterfaceGetCategories
IOAccessoryConfigStreamInterfaceGetProperty
IOAccessoryInterfaceDeviceInfo
IOAccessoryAccessoryVersionInfo
IOAccessoryAccessoryHardwareVersion
IOAccessorySleepPowerCurrentLimit
IOAccessoryBatteryPack
cpCreateSignature failed: 0x%x\n
DeviceActiveOOBPairingType
PropertyID
IOAccessoryAccessoryModelNumber
IOAccessoryUSBConnectTypePublished
IOAccessoryIDBusTransportMaxTransmit
ioamlib
IOPropertyMatch
IOAccessoryManagerType
IOAccessoryDigitalID
IOAccessoryAccessoryFirmwareVersion
IOAccessoryPowerCurrentLimits
IOServiceOpen failed: 0x%x\n
DeviceSupportsSupports2Way
__findPropertyEntry
DevicePlatformID
__findCategoryEntry
outSignature length is invalid
IOGeneralInterest
IOAccessoryPrimaryDevicePort
IOAccessoryID
IOAccessoryDetect
IOAccessoryPowerMode
IOAccessoryActivePowerMode
IOAccessoryUSBCurrentLimit
IOAccessoryUSBCurrentLimitBase
IOAccessoryUSBCurrentLimitMaximum
IOAccessory
IOAccessoryPort
IOAccessoryPortManagerPrimaryPort
DeviceFirmwareRevision
IOAccessoryConfigStreamInterfaceRequestGetProperty
v8@?0
numberref is NULL
outSignatureDer is empty
IOAccessoryAccessoryName
IOAccessoryConfigStreamInterfaceSetProperty
CFDataCreate failed
IOAccessorySupportedPowerModes
IOAccessoryDock9Pin
IOAccessoryTransportType
DeviceModelNumber
IOAccessoryConfigStreamInterfaceGetCategoryProperties
PropertyList
PropertyData
flags
IOPropertyExistsMatch
IOAccessoryConfigStreamInterfaceGetCategories_block_invoke
B24@?0q8^{__CFDictionary=}16
com.apple.ioamlib
DeviceHardwareRevision
DeviceProductName
IOService
IOAccessoryManagerAccessoryDeviceUID
IOAccessoryInterfaceModuleSerialNumber
IOAccessoryAccessoryPPID
IOAccessoryIDBusTransportMaxReceive
DeviceSerialNumber
IOAccessoryInterfaceDeviceSerialNumber
IOAccessoryUSBConnectType
v24@?0q8^{__CFDictionary=}16
v32@?0q8q16^{__CFDictionary=}24
AppleAuthCP
invalid outRsp
invalid inCmd
outSignature is NULL
IOAccessoryManager
IOAccessoryUSBActive
__iterateDictionaryList
VADResourceArbiter
IOAccessoryPortStreamType
CategoryID
vaduserclient-queue
IOAccessoryUSBChargingVoltage
IOAccessoryDevicePort
outSignature is empty
FeaturesSupported
IOAccessoryAccessorySerialNumber
IOAccessoryManagerSleepPower
IOAccessoryUSBCurrentLimitOffset
ProtocolString
IOAccessoryConfigStreamCategoryList
```
