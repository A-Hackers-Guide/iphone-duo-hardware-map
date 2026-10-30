# `com.apple.driver.ApplePCIePIODMAGen3p0`

- Name: ApplePCIePIODMAGen3p0
- Version: `1`
- UUID: `78BD517E-2010-39AE-B6C5-26FE136A9A11`
- Source version: `1042.40.10.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.ApplePIODMA`](com.apple.driver.ApplePIODMA.md) 1.0, [`com.apple.driver.IODARTFamily`](com.apple.driver.IODARTFamily.md) 1.0, [`com.apple.iokit.IOPCIFamily`](com.apple.iokit.IOPCIFamily.md) 2.7, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) | `ApplePCIePIODMA` | `pcie-apiodma,gen3p0` |
| [`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) | `ApplePCIePIODMA` | `pcie-apiodma,gen3p0` |

## IOKit personalities (1) [KC]

### ApplePCIePIODMAGen3p0
- `CFBundleIdentifier`: `com.apple.driver.ApplePCIePIODMAGen3p0`
- `IOClass`: `ApplePCIePIODMA`
- `IONameMatch`: `pcie-apiodma,gen3p0`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePCIePIODMAGen3p0`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ApplePCIePIODMA` | 0x180 | ApplePIODMA → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001031 off=0x00687e00-0x00688e31 addr=0xfffffe000768be00-0xfffffe000768ce31 r--/r--   __TEXT            
	sz=0x00000a59 off=0x006883d8-0x00688e31 addr=0xfffffe000768c3d8-0xfffffe000768ce31               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00007308 off=0x022efdd0-0x022f70d8 addr=0xfffffe00092f3dd0-0xfffffe00092fb0d8 r-x/r-x   __TEXT_EXEC       
	sz=0x00007188 off=0x022efdd0-0x022f6f58 addr=0xfffffe00092f3dd0-0xfffffe00092faf58          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000180 off=0x022f6f58-0x022f70d8 addr=0xfffffe00092faf58-0xfffffe00092fb0d8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000110 off=0x04983088-0x04983198 addr=0xfffffe000b987088-0xfffffe000b987198 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04983088-0x04983150 addr=0xfffffe000b987088-0xfffffe000b987150               __DATA.__data             
	sz=0x00000048 off=0x00000000-0x00000048 addr=0xfffffe000b987150-0xfffffe000b987198               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000007c0 off=0x01184000-0x011847c0 addr=0xfffffe0008188000-0xfffffe00081887c0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01184000-0x01184008 addr=0xfffffe0008188000-0xfffffe0008188008         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01184008-0x01184010 addr=0xfffffe0008188008-0xfffffe0008188010         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000690 off=0x01184010-0x011846a0 addr=0xfffffe0008188010-0xfffffe00081886a0         __DATA_CONST.__const            
	sz=0x00000040 off=0x011846a0-0x011846e0 addr=0xfffffe00081886a0-0xfffffe00081886e0         __DATA_CONST.__kalloc_type      
	sz=0x000000c0 off=0x011846e0-0x011847a0 addr=0xfffffe00081886e0-0xfffffe00081887a0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x011847a0-0x011847c0 addr=0xfffffe00081887a0-0xfffffe00081887c0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 52 at 0x04ae105c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     78BD517E-2010-39AE-B6C5-26FE136A9A11
008: LC_SOURCE_VERSION           1042.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004aab958 size=0x48
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `ApplePCIePIODMAGen3p0`
- `CFBundleIdentifier`: `com.apple.driver.ApplePCIePIODMAGen3p0`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePCIePIODMAGen3p0`
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
- `NSHumanReadableCopyright`: `Copyright © 2014-2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePCIePIODMAGen3p0.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898950656`
- `_PrelinkExecutableRelativePath`: `ApplePCIePIODMAGen3p0`
- `_PrelinkExecutableSize`: `35849`
- `_PrelinkExecutableSourceAddr`: `-2198898950656`
- `_PrelinkKmodInfo`: `-2198828715896`

## Strings (63) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `virtual void ApplePCIePIODMA::_applyTunablesFromData(const OSData *, regRead_t, regWrite_t, const char *)`
- `_offloadEngineInterruptAggregatorMemoryMap != nullptr`
- `121111121222121212121111111122111111111111222222`
- `_offloadEngineMemory != nullptr`
- `Invalid Request`
- `%06lu.%06u %s:@%s %s::%s: waking disabled thread with interruptsDone = 0x%x, completionHead = %u, completionTail = %u\n`
- `executeRequestGated`
- `_offloadEngineInterruptAggregatorMemory != nullptr`
- `No error`
- `CRS`
- `UR/CA`
- `interruptOccurred`
- `%06lu.%06u %s:@%s %s::%s: status = 0x%08x command = 0x%x, command2 = 0x%x, srcAddLo = 0x%x, srcAddrHi = 0x%x, dstAddrLo = 0x%x, dstAddrHi = 0x%x\n`
- `_readOffloadEngineFabricRegister`
- `_writeOffloadEngineFabricRegister`
- `_piodmaRegisters != nullptr`
- `_offloadEngineRegisters != nullptr`
- `Unknown`
- `%06lu.%06u %s:@%s %s::%s: aggregator mask = 0x%x\n`
- `Offload Engine APIODMA`
- `apcie-apiodma-tunables`
- `_offloadEngineMemoryMap != nullptr`
- `panicString @%s:%d`
- `%06lu.%06u %s:@%s %s::%s: %s tunables being applied\n`
- `%06lu.%06u %s:@%s %s::%s: %s tunable: offset/mask/value=0x%08x/0x%08x/0x%08x, 0x%08x -> 0x%08x\n`
- `Offload Engine Fabric`
- `site.ApplePCIePIODMA`
- `_offloadEngineInterruptAggregatorRegisters != nullptr`
- `_writeOffloadEnginePIODMARegister`
- `_applyTunablesFromData`
- `getBaseAddressRegisterIndex`
- `\"%s:%u: REQUIRE failed: %s\" @%s:%d`
- `Link State Error`
- `deviceToHost`
- `(numTunables * sizeof(spdsTunable)) == data->getLength()`
- `Request Error`
- `Completion Timeout`
- `%06lu.%06u %s:@%s %s::%s: aborting command Tag 0x%x\n`
- `%06lu.%06u %s:@%s %s::%s: address = 0x%llx masked = 0x%llx, index = %u\n`
- `%06lu.%06u %s:@%s %s::%s: Spurious interrupt\n`
- `%06lu.%06u %s:@%s %s::%s: waiting for cancel completion\n`
- `ApplePCIePIODMA.cpp`
- `%06lu.%06u %s:@%s %s::%s: APCIEC_OFFLOAD_ENGINE_PIODMA: 0x%llx = 0x%x\n`
- `ApplePCIePIODMA`
- `%06lu.%06u %s:@%s %s::%s: Skipping elided %s tunable: offset/mask/value=0x%08x/0x%08x/0x%08x\n`
- `tunable->size == sizeof(uint32_t)`
- `dart-bar`
- `hostToDevice`
- `%06lu.%06u %s:@%s %s::%s: for request 0x%x, received error %u (\"%s\")\n`
- `%06lu.%06u %s:@%s %s::%s: interrupt done = 0x%x\n`
- `disableGated`
- `%06lu.%06u %s:@%s %s::%s: APCIEC_OFFLOAD_ENGINE_FABRIC: 0x%llx = 0x%x\n`
- `apcie-oe-fabric-tunables`
- `virtual bool ApplePCIePIODMA::start(IOService *)`
- `%06lu.%06u %s:@%s %s::%s: completing command Tag 0x%x, error 0x%x\n`
- `_baseAddressOffsets != nullptr`
- `_offloadEngineFabricMemoryMap != nullptr`
- `Link Down`
- `uint8_t ApplePCIePIODMA::getBaseAddressRegisterIndex(IOByteCount)`
- `%06lu.%06u %s:@%s %s::%s: no config base\n`
- `%06lu.%06u %s:@%s %s::%s: completing command Tag 0x%x\n`
- `%06lu.%06u %s:@%s %s::%s: waking disabled thread with errorValue = 0x%x, errorAddress = 0x%llx, completionHead = %u, completionTail = %u\n`
- `_readOffloadEnginePIODMARegister`
