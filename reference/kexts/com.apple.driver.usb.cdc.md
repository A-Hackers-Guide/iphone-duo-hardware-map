# `com.apple.driver.usb.cdc`

- Name: AppleUSBCDC
- Version: `5.0.0`
- UUID: `1A8D5481-F4BD-3A4B-831C-135908A741B7`
- Source version: `404.40.4.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](com.apple.driver.usb.AppleUSBHostCompositeDevice.md) 1.0, [`com.apple.driver.usb.networking`](com.apple.driver.usb.networking.md) 5.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (4) [KC]

### CDCCompositeDevice
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc`
- `IOClass`: `AppleUSBCDCCompositeDevice`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `2`
- `bDeviceProtocol`: `*`
- `bDeviceSubClass`: `*`

### CDCCompositeDevice Misc
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc`
- `IOClass`: `AppleUSBCDCCompositeDevice`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `239`
- `bDeviceProtocol`: `1`
- `bDeviceSubClass`: `2`

### CDCCompositeDevice Vendor
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc`
- `IOClass`: `AppleUSBCDCCompositeDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `0`
- `bDeviceProtocol`: `0`
- `bDeviceSubClass`: `0`

### Medtronics HeartWare VAD Controller
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc`
- `IOClass`: `AppleUSBCDCCompositeDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc`
- `IOProviderClass`: `IOUSBHostDevice`
- `idProduct`: `49163`
- `idVendor`: `7563`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBCDCCompositeDevice` | 0xd0 | AppleUSBHostCompositeDevice → IOService → IORegistryEntry |
| `AppleUSBCDCControl` | 0x138 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000859 off=0x008cf580-0x008cfdd9 addr=0xfffffe00078d3580-0xfffffe00078d3dd9 r--/r--   __TEXT            
	sz=0x00000281 off=0x008cfb58-0x008cfdd9 addr=0xfffffe00078d3b58-0xfffffe00078d3dd9               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000022f8 off=0x02b10fa0-0x02b13298 addr=0xfffffe0009b14fa0-0xfffffe0009b17298 r-x/r-x   __TEXT_EXEC       
	sz=0x00002158 off=0x02b10fa0-0x02b130f8 addr=0xfffffe0009b14fa0-0xfffffe0009b170f8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x02b130f8-0x02b13298 addr=0xfffffe0009b170f8-0xfffffe0009b17298          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049d0800-0x049d0928 addr=0xfffffe000b9d4800-0xfffffe000b9d4928 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049d0800-0x049d08c8 addr=0xfffffe000b9d4800-0xfffffe000b9d48c8               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9d48c8-0xfffffe000b9d4928               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000df0 off=0x012a1180-0x012a1f70 addr=0xfffffe00082a5180-0xfffffe00082a5f70 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012a1180-0x012a1190 addr=0xfffffe00082a5180-0xfffffe00082a5190         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012a1190-0x012a11a0 addr=0xfffffe00082a5190-0xfffffe00082a51a0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000c18 off=0x012a11a0-0x012a1db8 addr=0xfffffe00082a51a0-0xfffffe00082a5db8         __DATA_CONST.__const            
	sz=0x00000080 off=0x012a1db8-0x012a1e38 addr=0xfffffe00082a5db8-0xfffffe00082a5e38         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x012a1e38-0x012a1f08 addr=0xfffffe00082a5e38-0xfffffe00082a5f08         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000068 off=0x012a1f08-0x012a1f70 addr=0xfffffe00082a5f08-0xfffffe00082a5f70         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 65 at 0x04aeb490
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1A8D5481-F4BD-3A4B-831C-135908A741B7
008: LC_SOURCE_VERSION           404.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab72b8 size=0x50
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBCDC`
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBCDC`
- `CFBundleNumericVersion`: `83918848`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `5.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `5.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `5.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBCDC.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896560768`
- `_PrelinkExecutableRelativePath`: `AppleUSBCDC`
- `_PrelinkExecutableSize`: `14953`
- `_PrelinkExecutableSourceAddr`: `-2198896560768`
- `_PrelinkKmodInfo`: `-2198828398592`

## Strings (29) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `12111112122212121121121112`
- `sendMER`
- `%06lu.%06u %s::%s: new style matching\n`
- `Generic CDC`
- `AppleUSBCDCControl`
- `%06lu.%06u %s::%s: returning %d, INT EP 0x%x\n`
- `allocateResources`
- `kCDCDoNotMatchThisDevice`
- `UniqueIdentifier`
- `%06lu.%06u %s::%s: deviceRequest() bmRequestType %#x, bRequest %#x, result %#x\n`
- `site.AppleUSBCDCCompositeDevice`
- `WWANHardwareProperties`
- `DeviceModemOverrides`
- `site.AppleUSBCDCControl`
- `idProduct`
- `ModemSW`
- `DevicePPPOverrides`
- `Initializing`
- `idVendor`
- `AppleUSBCDCCompositeDevice`
- `USB Product Name`
- `AccessPointName`
- `WWANDynamicProperties`
- `kUSBPreferredConfiguration`
- `WWAN_TYPE`
- `LCPMTU`
- `openGated`
- `121111121222121211111121112112111122222`
- `cdc-ctrl-debug`
