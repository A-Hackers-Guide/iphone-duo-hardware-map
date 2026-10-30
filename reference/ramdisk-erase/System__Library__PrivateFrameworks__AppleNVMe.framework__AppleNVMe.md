# `/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 96,176 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1760)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (97)

```
EmbeddedDeviceTypeSysConfig
EmbeddedDeviceTypeSideBar
This disk is hosted by a non-Apple NVMe controller
IONVMeController
AppleNVMeSideBarNamespaceWrite
inBufferSize > 0
EmbeddedDeviceTypeME
AppleNVMeNamespaceDevice
AppleNVMeNamespaceAccessFindServiceByName
EmbeddedDeviceTypeFirmware
An internal API error occurred
propertyRef != NULL
AppleNVMeNamespaceAccessReadData
EmbeddedDeviceTypePcieBootFirmware
IODeviceTree:/arm-io/ans
AppleNVMeSideBarNamespaceClean
AppleAPFSVolume
currentObject != IO_OBJECT_NULL
Role
EmbeddedDeviceTypeCalibration
IODeviceTree:/arm-io/apcie/pci-bridge0/s3e
Could not open a connection to the NVMe driver
Could not find a namespace device for the SideBar namespace
IOService
EmbeddedDeviceTypeEAN
IODeviceTree:/product/util
A bad argument was supplied to this API
Whole
AppleNVMeSideBarNamespaceRead
diskService != IO_OBJECT_NULL
Sanitize Support
EmbeddedDeviceTypeRoot
EmbeddedDeviceTypeEffaceable
EmbeddedDeviceTypePanicLog
blockSize > 0
Could not find the disk service in the registry
The read or write call to the driver failed
/Library/Caches/com.apple.xbs/57299ACE-6947-4BFD-AC2C-6468CDE8BAFA/TemporaryDirectory.Zwct8e/Sources/IONVMeFamily_user/AppleNVMeFramework/Source/AppleNVMePanicLogAccess.c
blockCount > 0
outBytesRead != NULL
Preferred Block Size
sideBarNamespaceTypeString != NULL
driverConnection != 0
System
inoutBuffer != NULL
AppleNVMeNamespaceAccessGetBlockCount
kern_status == kIOReturnSuccess
Could not find a corresponding APFS physical store for the disk
kernReturn == 0 
numberConvertedOK == true
disk
strncmp ( \"disk\", inBSDName, strlen ( \"disk\" ) ) == 0
IOObjectConformsTo ( diskService, kIOMediaClass )
%s failed, kernResult = 0x%x \n
AppleNVMeNamespaceAccessGetBlockSize
Sanitize Status SSTAT
%s IOServiceAddMatchingNotification () failed\n
WaitForNVMeNSAccessService
AppleNVMeNamespaceAccessUnmapRange
EmbeddedDeviceTypeBIS
EmbeddedDevicePanicLogNamespace
service != IO_OBJECT_NULL
CFGetTypeID ( propertyRef ) == CFNumberGetTypeID ( )
strlen ( inBSDName ) >= strlen ( \"diskX\" )
IOPropertyMatch
IOServiceFirstMatch
outBuffer != NULL
Success
The controller return a unsuccessful NVMe status code
/Library/Caches/com.apple.xbs/57299ACE-6947-4BFD-AC2C-6468CDE8BAFA/TemporaryDirectory.Zwct8e/Sources/IONVMeFamily_user/AppleNVMeFramework/Source/AppleNVMeSideBarAccess.c
%s: Warning - Using whole disk (%s) with base offset of 0\n
%s failed, NVMe device returned error 0x%x \n
NULL
EmbeddedDeviceTypeLifeboat
connection != IO_OBJECT_NULL
role
APFS
AppleNVMeSideBarGetRootDiskInfo
Base
nvmeDeviceService != IO_OBJECT_NULL
%s IONotificationPortCreate () failed\n
AppleNVMeNamespaceAccessWriteData
EmbeddedDeviceTypeAHCI
AssertMacros: %s, %s file: %s, line: %d, value: %lld\n
ANS2
Unknown error
inBlockCount > 0
kernResult == 0 
EmbeddedDeviceTypeControlBits
EmbeddedDeviceTypeNVRAM
Could not find the NVMe device for this disk
CFGetTypeID ( propertyRef ) == CFBooleanGetTypeID ( )
AppleEmbeddedNVMeController
sanitize-counters
currentObject != registryRoot
IOMedia
Sanitize Progress
```
