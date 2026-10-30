# `com.apple.driver.IODARTFamily`

- Name: IODARTFamily
- Version: `1`
- UUID: `1EE7A5EC-6A13-3FE7-A9A6-227D64A416C1`
- Source version: `373.40.4.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (76) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/dart-sep/mapper-sep`](../devicetree/root__arm-io__dart-sep__mapper-sep.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sep/mapper-sep-exclave`](../devicetree/root__arm-io__dart-sep__mapper-sep-exclave.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sio/mapper-sio`](../devicetree/root__arm-io__dart-sio__mapper-sio.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sio/mapper-aes`](../devicetree/root__arm-io__dart-sio__mapper-aes.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-aop`](../devicetree/root__arm-io__dart-sbr__mapper-aop.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-aop2`](../devicetree/root__arm-io__dart-sbr__mapper-aop2.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-exclave-aop`](../devicetree/root__arm-io__dart-sbr__mapper-exclave-aop.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-exclave-aop2`](../devicetree/root__arm-io__dart-sbr__mapper-exclave-aop2.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-mtp`](../devicetree/root__arm-io__dart-sbr__mapper-mtp.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-pmp`](../devicetree/root__arm-io__dart-sbr__mapper-pmp.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-admac-leap-ns`](../devicetree/root__arm-io__dart-sbr__mapper-admac-leap-ns.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-admac-base-ns`](../devicetree/root__arm-io__dart-sbr__mapper-admac-base-ns.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-admac-leap-s`](../devicetree/root__arm-io__dart-sbr__mapper-admac-leap-s.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-admac-base-s`](../devicetree/root__arm-io__dart-sbr__mapper-admac-base-s.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-scm`](../devicetree/root__arm-io__dart-sbr__mapper-scm.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-sbr/mapper-rsm`](../devicetree/root__arm-io__dart-sbr__mapper-rsm.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-usb0/mapper-usb`](../devicetree/root__arm-io__dart-usb0__mapper-usb.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dcp/mapper-dcp`](../devicetree/root__arm-io__dart-dcp__mapper-dcp.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dcp/mapper-dcp-exclave`](../devicetree/root__arm-io__dart-dcp__mapper-dcp-exclave.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-disp0/mapper-disp0`](../devicetree/root__arm-io__dart-disp0__mapper-disp0.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-disp0/mapper-disp0-piodma`](../devicetree/root__arm-io__dart-disp0__mapper-disp0-piodma.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-disp0/mapper-disp0-scl`](../devicetree/root__arm-io__dart-disp0__mapper-disp0-scl.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-disp0/mapper-disp0-sca`](../devicetree/root__arm-io__dart-disp0__mapper-disp0-sca.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dispgrt/mapper-dispgrt`](../devicetree/root__arm-io__dart-dispgrt__mapper-dispgrt.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-disp0-isoc/mapper-disp0-dpa`](../devicetree/root__arm-io__dart-disp0-isoc__mapper-disp0-dpa.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dcpsec/mapper-dcpsec`](../devicetree/root__arm-io__dart-dcpsec__mapper-dcpsec.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dcpsec/mapper-dcpsec-exclave`](../devicetree/root__arm-io__dart-dcpsec__mapper-dcpsec-exclave.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dispsec/mapper-dispsec`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dispsec/mapper-dispsec-piodma`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec-piodma.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dispsec/mapper-dispsec-scl`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec-scl.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dispsec/mapper-dispsec-sca`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec-sca.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dispsecgrt/mapper-dispsecgrt`](../devicetree/root__arm-io__dart-dispsecgrt__mapper-dispsecgrt.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dcpext0/mapper-dcpext0`](../devicetree/root__arm-io__dart-dcpext0__mapper-dcpext0.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dcpext0/mapper-dcpext0-exclave`](../devicetree/root__arm-io__dart-dcpext0__mapper-dcpext0-exclave.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dispext0/mapper-dispext0`](../devicetree/root__arm-io__dart-dispext0__mapper-dispext0.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dispext0/mapper-dispext0-piodma`](../devicetree/root__arm-io__dart-dispext0__mapper-dispext0-piodma.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-dispext0-isoc/mapper-dispext0-dpa`](../devicetree/root__arm-io__dart-dispext0-isoc__mapper-dispext0-dpa.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-scaler/mapper-scaler`](../devicetree/root__arm-io__dart-scaler__mapper-scaler.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-scaler/mapper-scaler-piodma`](../devicetree/root__arm-io__dart-scaler__mapper-scaler-piodma.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-jpeg/mapper-jpeg`](../devicetree/root__arm-io__dart-jpeg__mapper-jpeg.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-isp/mapper-isp`](../devicetree/root__arm-io__dart-isp__mapper-isp.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-isp/mapper-isp-mpm`](../devicetree/root__arm-io__dart-isp__mapper-isp-mpm.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-isp/mapper-isp-epipe0-exclave`](../devicetree/root__arm-io__dart-isp__mapper-isp-epipe0-exclave.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-isp/mapper-isp-epipe1-exclave`](../devicetree/root__arm-io__dart-isp__mapper-isp-epipe1-exclave.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-isp/mapper-isp-piodma1-exclave`](../devicetree/root__arm-io__dart-isp__mapper-isp-piodma1-exclave.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-isp/mapper-isp-exclave-secure1`](../devicetree/root__arm-io__dart-isp__mapper-isp-exclave-secure1.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ave/mapper-ave`](../devicetree/root__arm-io__dart-ave__mapper-ave.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-avd/mapper-avd`](../devicetree/root__arm-io__dart-avd__mapper-avd.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-avd/mapper-avd-piodma`](../devicetree/root__arm-io__dart-avd__mapper-avd-piodma.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-avd/mapper-avd-adsbuf`](../devicetree/root__arm-io__dart-avd__mapper-avd-adsbuf.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane0/mapper-ane0`](../devicetree/root__arm-io__dart-ane0__mapper-ane0.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane0/mapper-ane0-iso1`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso1.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane0/mapper-ane0-iso2`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso2.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane0/mapper-ane0-iso3`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso3.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane0/mapper-ane0-iso4`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso4.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane0/mapper-ane0-iso5`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso5.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane0/mapper-ane0-iso6`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso6.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane0/mapper-ane0-iso7`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso7.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane0/mapper-ane0-mpm`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-mpm.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane1/mapper-ane1`](../devicetree/root__arm-io__dart-ane1__mapper-ane1.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane1/mapper-ane1-iso1`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso1.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane1/mapper-ane1-iso2`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso2.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane1/mapper-ane1-iso3`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso3.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane1/mapper-ane1-iso4`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso4.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane1/mapper-ane1-iso5`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso5.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane1/mapper-ane1-iso6`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso6.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane1/mapper-ane1-iso7`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso7.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-ane1/mapper-ane1-mpm`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-mpm.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-apcie0/mapper-apcie0-control`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-control.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-apcie0/mapper-apcie0-alpha`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-alpha.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-apcie0/mapper-apcie0-beta`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-beta.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-apcie0/mapper-apcie0-piodma`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-piodma.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-apcie0/mapper-apcie0-plce`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-plce.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-apcie1/mapper-apcie1`](../devicetree/root__arm-io__dart-apcie1__mapper-apcie1.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-apcie1/mapper-apcie1-piodma`](../devicetree/root__arm-io__dart-apcie1__mapper-apcie1-piodma.md) | `IODARTMapper` | `iommu-mapper` |
| [`/arm-io/dart-apcie1/mapper-apcie1-plce`](../devicetree/root__arm-io__dart-apcie1__mapper-apcie1-plce.md) | `IODARTMapper` | `iommu-mapper` |

