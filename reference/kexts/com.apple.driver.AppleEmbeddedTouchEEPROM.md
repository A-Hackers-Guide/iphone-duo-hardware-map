# `com.apple.driver.AppleEmbeddedTouchEEPROM`

- Name: AppleEmbeddedTouchEEPROMDriver
- Version: `1`
- UUID: `9D0E72FE-726C-3F3F-98C4-FE3363902976`
- Source version: `56.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/i2c3/display-eeprom/display-eeprom-generic-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-generic-data.md) | `AppleEmbeddedTouchEEPROMDriver` | `display-generic-data,rw` |
| [`/arm-io/i2c3/display-eeprom-2/display-eeprom-generic-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-generic-data-2.md) | `AppleEmbeddedTouchEEPROMDriver` | `display-generic-data,rw` |

## IOKit personalities (1) [KC]

### AppleEmbeddedTouchEEPROM
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTouchEEPROM`
- `IOClass`: `AppleEmbeddedTouchEEPROMDriver`
- `IONameMatch`: `display-generic-data,rw`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTouchEEPROM`
- `IOProviderClass`: `AppleARMNORFlashDevice`
- `IOUserClientClass`: `AppleEmbeddedTouchEEPROMDriverUC`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEmbeddedTouchEEPROMDriver` | 0x88 | IOService → IORegistryEntry |
| `AppleEmbeddedTouchEEPROMDriverUC` | 0xe8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000025f2 off=0x0045d3f0-0x0045f9e2 addr=0xfffffe00074613f0-0xfffffe00074639e2 r--/r--   __TEXT            
	sz=0x00001fca off=0x0045da18-0x0045f9e2 addr=0xfffffe0007461a18-0xfffffe00074639e2               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00003a0c off=0x01c8d1d0-0x01c90bdc addr=0xfffffe0008c911d0-0xfffffe0008c94bdc r-x/r-x   __TEXT_EXEC       
	sz=0x0000386c off=0x01c8d1d0-0x01c90a3c addr=0xfffffe0008c911d0-0xfffffe0008c94a3c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x01c90a3c-0x01c90bdc addr=0xfffffe0008c94a3c-0xfffffe0008c94bdc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000004d0 off=0x04940150-0x04940620 addr=0xfffffe000b944150-0xfffffe000b944620 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x04940150-0x04940214 addr=0xfffffe000b944150-0xfffffe000b944214               __DATA.__data             
	sz=0x000003f8 off=0x00000000-0x000003f8 addr=0xfffffe000b944218-0xfffffe000b944610               __DATA.__common           (Zerofill)
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b944610-0xfffffe000b944620               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000f00 off=0x0108ed40-0x0108fc40 addr=0xfffffe0008092d40-0xfffffe0008093c40 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x0108ed40-0x0108ed50 addr=0xfffffe0008092d40-0xfffffe0008092d50         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x0108ed50-0x0108ed60 addr=0xfffffe0008092d50-0xfffffe0008092d60         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000d48 off=0x0108ed60-0x0108faa8 addr=0xfffffe0008092d60-0xfffffe0008093aa8         __DATA_CONST.__const            
	sz=0x00000080 off=0x0108faa8-0x0108fb28 addr=0xfffffe0008093aa8-0xfffffe0008093b28         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x0108fb28-0x0108fbf8 addr=0xfffffe0008093b28-0xfffffe0008093bf8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x0108fbf8-0x0108fc40 addr=0xfffffe0008093bf8-0xfffffe0008093c40         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 61 at 0x04ad91b8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     9D0E72FE-726C-3F3F-98C4-FE3363902976
008: LC_SOURCE_VERSION           56.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9f688 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleEmbeddedTouchEEPROMDriver`
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTouchEEPROM`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEmbeddedTouchEEPROMDriver`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2017 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedTouchEEPROMDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901222416`
- `_PrelinkExecutableRelativePath`: `AppleEmbeddedTouchEEPROMDriver`
- `_PrelinkExecutableSize`: `29646`
- `_PrelinkExecutableSourceAddr`: `-2198901222416`
- `_PrelinkKmodInfo`: `-2198828990128`

## Strings (143) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `TouchEEPROMDriver::%s: Invalid EEPROM device name: deviceName = %p, length = %u\n`
- `writeRegionInternal`
- `TouchEEPROMDriver::%s: [ENTRY] AppleEmbeddedTouchEEPROMDriver::start() called with provider=%p\n`
- `TouchEEPROMDriver::%s: Invalid name buffer\n\n`
- `TouchEEPROMDriver::%s: Device name is NULL, cannot register EEPROM instance\n\n`
- `display-index`
- `EEPROMWriteToInstance`
- `TouchEEPROMDriver::%s: [EXIT] readRegionInternal returning: 0x%x\n`
- `TouchEEPROMDriver::%s: IOService not found\n\n`
- `TouchEEPROMDriver::%s: [EXIT] publishNotificationHandler completed successfully for EEPROM %u\n`
- `12111112122212121`
- `TouchEEPROMDriver::%s: Invalid device name format '%s', using fallback instance %u\n\n`
- `TouchEEPROMDriver::%s: Grandparent service found but no name property, using fallback service name\n\n`
- `TouchEEPROMDriver::%s: Number of BIM regions returned from EDT does not match the expected count. Got %lu, expected %d\n\n`
- `TouchEEPROMDriver::%s: [ERROR] owningTask is null\n`
- `TouchEEPROMDriver::%s: [ERROR] Failed to cast provider to AppleEmbeddedTouchEEPROMDriver\n`
- `TouchEEPROMDriver::%s: [EXIT] initWithTask returning: %s\n`
- `TouchEEPROMDriver::%s: [ENTRY] externalMethod called with selector=%u\n`
- `TouchEEPROMDriver::%s: [ERROR] Invalid selector: %u (max: %u)\n`
- `EEPROMWrite`
- `getRegionSize`
- `TouchEEPROMDriver::%s: EEPROM instance already exists with index %u\n\n`
- `display-eeprom`
- `TouchEEPROMDriver::%s: Using grandparent device name '%s' (I2C device, length=%u)\n\n`
- `TouchEEPROMDriver::%s: [INFO] Read operation for eepromInstanceID= %u, regionType= 0x%08x\n`
- `TouchEEPROMDriver::%s: [INFO] Getting region size for eepromInstanceID= %u, regionType= 0x%08x\n`
- `site.AppleEmbeddedTouchEEPROMDriver`
- `TouchEEPROMDriver::%s: [INFO] Allocating EEPROM lock for first time\n`
- `TouchEEPROMDriver::%s: [SUCCESS] Global notification setup successful, handler set to instance %p\n`
- `TouchEEPROMDriver::%s: AppleEmbeddedTouchEEPROMDriver class instance not found\n\n`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `EEPROMGetInstanceIndexByName`
- `TouchEEPROMDriver::%s: Set EEPROM %u name to %s\n\n`
- `name`
- `TouchEEPROMDriver::%s: [ENTRY] UserClient start called with provider=%p\n`
- `TouchEEPROMDriver::%s: Null pointer\n`
- `TouchEEPROMDriver::%s: EEPROM %u (%s) Write to offset = 0x%08x, size = 0x%08x \n`
- `TouchEEPROMDriver::%s: Device '%s' not found\n\n`
- `TouchEEPROMDriver::%s: Cannot extract region sizes from EDT for service %s\n\n`
- `validateRegionParameters`
- `initWithTask`
- `TouchEEPROMDriver::%s: [ERROR] Failed to get entitlement object\n`
- `TouchEEPROMDriver::%s: [INFO] Direct buffer: %p, size: %u\n`
- `TouchEEPROMDriver::%s: [INFO] Calling target->writeRegion with eepromInstanceID=%u, regionType=%u, size=%u\n`
- `TouchEEPROMDriver::%s: [INFO] Global notificaiton already setup\n`
- `unknown`
- `\"%s\" @%s:%d`
- `site.AppleEmbeddedTouchEEPROMDriverUC`
- `EEPROMGetInstanceNameByIndex`
- `readRegionInternal`
- `TouchEEPROMDriver::%s: [EXIT] readRegion returning: 0x%x\n`
- `TouchEEPROMDriver::%s: EEPROM %u Size for region regionType: %x is %u\n\n`
- `TouchEEPROMDriver::%s: [EXIT] UserClient start returning: %s\n`
- `TouchEEPROMDriver::%s: [ENTRY] writeRegion called with eepromInstanceID=%u, regionType=%u, buffer=%p, inSize=%u\n`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `TouchEEPROMDriver::%s: Invalid EEPROM Instance: %u (array size: %u, device: %p)\n\n`
- `TouchEEPROMDriver::%s: Found device '%s' at instance %u\n\n`
- `TouchEEPROMDriver::%s: Null pointer to size\n\n`
- `EEPROMRead`
- `getRegionSizeInternal`
- `TouchEEPROMDriver::%s: EEPROM %u (%s) Read from offset = 0x%08x, size = 0x%08x \n`
- `TouchEEPROMDriver::%s: Null pointer for count\n\n`
- `AppleEmbeddedTouchEEPROMDriver`
- `TouchEEPROMDriver::%s: EEPROM %u name is %s\n\n`
- `TouchEEPROMDriver::%s: [INFO] getRegionSize returned: 0x%x, size=%u\n`
- `getEEPROMInstanceCount`
- `registerEEPROMInstance`
- `TouchEEPROMDriver::%s: Target instance ID %u exceeds maximum (%u)\n\n`
- `TouchEEPROMDriver::%s: Null pointer: target = %p arguments = %p\n`
- `writeRegion`
- `TouchEEPROMDriver::%s: EEPROM valid instance count is %u (array size: %u)\n\n`
- `TouchEEPROMDriver::%s: Maximum EEPROM instances (%u) reached\n\n`
- `size`
- `com.apple.private.touch.eeprom.access`
- `readRegion`
- `TouchEEPROMDriver::%s: [ENTRY] readRegionInternal called\n`
- `TouchEEPROMDriver::%s: [INFO] Calling target->readRegion with eepromInstanceID=%u, regionType=%u, outSize=%u\n`
- `TouchEEPROMDriver::%s: No grandparent service found, using fallback service name\n\n`
- `TouchEEPROMDriver::%s: Failed to add EEPROM instance for NOR device %p (%s) - maximum instances (%u) reached or other error. EEPROM discovered but not accessible to userspace.\n\n`
- `12111112122212121111111111111`
- `TouchEEPROMDriver::%s: [INFO] Mapped buffer: %p, size: %u\n`
- `eeprom.debug`
- `TouchEEPROMDriver::%s: Device '%s' assigned to target instance ID %u (name-based fallback)\n\n`
- `TouchEEPROMDriver::%s: [ENTRY] initWithTask called with owningTask=%p, type=%u\n`
- `TouchEEPROMDriver::%s: [INFO] Creating new global notification for 'display-generic-data,rw'\n`
- `TouchEEPROMDriver::%s: [ERROR] addMatchingNotification() failed\n`
- `TouchEEPROMDriver::%s: [EXIT] writeRegion returning: 0x%x\n`
- `TouchEEPROMDriver::%s: Service name is '%s' (length=%u)\n\n`
- `TouchEEPROMDriver::%s: Found display-index property: %u\n\n`
- `false`
- `EEPROMReadFromInstance`
- `TouchEEPROMDriver::%s: [ENTRY] getRegionSizeInternal called\n`
- `TouchEEPROMDriver::%s: [ERROR] provider is not a NOR flash device.\n`
- `getEEPROMInstanceNameByIndex`
- `TouchEEPROMDriver::%s: [ENTRY] publishNotificationHandler called\n`
- `TouchEEPROMDriver::%s: [EXIT] externalMethod returning: 0x%x\n`
- `TouchEEPROMDriver::%s: [INFO] writeRegion returned: 0x%x\n`
- `TouchEEPROMDriver::%s: [EXIT] writeRegionInternal returning: 0x%x\n`
- `TouchEEPROMDriver::%s: [INFO] Mapped output buffer: %p, size: %u\n`
- `EEPROMGetRegionSizeOfInstance`
- `TouchEEPROMDriver::%s: Using display-index property value %u for instance ID\n\n`
- `TouchEEPROMDriver::%s: Service %p (class: %s) is not an AppleARMNORFlashDevice\n\n`
- `TouchEEPROMDriver::%s: Found NOR device %p for service %p\n\n`
- `TouchEEPROMDriver::%s: Null pointer: target = %p reference = %p arguments = %p\n`
- `EEPROMGetInstanceCount`
- `TouchEEPROMDriver::%s: [INFO] Direct output buffer: %p, size: %u\n`
- `TouchEEPROMDriver::%s: [EXIT] getRegionSizeInternal returning: 0x%x\n`
- `TouchEEPROMDriver::%s: [INFO] EEPROM lock already exists\n`
- `TouchEEPROMDriver::%s: Buffer size is smaller than expected. Expected size is %u. Buffer Size received is %u\n\n`
- `getEEPROMInstanceIndexByName`
- `EEPROMGetRegionSize`
- `TouchEEPROMDriver::%s: [ENTRY] writeRegionInternal called\n`
- `TouchEEPROMDriver::%s: [ERROR] Start failing in the provider.\n`
- `%u`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `TouchEEPROMDriver::%s: Unknown device name pattern '%s', using fallback instance %u\n\n`
- `TouchEEPROMDriver::%s: Added new EEPROM instance %u for NOR device %p (device: %s)\n\n`
- `TouchEEPROMDriver::%s: No parent service found, using fallback service name\n\n`
- `start`
- `TouchEEPROMDriver::%s: Bad input count: %u\n\n`
- `TouchEEPROMDriver::%s: map is null.\n`
- `TouchEEPROMDriver::%s: [ERROR] Failed to allocate EEPROM lock.\n`
- `TouchEEPROMDriver::%s: Null pointer for size\n\n`
- `externalMethod`
- `TouchEEPROMDriver::%s: [ERROR] Actual region count (%u) does not match expected region count (%u)\n`
- `display-generic-data,rw`
- `TouchEEPROMDriver::%s: [EXIT] AppleEmbeddedTouchEEPROMDriver::start() completed successfully\n`
- `TouchEEPROMDriver::%s: Invalid regionType: %u\n\n`
- `TouchEEPROMDriver::%s: Invalid region regionType: %u\n\n`
- `publishNotificationHandler`
- `TouchEEPROMDriver::%s: Setting up %lu regions for EEPROM %u (%s)\n\n`
- `TouchEEPROMDriver::%s: Invalid buffer: buffer = %p, size = %u\n`
- `TouchEEPROMDriver::%s: [INFO] readRegion returned: 0x%x, actual size read: %u\n`
- `TouchEEPROMDriver::%s: [ENTRY] readRegion called with eepromInstanceID=%u, regionType=%u, buffer=%p, outSize=%p\n`
- `TouchEEPROMDriver::%s: display-index value %u exceeds maximum, using fallback\n\n`
- `TouchEEPROMDriver::%s: Null buffer\n\n`
- `OSBoundedPtr.h`
- `AppleEmbeddedTouchEEPROMDriverUC`
- `true`
- `TouchEEPROMDriver::%s: Invalid parameters\n\n`
- `display-eeprom-`
- `TouchEEPROMDriver::%s: Target instance ID %u is already occupied by device '%s'\n\n`
- `TouchEEPROMDriver::%s: No valid display-index property found, using name-based fallback\n\n`
