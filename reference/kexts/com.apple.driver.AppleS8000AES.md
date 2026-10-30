# `com.apple.driver.AppleS8000AES`

- Name: AppleS8000AES
- Version: `1`
- UUID: `CC4C97F8-8818-38C2-9423-9062CEA09634`
- Source version: `140.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOCryptoAcceleratorFamily`](com.apple.iokit.IOCryptoAcceleratorFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) | `AppleS8000AESAccelerator` | `aes,s8000` |

## IOKit personalities (1) [KC]

### AppleS8000AES
- `CFBundleIdentifier`: `com.apple.driver.AppleS8000AES`
- `IOClass`: `AppleS8000AESAccelerator`
- `IONameMatch`: `aes,s8000`
- `IOPersonalityPublisher`: `com.apple.driver.AppleS8000AES`
- `IOPlatformQuiesceAction`: `80000`
- `IOPlatformWakeAction`: `80000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleS8000AESAccelerator` | 0xa00 | IOAESAccelerator → IOCryptoAccelerator → IOService → IORegistryEntry |
| `IOAppleS8000AESAcceleratorCommand` | 0x40 | IOCommand |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001a24 off=0x006d3fc0-0x006d59e4 addr=0xfffffe00076d7fc0-0xfffffe00076d99e4 r--/r--   __TEXT            
	sz=0x00000008 off=0x006d4638-0x006d4640 addr=0xfffffe00076d8638-0xfffffe00076d8640               __TEXT.__const            
	sz=0x000013a4 off=0x006d4640-0x006d59e4 addr=0xfffffe00076d8640-0xfffffe00076d99e4               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000434c off=0x0247d130-0x0248147c addr=0xfffffe0009481130-0xfffffe000948547c r-x/r-x   __TEXT_EXEC       
	sz=0x0000414c off=0x0247d130-0x0248127c addr=0xfffffe0009481130-0xfffffe000948527c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000200 off=0x0248127c-0x0248147c addr=0xfffffe000948527c-0xfffffe000948547c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000268 off=0x0498ffc8-0x04990230 addr=0xfffffe000b993fc8-0xfffffe000b994230 rw-/rw-   __DATA            
	sz=0x00000200 off=0x0498ffc8-0x049901c8 addr=0xfffffe000b993fc8-0xfffffe000b9941c8               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9941c8-0xfffffe000b994228               __DATA.__common           (Zerofill)
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000b994228-0xfffffe000b994230               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000970 off=0x011c21d0-0x011c2b40 addr=0xfffffe00081c61d0-0xfffffe00081c6b40 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x011c21d0-0x011c21d8 addr=0xfffffe00081c61d0-0xfffffe00081c61d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x011c21d8-0x011c21e0 addr=0xfffffe00081c61d8-0xfffffe00081c61e0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000790 off=0x011c21e0-0x011c2970 addr=0xfffffe00081c61e0-0xfffffe00081c6970         __DATA_CONST.__const            
	sz=0x00000080 off=0x011c2970-0x011c29f0 addr=0xfffffe00081c6970-0xfffffe00081c69f0         __DATA_CONST.__kalloc_type      
	sz=0x00000100 off=0x011c29f0-0x011c2af0 addr=0xfffffe00081c69f0-0xfffffe00081c6af0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x011c2af0-0x011c2b40 addr=0xfffffe00081c6af0-0xfffffe00081c6b40         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 74 at 0x04ae3674
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     CC4C97F8-8818-38C2-9423-9062CEA09634
008: LC_SOURCE_VERSION           140.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aaec20 size=0x88
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleS8000AES`
- `CFBundleIdentifier`: `com.apple.driver.AppleS8000AES`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleS8000AES`
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
- `NSHumanReadableCopyright`: `Copyright © 2013 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleS8000AES.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898638912`
- `_PrelinkExecutableRelativePath`: `AppleS8000AES`
- `_PrelinkExecutableSize`: `26952`
- `_PrelinkExecutableSourceAddr`: `-2198898638912`
- `_PrelinkKmodInfo`: `-2198828662840`