## IOKit personalities (1) [KC]

### IODARTMapper
- `CFBundleIdentifier`: `com.apple.driver.IODARTFamily`
- `IOClass`: `IODARTMapper`
- `IONameMatch`: `iommu-mapper`
- `IOPersonalityPublisher`: `com.apple.driver.IODARTFamily`
- `IOProviderClass`: `IODARTMapperNub`


## C++ classes (9) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IODART` | 0xc48 | IOService → IORegistryEntry |
| `IODARTClient` | 0x100 | IOUserClient → IOService → IORegistryEntry |
| `IODARTMapper` | 0xa78 | IOMapper → IOService → IORegistryEntry |
| `IODARTMapperClient` | 0xf8 | IOUserClient → IOService → IORegistryEntry |
| `IODARTMapperNub` | 0x90 | IOService → IORegistryEntry |
| `IODARTPIOAllocatorGeneric` | 0x50 | IODARTVMAllocator |
| `IODARTVMAllocator` | 0x48 |  |
| `IODARTVMAllocatorGeneric` | 0x50 | IODARTVMAllocator |
| `IODARTVMSpace` | 0x88 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000025a0 off=0x009c4be0-0x009c7180 addr=0xfffffe00079c8be0-0xfffffe00079cb180 r--/r--   __TEXT            
	sz=0x00001efb off=0x009c5258-0x009c7153 addr=0xfffffe00079c9258-0xfffffe00079cb153               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000020 off=0x009c7160-0x009c7180 addr=0xfffffe00079cb160-0xfffffe00079cb180               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00013c88 off=0x03087170-0x0309adf8 addr=0xfffffe000a08b170-0xfffffe000a09edf8 r-x/r-x   __TEXT_EXEC       
	sz=0x00013818 off=0x03087170-0x0309a988 addr=0xfffffe000a08b170-0xfffffe000a09e988          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000470 off=0x0309a988-0x0309adf8 addr=0xfffffe000a09e988-0xfffffe000a09edf8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000240 off=0x049ef4e0-0x049ef720 addr=0xfffffe000b9f34e0-0xfffffe000b9f3720 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049ef4e0-0x049ef5a8 addr=0xfffffe000b9f34e0-0xfffffe000b9f35a8               __DATA.__data             
	sz=0x00000178 off=0x00000000-0x00000178 addr=0xfffffe000b9f35a8-0xfffffe000b9f3720               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00003248 off=0x01357598-0x0135a7e0 addr=0xfffffe000835b598-0xfffffe000835e7e0 rw-/rw-   __DATA_CONST      
	sz=0x00000038 off=0x01357598-0x013575d0 addr=0xfffffe000835b598-0xfffffe000835b5d0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000038 off=0x013575d0-0x01357608 addr=0xfffffe000835b5d0-0xfffffe000835b608         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000026d8 off=0x01357608-0x01359ce0 addr=0xfffffe000835b608-0xfffffe000835dce0         __DATA_CONST.__const            
	sz=0x00000400 off=0x01359ce0-0x0135a0e0 addr=0xfffffe000835dce0-0xfffffe000835e0e0         __DATA_CONST.__kalloc_type      
	sz=0x00000410 off=0x0135a0e0-0x0135a4f0 addr=0xfffffe000835e0e0-0xfffffe000835e4f0         __DATA_CONST.__kalloc_var       
	sz=0x00000238 off=0x0135a4f0-0x0135a728 addr=0xfffffe000835e4f0-0xfffffe000835e728         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b8 off=0x0135a728-0x0135a7e0 addr=0xfffffe000835e728-0xfffffe000835e7e0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 165 at 0x04af10d0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1EE7A5EC-6A13-3FE7-A9A6-227D64A416C1
