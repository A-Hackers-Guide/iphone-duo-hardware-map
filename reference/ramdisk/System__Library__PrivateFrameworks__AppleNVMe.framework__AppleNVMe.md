# `/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe`

From the upgrade restore ramdisk (141-29011-104.dmg). 96,176 bytes.

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
IODeviceTree:/arm-io/apcie/pci-bridge0/s3e
%s: Warning - Using whole disk (%s) with base offset of 0\n
diskService != IO_OBJECT_NULL
sanitize-counters
EmbeddedDeviceTypeNVRAM
EmbeddedDeviceTypeCalibration
Preferred Block Size
nvmeDeviceService != IO_OBJECT_NULL
IOObjectConformsTo ( diskService, kIOMediaClass )
Sanitize Progress
EmbeddedDeviceTypeControlBits
This disk is hosted by a non-Apple NVMe controller
Base
sideBarNamespaceTypeString != NULL
disk
strncmp ( \"disk\", inBSDName, strlen ( \"disk\" ) ) == 0
inoutBuffer != NULL
Sanitize Status SSTAT
%s IOServiceAddMatchingNotification () failed\n
EmbeddedDevicePanicLogNamespace
AssertMacros: %s, %s file: %s, line: %d, value: %lld\n
ANS2
kernResult == 0 
AppleNVMeSideBarNamespaceClean
Sanitize Support
AppleNVMeNamespaceAccessUnmapRange
IODeviceTree:/product/util
Could not find the disk service in the registry
Could not find a corresponding APFS physical store for the disk
Could not find a namespace device for the SideBar namespace
currentObject != IO_OBJECT_NULL
CFGetTypeID ( propertyRef ) == CFBooleanGetTypeID ( )
Role
EmbeddedDeviceTypeEAN
service != IO_OBJECT_NULL
The read or write call to the driver failed
/Library/Caches/com.apple.xbs/57299ACE-6947-4BFD-AC2C-6468CDE8BAFA/TemporaryDirectory.Zwct8e/Sources/IONVMeFamily_user/AppleNVMeFramework/Source/AppleNVMeSideBarAccess.c
AppleEmbeddedNVMeController
IOPropertyMatch
AppleNVMeNamespaceAccessFindServiceByName
IOService
AppleNVMeSideBarNamespaceRead
AppleNVMeNamespaceAccessGetBlockCount
EmbeddedDeviceTypeLifeboat
EmbeddedDeviceTypeSideBar
kern_status == kIOReturnSuccess
blockCount > 0
outBuffer != NULL
A bad argument was supplied to this API
%s failed, NVMe device returned error 0x%x \n
connection != IO_OBJECT_NULL
propertyRef != NULL
AppleNVMeSideBarNamespaceWrite
AppleAPFSVolume
inBufferSize > 0
AppleNVMeNamespaceAccessGetBlockSize
AppleNVMeNamespaceAccessReadData
NULL
role
AppleNVMeSideBarGetRootDiskInfo
CFGetTypeID ( propertyRef ) == CFNumberGetTypeID ( )
inBlockCount > 0
driverConnection != 0
AppleNVMeNamespaceDevice
%s failed, kernResult = 0x%x \n
EmbeddedDeviceTypePanicLog
EmbeddedDeviceTypeBIS
outBytesRead != NULL
Whole
IONVMeController
strlen ( inBSDName ) >= strlen ( \"diskX\" )
WaitForNVMeNSAccessService
blockSize > 0
System
The controller return a unsuccessful NVMe status code
Unknown error
%s IONotificationPortCreate () failed\n
EmbeddedDeviceTypeSysConfig
EmbeddedDeviceTypeEffaceable
EmbeddedDeviceTypeAHCI
EmbeddedDeviceTypeME
Could not open a connection to the NVMe driver
IODeviceTree:/arm-io/ans
Success
Could not find the NVMe device for this disk
IOMedia
APFS
numberConvertedOK == true
An internal API error occurred
AppleNVMeNamespaceAccessWriteData
EmbeddedDeviceTypeRoot
EmbeddedDeviceTypeFirmware
EmbeddedDeviceTypePcieBootFirmware
/Library/Caches/com.apple.xbs/57299ACE-6947-4BFD-AC2C-6468CDE8BAFA/TemporaryDirectory.Zwct8e/Sources/IONVMeFamily_user/AppleNVMeFramework/Source/AppleNVMePanicLogAccess.c
currentObject != registryRoot
kernReturn == 0 
IOServiceFirstMatch
```
