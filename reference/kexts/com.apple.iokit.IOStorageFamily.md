# `com.apple.iokit.IOStorageFamily`

- Name: I/O Kit Storage Family
- Version: `2.1`
- UUID: `F6844615-0F85-3986-B9A2-A5D95AFEFA74`
- Source version: `347.40.3.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (5) [KC]

### IOApplePartitionScheme
- `CFBundleIdentifier`: `com.apple.iokit.IOStorageFamily`
- `Content Mask`: `Apple_partition_scheme`
- `IOClass`: `IOApplePartitionScheme`
- `IOMatchCategory`: `IOStorage`
- `IOPersonalityPublisher`: `com.apple.iokit.IOStorageFamily`
- `IOProbeScore`: `2000`
- `IOPropertyMatch`:
  -
    - `Whole`: `True`
  -
    - `Content Hint`: `CD_ROM_Mode_1`
    - `Writable`: `False`
  -
    - `Content Hint`: `CD_ROM_Mode_2_Form_1`
    - `Writable`: `False`
- `IOProviderClass`: `IOMedia`

### IOBlockStorageDriver
- `CFBundleIdentifier`: `com.apple.iokit.IOStorageFamily`
- `IOClass`: `IOBlockStorageDriver`
- `IOPersonalityPublisher`: `com.apple.iokit.IOStorageFamily`
- `IOPropertyMatch`:
  - `device-type`: `Generic`
- `IOProviderClass`: `IOBlockStorageDevice`

### IOFDiskPartitionScheme
- `CFBundleIdentifier`: `com.apple.iokit.IOStorageFamily`
- `Content Mask`: `FDisk_partition_scheme`
- `Content Table`:
  - `0x01`: `DOS_FAT_12`
  - `0x04`: `DOS_FAT_16_S`
  - `0x06`: `DOS_FAT_16`
  - `0x07`: `Windows_NTFS`
  - `0x0B`: `DOS_FAT_32`
  - `0x0C`: `Windows_FAT_32`
  - `0x0E`: `Windows_FAT_16`
  - `0x14`: `DOS_FAT_16_S_Hidden`
  - `0x16`: `DOS_FAT_16_Hidden`
  - `0x42`: `Windows_LDM`
  - `0x82`: `Linux_Swap`
  - `0x83`: `Linux`
  - `0x8E`: `Linux_LVM`
  - `0xA5`: `FreeBSD`
  - `0xA6`: `OpenBSD`
  - `0xA7`: `Apple_Rhapsody_UFS`
  - `0xA8`: `Apple_UFS`
  - `0xA9`: `NetBSD`
  - `0xAB`: `Apple_Boot`
  - `0xAE`: `Apple_Encrypted`
  - `0xAF`: `Apple_HFS`
  - `0xFD`: `Linux_RAID`
- `IOClass`: `IOFDiskPartitionScheme`
- `IOMatchCategory`: `IOStorage`
- `IOPersonalityPublisher`: `com.apple.iokit.IOStorageFamily`
- `IOProbeScore`: `3000`
- `IOPropertyMatch`:
  - `Whole`: `True`
- `IOProviderClass`: `IOMedia`

### IOGUIDPartitionScheme
- `CFBundleIdentifier`: `com.apple.iokit.IOStorageFamily`
- `Content Mask`: `GUID_partition_scheme`
- `IOClass`: `IOGUIDPartitionScheme`
- `IOMatchCategory`: `IOStorage`
- `IOPersonalityPublisher`: `com.apple.iokit.IOStorageFamily`
- `IOProbeScore`: `4000`
- `IOPropertyMatch`:
  - `Whole`: `True`
- `IOProviderClass`: `IOMedia`

### IOMediaBSDClient
- `CFBundleIdentifier`: `com.apple.iokit.IOStorageFamily`
- `IOClass`: `IOMediaBSDClient`
- `IOMatchCategory`: `IOMediaBSDClient`
- `IOPersonalityPublisher`: `com.apple.iokit.IOStorageFamily`
- `IOProbeScore`: `30000`
- `IOProviderClass`: `IOMedia`
- `IOResourceMatch`: `IOBSD`


## C++ classes (13) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOApplePartitionScheme` | 0xc0 | IOPartitionScheme → IOStorage → IOService → IORegistryEntry |
| `IOBlockStorageDevice` | 0x90 | IOService → IORegistryEntry |
| `IOBlockStorageDriver` | 0x158 | IOStorage → IOService → IORegistryEntry |
| `IOBreaker` | 0x118 | IOSubMemoryDescriptor → IOMemoryDescriptor |
| `IODeblocker` | 0x148 | IOMemoryDescriptor |
| `IOFDiskPartitionScheme` | 0xc0 | IOPartitionScheme → IOStorage → IOService → IORegistryEntry |
| `IOFilterScheme` | 0x98 | IOStorage → IOService → IORegistryEntry |
| `IOGUIDPartitionScheme` | 0xc0 | IOPartitionScheme → IOStorage → IOService → IORegistryEntry |
| `IOMedia` | 0xd0 | IOStorage → IOService → IORegistryEntry |
| `IOMediaBSDClient` | 0xb0 | IOService → IORegistryEntry |
| `IOPartitionScheme` | 0xb0 | IOStorage → IOService → IORegistryEntry |
| `IOStorage` | 0x90 | IOService → IORegistryEntry |
| `IOUserBlockStorageDevice` | 0x118 | IOBlockStorageDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002030 off=0x00a5d7b0-0x00a5f7e0 addr=0xfffffe0007a617b0-0xfffffe0007a637e0 r--/r--   __TEXT            
	sz=0x00001684 off=0x00a5de78-0x00a5f4fc addr=0xfffffe0007a61e78-0xfffffe0007a634fc               __TEXT.__cstring          (CstringLiterals)
	sz=0x000002e0 off=0x00a5f500-0x00a5f7e0 addr=0xfffffe0007a63500-0xfffffe0007a637e0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0001b674 off=0x033cbf30-0x033e75a4 addr=0xfffffe000a3cff30-0xfffffe000a3eb5a4 r-x/r-x   __TEXT_EXEC       
	sz=0x0001ae14 off=0x033cbf30-0x033e6d44 addr=0xfffffe000a3cff30-0xfffffe000a3ead44          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000860 off=0x033e6d44-0x033e75a4 addr=0xfffffe000a3ead44-0xfffffe000a3eb5a4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000003b9 off=0x04a16a90-0x04a16e49 addr=0xfffffe000ba1aa90-0xfffffe000ba1ae49 rw-/rw-   __DATA            
	sz=0x00000170 off=0x04a16a90-0x04a16c00 addr=0xfffffe000ba1aa90-0xfffffe000ba1ac00               __DATA.__data             
	sz=0x00000218 off=0x00000000-0x00000218 addr=0xfffffe000ba1ac00-0xfffffe000ba1ae18               __DATA.__common           (Zerofill)
	sz=0x00000029 off=0x00000000-0x00000029 addr=0xfffffe000ba1ae20-0xfffffe000ba1ae49               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00005c40 off=0x013ee680-0x013f42c0 addr=0xfffffe00083f2680-0xfffffe00083f82c0 rw-/rw-   __DATA_CONST      
	sz=0x00000058 off=0x013ee680-0x013ee6d8 addr=0xfffffe00083f2680-0xfffffe00083f26d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000058 off=0x013ee6d8-0x013ee730 addr=0xfffffe00083f26d8-0xfffffe00083f2730         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00004c70 off=0x013ee730-0x013f33a0 addr=0xfffffe00083f2730-0xfffffe00083f73a0         __DATA_CONST.__const            
	sz=0x00000700 off=0x013f33a0-0x013f3aa0 addr=0xfffffe00083f73a0-0xfffffe00083f7aa0         __DATA_CONST.__kalloc_type      
	sz=0x00000320 off=0x013f3aa0-0x013f3dc0 addr=0xfffffe00083f7aa0-0xfffffe00083f7dc0         __DATA_CONST.__kalloc_var       
	sz=0x00000430 off=0x013f3dc0-0x013f41f0 addr=0xfffffe00083f7dc0-0xfffffe00083f81f0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d0 off=0x013f41f0-0x013f42c0 addr=0xfffffe00083f81f0-0xfffffe00083f82c0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 294 at 0x04af7e84
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F6844615-0F85-3986-B9A2-A5D95AFEFA74
008: LC_SOURCE_VERSION           347.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac5698 size=0x308
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOStorageFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOStorageFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `I/O Kit Storage Family`
- `CFBundleNumericVersion`: `34635776`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `2.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `2.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 1998-2014 Apple Inc. All rights reserved.`
- `OSBundleAllowUserLoad`: `True`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOStorageFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894930000`
- `_PrelinkExecutableRelativePath`: `IOStorageFamily`
- `_PrelinkExecutableSize`: `145053`
- `_PrelinkExecutableSourceAddr`: `-2198894930000`
- `_PrelinkKmodInfo`: `-2198828111216`