008: LC_SOURCE_VERSION           373.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004abe2f0 size=0x210
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IODARTFamily`
- `CFBundleIdentifier`: `com.apple.driver.IODARTFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IODARTFamily`
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
- `NSHumanReadableCopyright`: `Copyright © 2009-2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IODARTFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895555616`
- `_PrelinkExecutableRelativePath`: `IODARTFamily`
- `_PrelinkExecutableSize`: `104112`
- `_PrelinkExecutableSourceAddr`: `-2198895555616`
- `_PrelinkKmodInfo`: `-2198828272416`

## Strings (227) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `manual-availability`
- `noncompliant-dead-mappings`
- `getProtectionGranularity`
- `1`
- `setActive`
- `\"%s: Unable to reserve DVA range %u @ [%#llx..%#llx) pages [%#lx..%#lx) possible overlapping ranges %p\" @%s:%d`
- `(%s) %s::%s: _iomdCacheReclaimImmediate() failed!\n`
- `\"%s: pio-range property not allowed\" @%s:%d`
- `site.iomdHistoryEntry`
- `site.iomdCacheEntry`
- `\"%s: mapper for SID %u terminated with outstanding client error handler registrations\" @%s:%d`
- `(%s) %s::%s: GetAllocations: no structure or descriptor\n`
- `externalMethod`
- `111111111111111111111111111111`
- `iomd-cache-flush-on-deactive`
- `site._segmentHistoryEntry`
- `(%s) %s::%s: Failed to allocate %d pages from page 0x%x in reserved DVA range [0x%016llx..0x%016llx)\n`
- `121111121222121212222222221121111223121222111322111111111111212222222111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111121122222211111111222211222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `mapper-dynamic`
- `(%s) %s::%s: failed to allocate segment history buffer\n`
- `_iovmAlloc`
- `%s::%s: provider %p is not a DART\n`
- `IODARTClient`
- `\"%s: IODMACommand %p not prepared: 0x%x\" @%s:%d`
- `IODeviceTree:/chosen`
- `_registerMapper`
- `iommu-parent`
- `site.IODARTVMAllocator`
- `smmu-options`
- `site.pageRange_t`
- `%s\n`
- `(%s) %s::%s: Logging options changed: 0x%08X\n`
- `dart-options`
- `\"%s: failed to save global mapper property %s : %p\" @%s:%d`
- `site.IODARTErrorInfo`
- `\"unsupported\" @%s:%d`
- `(%s) %s::%s: Zero-length IODC %p at offset 0x%llx\n`
- `1211111212221212111111111111112`
- `21112132`
- `iomdInterfaceTest`
- `(%s) %s::%s: free request at 0x%08x has different number of client pages (0x%08x) than VM space (0x%08x) at %p [0x%08x..0x%08x)\n`
- `IODARTVMAllocatorGeneric`
- `init`
- `(%s) %s::%s: descriptor map failed\n`
- `dart-map-seg-limit`
- `(%s) %s::%s: Failed to create PIO allocator dictionary\n`
- `\"%s: failed to create globalMapperProperties\" @%s:%d`
- `setParameter`
- `site.IODART::pageRange_t`
- `IODARTMapper`
- `_iovmInsertBatch`
- `setAllocator`
- `(%s) %s::%s: %s: failed to attach nub %p to DART %p\n`
- `vmReserve`
- `\"Invalid Direction %u \\n\" @%s:%d`
- `/IODARTMapper.cpp`
- `(%s) %s::%s: VM insert does not fit in VM Space %p - vsPageCount(%u) pageCount(%u)\n`
- `\"%s: Mapper not registered: 0x%08x\" @%s:%d`
- `121111121222121211122112111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222`
- `(%s) %s::%s: mapper has no allocations\n`
- `vmAllocReserved`
- `(%s) %s::%s: Failed to create PIO range allocator\n`
- `dart-segment-history`
- `site.IODARTVMSpace`
- `11122`
- `iomdEarlyPurge`
- `\"%s: dynamic mapper dictionary contains reserved '%s' property\" @%s:%d`
- `AAPL,phandle`
- `site.IODARTClient`
- `site.IODARTMapper`
- `site.IODARTMapper::pioRange_t`
- `iomdEarlyReclaim`
- `(%s) %s::%s: Failed to register mapper for SID %d: 0x%08x\n`
- `_iovmAllocDMACommand`
- `(%s) %s::%s: VM space does not contain DVA 0x%llx\n`
- `site.persistentMappings_t`
- `\"%s: VM space declined translation\" @%s:%d`
- `\"%s: SID %u persistent L2 entries must be within the first CTE, found %u L2 entries in CTE %p index %#x\" @%s:%d`
- `\"%s: Persistent mapping page limits [0x%lx..0x%lx) outside valid range [0x%lx..0x%lx)\" @%s:%d`
- `reg`
- `  %016llx`
- `/IODARTVMSpace.cpp`
- `IODARTMapperClient`
- `_isMapperReady`
- `_findVMSpace`
- `(%s) %s::%s: pio allocation request for inactive DART: %d pages IODC %p\n`
- `%s::%s: %s: failed to set %s property\n`
- `l%u-tt-%u`
- `_iomdCacheReclaimIsRunning`
- `/IODARTPrivate.h`
- `(%s) %s::%s: VM exhausted\n`
- `22222223312322`
- `%s:%u: REQUIRE failed`
- `111212`
- `121111121222121211`
- `(%s) %s::%s: Rejecting map request iodc=%p, iomd=%p, seglength=0x%llx length=0x%llx subpage mapping not supported by %s\n`
- `_iovmAllocPIO`
- `(%s) %s::%s: Allocated %d pages from page 0x%x in reserved DVA range [0x%016llx..0x%016llx)\n`
- `(%s) %s::%s: failed to allocate IOMD cache history buffer\n`
- `(%s) %s::%s: VM Space not found for remap %#x\n`
- `(%s) %s::%s: %s: failed to allocate dictionary\n`
- `/IODARTVMAllocator.cpp`
- `_mapClientBuffer`
- `111222232211`
- `range-size`
- `_iovmFreeDMACommand`
- `/IODARTClient.cpp`
- `cache-history-entries`
- `AddStringToDictionary`
- `(%s) %s::%s: PIO VM exhausted\n`
- `cacheFlushInactive`
- `\"%s: Request begin/end (0x%llx/0x%llx) not page aligned\" @%s:%d`
- `1211111111`
- `(%s) %s::%s: Failed to add PIO range allocator\n`
- `vm-force`
- `set-log-options`
- `site.IODART::capability_t`
- `12111112122212121111111111111121`
- `(%s) %s::%s: mapper not initialized\n`
- `(%s) %s::%s: allocation request for inactive DART: %d pages IODC %p\n`
- `dead-mappings`
- `_iovmInsert`
- `\"%s: failed to create mapper for mapper nub %p\" @%s:%d`
- `/IODARTMapperClient.cpp`
- `IODARTVMAllocator`
- `pt-region-%d`
- `real-time`
- `mapper-all`
- `mapper-protection-granularity`
- `dram-base`
- `(%s) %s::%s: Failed to increase batch segment allocation, max segs = 0x%llx\n`
- `(%s) %s::%s: %s: failed to set global mapper property: %s\n`
- `IODART.cpp`
- `allow-subpage-mapping`
- `\"%s: Mapper cannot be invoked with preemption disabled\" @%s:%d`
- `(%s) %s::%s: %s: failed to set iommu-parent %p in device %p -- terminating mapper nub %p\n`
- `IODARTVMSpace`
- `iommu-dart-identity`
- `site.IODARTMapperNub`
- `site.ppl_iommu_seg`
- `(%s) %s::%s: %s: no device\n`
- `(%s) %s::%s: %s: device %p already has an iommu-parent %p\n`
- `dart-all`
- `\"%s: VM space declined remap translation\" @%s:%d`
- `(%s) %s::%s: passed object %p is not IODARTVMAllocator\n`
- `site.IODARTPIOAllocatorGeneric`
- `\"%s: Incompatible DART interface: expected 0x%016llx actual 0x%016llx\" @%s:%d`
- `iomd-cache-size`
- `(%s) %s::%s: PIO region insufficent to hold more allocators\n`
- `tail-padding`
- `iovmMapMemory`
- `(%s) %s::%s: %s: failed to create mapper nub\n`
- `iommu-dart-dynamic`
- `111222232`
- `(%s) %s::%s: %s: failed to merge additional property dictionary %p\n`
- `site.IODART`
- `relaxed-rw-protections`
- `_errorHandlerUnregister`
- `destroyMapper`
- `(%s) %s::%s: failed to find VM space for DVA 0x%lx\n`
- `iommu-mapper`
- `(%s) %s::%s: PIO allocations are forever: ignoring free(0x%08x, 0x%08x)\n`
- `(%s) %s::%s: failed to get VM space for allocation at 0x%x\n`
- `IODARTPIOAllocatorGeneric`
- `iomd-early-reclaim`
- `IODART`
- `start`
- `IODARTMapper.cpp`
- `iommu-initial-translations`
- `(%s) %s::%s: mapper offline\n`
- `0x%016llx`
- `site.IODARTMapperClient`
- `121111111`
- `iomd-cache-wired-threshold`
- `(%s) %s::%s: %s: failed set %s property\n`
- `(%s) %s::%s: Insufficient buffer space: is 0x%08x, index 0x%08x\n`
- `(%s) %s:%u: VERIFY failed`
- `(%s) %s::%s: %s: failed to set %s property\n`
- `registerErrorHandler`
- `pio-range`
- `retrieveVMLimits`
- `range-base`
- `%s(%d): L%u(%d) page table @ %p:\n`
- `(%s) %s::%s: client_function=%p,%p clientObject=%p,%p clientOptions=%#llx,%#llx\n`
- `captureRegisters`
- `(%s) %s::%s: No VMSpace found for startAddress(%p)\n`
- `(%s) %s::%s: VM space declined translation at DVA 0x%llx\n`
- `callPlatformFunction`
- `/AllocGeneric.cpp`
- `copyAllocationInfo`
- `\"%s: Failed to allocate space for persistent mapping with page range [0x%lx..0x%lx)\" @%s:%d`
- `IODARTMapperNub`
- `11221`
- `iomd-cache-ttl`
- `_findVMSpaceReserved`
- `site.IODARTVMAllocatorGeneric`
- `mapper-history`
- `setIomdCacheAttribute`
- `\"%s: CE %p on unknown list 0x%08x\" @%s:%d`
- `(%s) %s:%u: REQUIRE failed`
- `_iomdCacheReclaimStop`
- `_setParameter`
- `dart-unmap-page-limit`
- `dart-mapper`
- `-cache`
- `/IODART.cpp`
- `(%s) %s::%s: free request at 0x%08x is not at the beginning of VM space %p [0x%08x..0x%08x)\n`
- `12111211213212122`
- `(%s) %s::%s: PIO allocations are forever: ignoring free(%p)\n`
- `(%s) %s::%s: result=%d,_reclaimScheduled=%d\n`
- `_iovmFree`
- `NewIODARTMapper`
- `(%s) %s::%s: Failed to DMA create range allocator\n`
- `site.ErrorHandlerEntry_t`
- `\"dead mapping {0x%08x 0x%08x} not found in vm space\" @%s:%d`
- `(%s) %s::%s: Map request failed (0x%08x) iodc=%p, iomd=%p, length=0x%llx\n`
- `(%s) %s::%s: failed to get VM space for allocation\n`
- `(%s) %s::%s: cannot make requested allocation at 0x%x/0x%x\n`
- `vmFree`
- `%s L%u(%d): %04X:`
- `iommu-dart-translation`
- `_addBatchSegment`
- `(%s) %s::%s: Failed to reserve [0x%x..0x%x)\n`
- `\"%s: pio-region %d not page aligned: 0x%016llx 0x%016llx\" @%s:%d`
- `numAllocations`
- `(%s) %s::%s: name missing for provider %p SID %d\n`
- `vmAlloc`