## Strings (101) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleS8000AESAccelerator`
- `NULL != (_aesMemoryMap = _aesProvider->mapDeviceMemoryWithIndex(0))`
- `NULL != (_aesDisableKeyMap = _aesProvider->mapDeviceMemoryWithIndex(1))`
- `0 != (_aesDKeyAddr = _aesDKeyMap->getVirtualAddress())`
- `wait-for`
- `\"AppleS8000AESAccelerator: AppleS8000AESAccelerator failed to register with IOAESAccelerator\" @%s:%d`
- `!_enabled`
- `%s: WARNING: AppleS8000AESAccelerator::bad descrambler configuration\n`
- `AppleS8000AES::start: dkey phys:0x%#lx virt:0x%#lx\n`
- `IOReturn AppleS8000AESAccelerator::_configureAES(IOAESAcceleratorCommand *, UInt32)`
- `void AppleS8000AESAccelerator::_completeAES()`
- `bool AppleS8000AESAccelerator::_isKeyDisabled(UInt32)`
- `AppleS8000AES.h`
- `AppleS8000AES::start: aes-version: %d\n`
- `address-width`
- `AppleS8000AES::start: address-width: %d\n`
- `NULL != (_aesDKeyMap = _aesProvider->mapDeviceMemoryWithIndex(2))`
- `kIOReturnSuccess == _iv_dma->setMemoryDescriptor(_iv_bounce)`
- `length >= sizeof(sw_input)`
- `UInt32 AppleS8000AESAccelerator::_keySelectionForHandle(UInt32)`
- `%s: WARNING: AppleS8000AESAccelerator::attempt to disable unsuported key %u\n`
- `IOHibernateState`
- `aes-version`
- `%s: WARNING: AppleS8000AESAccelerator::bad configuration for IOAESOperationH16Scrambler operation\n`
- `dmaCMD->command`
- `sioaesdisablegid0-offset`
- `_space_available(size)`
- `%s: WARNING: Unknown key size: %d\n\n`
- `UInt32 AppleS8000AESAccelerator::_key_size(UInt8)`
- `NULL != _interruptEventSource`
- `virtual void AppleS8000AESAccelerator::stop(IOService *)`
- `_enabled`
- `\"dmaDST %016llx %p %d\" @%s:%d`
- `%s: WARNING: AppleS8000AESAccelerator::attempt to look up unsuported key %u\n`
- `\"Length of the devicetree property (%s) is unexpected (expected : %d byte , result: %d byte\" @%s:%d`
- `void AppleS8000AESAccelerator::_push_command(void *, UInt32)`
- `AES_COMMAND: %08x\n`
- `\"AppleS8000AESAccelerator::_enableAES: DPA has not been seeded!\" @%s:%d`
- `\"AppleS8000AESAccelerator::performAESQuantum: Unknown Operation %d\" @%s:%d`
- `void AppleS8000AESAccelerator::_interruptOccurred(IOInterruptEventSource *, int)`
- `NULL != _iv_dma`
- `virtual IOReturn AppleS8000AESAccelerator::performAESQuantum(IOAESAcceleratorCommand *)`
- `plainText != NULL`
- `cipherText != NULL`
- `!queue_empty(&_commandQueue)`
- `sioaesdisable-offset`
- `cmac != NULL`
- `AppleS8000AES.cpp`
- `segments[0].fLength == IV_BOUNCE_SIZE`
- `length >= sizeof(response)`
- `yes`
- `-ignore_dpa`
- `_commandsInFlight == 0`
- `bool AppleS8000AESAccelerator::_push_command_key(UInt32, UInt32, UInt8 *, UInt8 *, bool)`
- `/Library/Caches/com.apple.xbs/8911E14A-B25D-456E-A744-490BCC8D7CAC/TemporaryDirectory.4BNA3C/Sources/AppleS8000/AppleS8000AES.cpp`
- `virtual bool AppleS8000AESAccelerator::start(IOService *)`
- `%s: WARNING: AppleS8000AESAccelerator::operation with no key data\n`
- `srcDMA != NULL`
- `_commandsInFlight > 0`
- `Couldn't find %s from DeviceTree to override\n`
- `\"%s:%s:%u: REQUIRE failed: %s\" @%s:%d`
- `AppleS8000AES::start: registers at phys:0x%#lx/0x%#lx virt:0x%#lx/0x%#lx / 0x%#lx/0x%#lx\n`
- `use-auto-gating`
- `kIOReturnSuccess == _iv_dma->genIOVMSegments(&offset, &segments, &numSegments)`
- `%s: WARNING: AppleS8000AESAccelerator::bad wrapped key configuration\n`
- `AppleS8000AESAccelerator: WARNING: DPA is not seeded, but not panicking!\n`
- `%s: WARNING: AppleS8000AESAccelerator::unsupported operation %u\n`
- `\"AppleS8000AESAccelerator::Wrapped Key Policy is undefined\" @%s:%d`
- `IOAppleS8000AESAcceleratorCommand`
- `0 != (_aesDisableKeyAddr = _aesDisableKeyMap->getVirtualAddress())`
- `service-gates`
- `-aes_spew`
- `NULL != (_commandGate = IOCommandGate::commandGate(this))`
- `\"AppleS8000AESAccelerator::Powering Down AES Block while Commands still in FIFO.\" @%s:%d`
- `dmaCMD != nullptr`
- `dstDMA != NULL`
- `site.AppleS8000AESAccelerator`
- `AppleS8000AES::start: using-acg: %s\n`
- `AppleS8000AES::start: using DART Mapper: %p\n`
- `index < MAX_IV_INDEX`
- `\"AppleS8000AESAccelerator::_distribute_dkey: DKey distribution failure (aes-version=%u)\" @%s:%d`
- `0 != (_aesBaseAddress = _aesMemoryMap->getVirtualAddress())`
- `121111121222121212212221121222111121122111212211111111211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `12111112`
- `NULL != _iv_bounce`
- `void AppleS8000AESAccelerator::_enableAES(bool)`
- `%s: WARNING: AppleS8000AESAccelerator::bad IOAESH16Descrambler configuration\n`
- `%s: WARNING: AppleS8000AESAccelerator::unsupported key %u\n`
- `void AppleS8000AESAccelerator::_handleIVBounce(IOAESIV *, UInt16)`
- `no`
- `\"dmaSRC %016llx %p %d\" @%s:%d`
- `virtual void AppleS8000AESAccelerator::disableHardwareKey(UInt32)`
- `sioaesdisableuid1-offset`
- `sioaesdisablegid1-offset`
- `/Library/Caches/com.apple.xbs/8911E14A-B25D-456E-A744-490BCC8D7CAC/TemporaryDirectory.4BNA3C/Sources/AppleS8000/AppleS8000AES.h`
- `bool AppleS8000AESAccelerator::_space_available(UInt32)`
- `size % sizeof(UInt32) == 0`
- `site.IOAppleS8000AESAcceleratorCommand`
- `%s: WARNING: AppleS8000AESAccelerator::bad LegacySKG configuration\n`
- `%s: WARNING: AppleS8000AESAccelerator::bad operation for kIOAESAcceleratorKeyHandleScrambledH16 configuration\n`
- `\"AppleS8000AESAccelerator::AES Error: IntStatus 0x%#x\\n\" @%s:%d`
