# `com.apple.driver.AppleSART`

- Name: AppleSART
- Version: `1`
- UUID: `BC5EEA88-6789-37FD-8F92-71DCF373FDB4`
- Source version: `25.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) | `IOCoastGuardSARTMapper` | `sart,coastguard` |

## IOKit personalities (3) [KC]

### AppleSARTMarconi
- `CFBundleIdentifier`: `com.apple.driver.AppleSART`
- `IOClass`: `AppleSARTMarconi`
- `IONameMatch`: `sart-marconi,t8006`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSART`
- `IOProviderClass`: `AppleARMIODevice`

### IOCoastGuardSARTMapper
- `CFBundleIdentifier`: `com.apple.driver.AppleSART`
- `IOClass`: `IOCoastGuardSARTMapper`
- `IONameMatch`:
  - `sart,coastguard`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSART`
- `IOProviderClass`: `AppleARMIODevice`

### IOSARTMapper
- `CFBundleIdentifier`: `com.apple.driver.AppleSART`
- `IOClass`: `IOSARTMapper`
- `IONameMatch`: `sart,t8015`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSART`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSARTMarconi` | 0xb0 | IOService → IORegistryEntry |
| `IOCoastGuardSARTMapper` | 0x120 | IOMapper → IOService → IORegistryEntry |
| `IOSARTMapper` | 0x180 | IOMapper → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001348 off=0x0071cf70-0x0071e2b8 addr=0xfffffe0007720f70-0xfffffe00077222b8 r--/r--   __TEXT            
	sz=0x00000d70 off=0x0071d548-0x0071e2b8 addr=0xfffffe0007721548-0xfffffe00077222b8               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000290c off=0x0257e6d0-0x02580fdc addr=0xfffffe00095826d0-0xfffffe0009584fdc r-x/r-x   __TEXT_EXEC       
	sz=0x0000277c off=0x0257e6d0-0x02580e4c addr=0xfffffe00095826d0-0xfffffe0009584e4c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000190 off=0x02580e4c-0x02580fdc addr=0xfffffe0009584e4c-0xfffffe0009584fdc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x04991718-0x04991868 addr=0xfffffe000b995718-0xfffffe000b995868 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04991718-0x049917e0 addr=0xfffffe000b995718-0xfffffe000b9957e0               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b9957e0-0xfffffe000b995868               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001428 off=0x011df370-0x011e0798 addr=0xfffffe00081e3370-0xfffffe00081e4798 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x011df370-0x011df388 addr=0xfffffe00081e3370-0xfffffe00081e3388         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x011df388-0x011df3a0 addr=0xfffffe00081e3388-0xfffffe00081e33a0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001238 off=0x011df3a0-0x011e05d8 addr=0xfffffe00081e33a0-0xfffffe00081e45d8         __DATA_CONST.__const            
	sz=0x000000c0 off=0x011e05d8-0x011e0698 addr=0xfffffe00081e45d8-0xfffffe00081e4698         __DATA_CONST.__kalloc_type      
	sz=0x000000c8 off=0x011e0698-0x011e0760 addr=0xfffffe00081e4698-0xfffffe00081e4760         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x011e0760-0x011e0798 addr=0xfffffe00081e4760-0xfffffe00081e4798         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 57 at 0x04ae3c94
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BC5EEA88-6789-37FD-8F92-71DCF373FDB4
008: LC_SOURCE_VERSION           25.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aaf8f0 size=0x90
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSART`
- `CFBundleIdentifier`: `com.apple.driver.AppleSART`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSART`
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
- `NSHumanReadableCopyright`: `Copyright © 2018 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSART.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898339984`
- `_PrelinkExecutableRelativePath`: `AppleSART`
- `_PrelinkExecutableSize`: `20940`
- `_PrelinkExecutableSourceAddr`: `-2198898339984`
- `_PrelinkKmodInfo`: `-2198828656872`

## Strings (67) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `_provider != NULL`
- `length <= UINT32_MAX`
- `site.AppleSARTMarconi`
- `role`
- `max-region-count`
- `(size & ((1 << 12) - 1)) == 0`
- `size <= ((size_t)((1 << (0x13)) - 1) << 12)`
- `virtual bool IOCoastGuardSARTMapper::start(IOService *)`
- `virtual IOReturn IOCoastGuardSARTMapper::iovmUnmapMemory(IOMemoryDescriptor *, IODMACommand *, uint64_t, uint64_t)`
- `unknown`
- `(_regMap = _provider->mapDeviceMemoryWithIndex(0)) != NULL`
- `uint32_t AppleSARTMarconi::_makeRegionBase(uint64_t)`
- `/Library/Caches/com.apple.xbs/ABC41D5C-9587-4D9F-8BDB-FF041AED5BDF/TemporaryDirectory.lJvBpM/Sources/AppleSART/IOSARTMapper.cpp`
- `virtual bool IOSARTMapper::_setActive(bool)`
- `(paddr & ((1 << 12) - 1)) == 0`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `_sartMappedRegs != 0`
- `_sartRegisterMap != NULL`
- `_maxRegionCount > 0`
- `paddr <= ((uintptr_t)((1 << (0x18)) - 1) << 12)`
- `_activeState`
- `/Library/Caches/com.apple.xbs/ABC41D5C-9587-4D9F-8BDB-FF041AED5BDF/TemporaryDirectory.lJvBpM/Sources/AppleSART/IOCoastGuardSARTMapper.cpp`
- `KERN_SUCCESS == pmap_iommu_ioctl(&_ppl->super, SART_IOCTL_SET_ACTIVE, &activeState, sizeof(activeState), NULL, 0)`
- `rSART_REGION_BASE(_regBase, i) == _makeRegionBase(regions[i].base)`
- `virtual IOReturn IOSARTMapper::iovmMapMemory(IOMemoryDescriptor *, uint64_t, uint64_t, uint32_t, const IODMAMapSpecification *, IODMACommand *, const IODMAMapPageList *, uint64_t *, uint64_t *)`
- `sart-power-managed`
- `sart-power-reg-offset`
- `rSART_REGION(_regBase, i) == _makeRegion(regions[i].size, regions[i].base & 1)`
- `rSART_REGION_BASE(_regBase, i) == 0`
- `int IOSARTMapper::_addRegion(uintptr_t, uint32_t, bool)`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `rSART_REGION(_regBase, i) == 0`
- `_started`
- `/Library/Caches/com.apple.xbs/ABC41D5C-9587-4D9F-8BDB-FF041AED5BDF/TemporaryDirectory.lJvBpM/Sources/AppleSART/AppleSARTMarconi.cpp`
- `(base & (((1 << 12) - 1) - 1)) == 0`
- `uint32_t AppleSARTMarconi::_makeRegion(uint64_t, bool)`
- `121111121222121212222222221121211112`
- `\"%s:%s:%u REQUIRE failed: %s\" @%s:%d`
- `AppleSARTMarconi`
- `IOSARTMapper`
- `IOCoastGuardSARTMapper.cpp`
- `_sartPowerRegisterMap != NULL`
- `base <= ((uintptr_t)((1 << (0x18)) - 1) << 12)`
- `site.IOSARTMapper`
- `121111121222121212222222221112112222222222222222`
- `virtual IOReturn IOSARTMapper::iovmInsert(uint32_t, uint64_t, uint64_t, uint64_t, uint64_t)`
- `virtual IOReturn IOCoastGuardSARTMapper::iovmMapMemory(IOMemoryDescriptor *, uint64_t, uint64_t, uint32_t, const IODMAMapSpecification *, IODMACommand *, const IODMAMapPageList *, uint64_t *, uint64_t *)`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `\"%s\" @%s:%d`
- `segmentLength <= UINT32_MAX`
- `(count > 0) && (count <= _maxRegionCount) && ((count * sizeof(region_descriptor)) == length)`
- `IOSARTMapper.cpp`
- `IOCoastGuardSARTMapper`
- `virtual IOReturn IOCoastGuardSARTMapper::callPlatformFunction(const OSSymbol *, bool, void *, void *, void *, void *)`
- `1211111212221212111112`
- `OSBoundedPtr.h`
- `setActive`
- `_activeTransientMappings > 0`
- `virtual bool AppleSARTMarconi::start(IOService *)`
- `AppleSARTMarconi.cpp`
- `data != NULL`
- `region`
- `virtual bool IOSARTMapper::start(IOService *)`
- `virtual IOReturn IOSARTMapper::iovmUnmapMemory(IOMemoryDescriptor *, IODMACommand *, uint64_t, uint64_t)`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `sart-version`
- `site.IOCoastGuardSARTMapper`