## Strings (230) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ERR`
- `%s %s: Bad block size %u`
- `IOMaximumSegmentAddressableBitCount`
- `Removable.icns`
- `GPT Attributes`
- `BSD Minor`
- `virtual void IOUserBlockStorageDevice::stop(IOService *)`
- `%x,%x:0`
- `Physical Interconnect`
- `%s %s: Terminating`
- `External.icns`
- `%s %s: Failed to submit request`
- `%s %s: Allocate resources\n`
- `Errors (Read)`
- `Removable`
- `site.IOMediaBSDClient`
- `Terminate Reason`
- `Priority`
- `disk%d%s`
- `virtual IOReturn IOUserBlockStorageDevice::doSynchronize(UInt64, UInt64, IOStorageSynchronizeOptions)`
- `IOMaximumByteCountRead`
- `Controller Characteristics`
- `IOBlockStorageDevice`
- `%s: No whole media found for media \"%s\".\n`
- `owner-uid`
- `AppleAPFSContainerScheme`
- `void IOUserBlockStorageDevice::Complete_Impl(uint32_t, kern_return_t)`
- `%s %s: Registering dext`
- `site.IORequest`
- `virtual IOReturn IOUserBlockStorageDevice::doUnmap(IOBlockStorageDeviceExtent *, UInt32, IOStorageUnmapOptions)`
- `IOMinimumSegmentAlignmentByteCount`
- `Medium Type`
- `Fatal Error Code`
- `1112211112`
- `%s %s: Failed to submit Synchronize request`
- `Latency Time (Write)`
- `com.apple.developer.driverkit.family.block-storage-device`
- `%s %s: Completing outstanding async request %u`
- `IOBlockStorageDriver`
- `IOMaximumSegmentByteCountRead`
- `IOGUIDPartitionScheme`
- `%d`
- `IOMaximumSegmentCountRead`
- `owner-gid`
- `%s[IOBlockStorageDriver]::handleStart: err '%s' from checkForMedia\n`
- `IODeblocker`
- `site.AnchorTable`
- `Apple_Driver43`
- `IOBreaker`
- `Size`
- `Content Mask`
- `IOMediaBSDClient`
- `BSD Unit`
- `%x:0`
- `Device Characteristics`
- `throttle-unit`
- `%s[IOBlockStorageDriver]::mediaStateHasChanged: err '%s' from recordMediaParameters\n`
- `12112121212221221221222122122211111222212`
- `Apple_Driver_ATAPI`
- `%s[IOBlockStorageDriver]; executeRequest: request failed to start!\n`
- `IOMaximumSegmentCountWrite`
- `UUID`
- `Content`
- `Low Power Mode`
- `site.MinorSlot *`
- `IOMaximumByteCountWrite`
- `void IOUserBlockStorageDevice::CompleteIO_Impl(uint32_t, uint64_t, kern_return_t)`
- `%s %s: Failed to submit Unmap request`
- `%s %s: Failed to submit Eject request`
- `Format Error Detail`
- `IOUserBlockStorageDevice`
- `INFO`
- `Solid State`
- `rdisk%d%s`
- `AppleAPFSContainer`
- `%s %s: failed to allocate outstanding requests table\n`
- `112`
- `12`
- `Retries (Write)`
- `site.IOBlockStorageDriver::Context`
- `0x%02X`
- `site.MinorSlot`
- `%s %s: Failed to put request to the outstanding array`
- `Total Time (Write)`
- `Media`
- `site.IOMedia`
- `Leaf`
- `IOStorage`
- `%s %s: Completing outstanding sync request %u`
- `Bytes (Write)`
- `%s[IOBlockStorageDriver]::handleStart; err '%s' from reportRemovability\n`
- `disk#`
- `IOMediaIcon`
- `%s %s: Failed to init`
- `Apple_Patches`
- `%s[IOBlockStorageDriver]::checkForMedia; err '%s' from reportMediaState\n`
- `%s: No location is found for media \"%s\".\n`
- `1`
- `%s %s: failed to init requests pool\n`
- `IOApplePartitionScheme`
- `IOUnitName`
- `site.AnchorSlot`
- `%s %s: Got null provider.`
- `Retries (Read)`
- `site.IODeblocker`
- `Content Table`
- `Writable`
- `1211111212221212111211`
- `12111112122212121112222122`
- `Whole`
- `AES-XTS`
- `IOMaximumSwapWrite`
- `Apple_Driver43_CD`
- `%s: %s.\n`
- `site.IOPartitionScheme`
- `IOUnit`
- `kern_return_t IOUserBlockStorageDevice::StartDev_Impl(IOService *, const DeviceParams *)`
- `Apple_Free`
- `Untitled %d`
- `22222222221121121`
- `site.IOUserBlockStorageDevice`
- `%s %s: StartDev() execution failed`
- `%s %s: Service is terminating`
- `Internal/External`
- `1211111212221212111`
- `%s %s: Failed to report ejectability`
- `Virtual Interface`
- `Errors (Write)`
- `%s[IOBlockStorageDriver]::mediaStateHasChanged; err '%s' from acceptNewMedia\n`
- `%s[IOBlockStorageDriver]::mediaStateHasChanged; err '%s' from decommissionNewMedia\n`
- `IOFDiskPartitionScheme`
- `2111212122`
- `owner-mode`
- `IOMaximumBlockCountWrite`
- `IOServiceDEXTEntitlements`
- `12111112122212121111112122222111112`
- `virtual bool IOUserBlockStorageDevice::willTerminate(IOService *, IOOptionBits)`
- `AES-XEX`
- `%s %s: Bad request ID`
- `Apple_partition_map`
- `IOMaximumSegmentByteCountWrite`
- `Open`
- `IOMinimumSaturationByteCount`
- `virtual bool IOUserBlockStorageDevice::init(OSDictionary *)`
- `virtual bool IOUserBlockStorageDevice::start(IOService *)`
- `virtual IOReturn IOUserBlockStorageDevice::doEjectMedia()`
- `site.MinorTable`
- `site.IOBlockStorageDriver::ExpansionData`
- `IOUnitLUN`
- `Internal.icns`
- `2111`
- `IOMaximumBlockCountRead`
- `site.IOApplePartitionScheme`
- `Bytes (Read)`
- `site.IOGUIDPartitionScheme`
- `%s %s: Bad num of outstanding IOs %u`
- `Force Unit Access`
- `Apple_Driver_ATA`
- `site.IOBlockStorageDriver`
- `Apple_patition_map`
- `IOCommandPoolSize`
- `BSD Major`
- `Statistics`
- `Protocol Characteristics`
- `site.IOFDiskPartitionScheme`
- `minor not available for device %x: %x.\n`
- `virtual IOReturn IOUserBlockStorageDevice::doAsyncReadWrite(IOMemoryDescriptor *, uint64_t, uint64_t, IOStorageAttributes *, IOStorageCompletion *)`
- `disable_external_storage`
- `Content Hint`
- `Partition ID`
- `site.IOBlockStorageDevice`
- `12112121212212222222221222111112221`
- `CD_ROM_Mode_1`
- `Physical Interconnect Location`
- `IOFilterScheme`
- `QueuedFlush`
- `1211111212221212111111111111111111221222222`
- ` `
- `site.IOBreaker`
- `BSD Name`
- `%s %s: StartDev called more than once.`
- `Preferred Block Size`
- `Physical Block Size`
- `%s %s: Failed to get device params`
- `root`
- `2122211112212221`
- `AES-CBC`
- `%s %s: Failed to allocate new dictionary`
- `%s %s: Failed to prepare request`
- `Base`
- `CFBundleIdentifier`
- `IOMedia`
- `Encryption Type`
- `Apple_Partition_Map`
- `%s %s: Stopped`
- `WriteCacheState`
- `Operations (Write)`
- `site.IOFilterScheme`
- `%s %s: Failed to allocate data buffer\n`
- `Unmap`
- `Generic`
- `%s[IOBlockStorageDriver]::systemWillShutdown, shutdown thread timed out\n`
- `Barrier`
- `com.apple.iokit.IOStorageFamily`
- `IOBundleResourceFile`
- `Operations (Read)`
- `%s %s: Started`
- `%s %s: Failed to start base`
- `iommu-parent`
- `Apple_Driver`
- `Total Time (Read)`
- `%s[IOBlockStorageDriver]::handleStart; err '%s' from reportEjectability\n`
- `EFI PART`
- `site.IOMedia::ExpansionData`
- `IOPartitionScheme`
- `kern_return_t IOUserBlockStorageDevice::RegisterDext_Impl()`
- `121111121222121211121111`
- `site.IOStorage`
- `%s %s: Request failure.`
- `Live`
- `%s %s: The number of transferred bytes is wrong`
- `%s %s: Start() execution failed`
- `device-type`
- `Latency Time (Read)`
- `1211111212221212111212`
- `External`
- `Ejectable`
- `site.IORequest * _Atomic`
- `IOStorageFeatures`
- `121111121222121211`
