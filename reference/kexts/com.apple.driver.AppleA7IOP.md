# `com.apple.driver.AppleA7IOP`

- Name: AppleA7IOP
- Version: `1.0.2`
- UUID: `5C9CB667-1A6E-32F7-AEB0-13C47479C08D`
- Source version: `342.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleA7IOP` | 0x188 | AppleIOP → IOSlaveCPU → IOService → IORegistryEntry |
| `AppleA7IOPNub` | 0x98 | IOService → IORegistryEntry |
| `AppleIOP` | 0xf0 | IOSlaveCPU → IOService → IORegistryEntry |
| `AppleWrapperMailbox` | 0x160 | AppleIOP → IOSlaveCPU → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001583 off=0x0014eb80-0x00150103 addr=0xfffffe0007152b80-0xfffffe0007154103 r--/r--   __TEXT            
	sz=0x00000fab off=0x0014f158-0x00150103 addr=0xfffffe0007153158-0xfffffe0007154103               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000064c8 off=0x01668b80-0x0166f048 addr=0xfffffe000866cb80-0xfffffe0008673048 r-x/r-x   __TEXT_EXEC       
	sz=0x000061b8 off=0x01668b80-0x0166ed38 addr=0xfffffe000866cb80-0xfffffe0008672d38          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000310 off=0x0166ed38-0x0166f048 addr=0xfffffe0008672d38-0xfffffe0008673048          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000178 off=0x0492e218-0x0492e390 addr=0xfffffe000b932218-0xfffffe000b932390 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0492e218-0x0492e2e0 addr=0xfffffe000b932218-0xfffffe000b9322e0               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000b9322e0-0xfffffe000b932390               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001f78 off=0x00f92f80-0x00f94ef8 addr=0xfffffe0007f96f80-0xfffffe0007f98ef8 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x00f92f80-0x00f92fa0 addr=0xfffffe0007f96f80-0xfffffe0007f96fa0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x00f92fa0-0x00f92fc0 addr=0xfffffe0007f96fa0-0xfffffe0007f96fc0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001c60 off=0x00f92fc0-0x00f94c20 addr=0xfffffe0007f96fc0-0xfffffe0007f98c20         __DATA_CONST.__const            
	sz=0x00000100 off=0x00f94c20-0x00f94d20 addr=0xfffffe0007f98c20-0xfffffe0007f98d20         __DATA_CONST.__kalloc_type      
	sz=0x00000188 off=0x00f94d20-0x00f94ea8 addr=0xfffffe0007f98d20-0xfffffe0007f98ea8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x00f94ea8-0x00f94ef8 addr=0xfffffe0007f98ea8-0xfffffe0007f98ef8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 108 at 0x04ad0f60
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     5C9CB667-1A6E-32F7-AEB0-13C47479C08D
008: LC_SOURCE_VERSION           342.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004a96600 size=0x148
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleA7IOP`
- `CFBundleIdentifier`: `com.apple.driver.AppleA7IOP`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleA7IOP`
- `CFBundleNumericVersion`: `16941056`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2011-2014 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleA7IOP.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904427648`
- `_PrelinkExecutableRelativePath`: `AppleA7IOP`
- `_PrelinkExecutableSize`: `39739`
- `_PrelinkExecutableSourceAddr`: `-2198904427648`
- `_PrelinkKmodInfo`: `-2198829063656`

## Strings (106) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `_akfAction != nullptr`
- `kIOReturnSuccess == ret`
- `0 != akfPhysicalAddress`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `site.AppleA7IOPNub`
- `force-timebase-sync`
- `initialize()`
- `kIOReturnSuccess == _enablePowerLate()`
- `Outbox`
- `virtual bool AppleWrapperMailbox::start(IOService *)`
- `AP->IOP Mailbox Log:\nTimestamp          | Dir  | Message\n`
- `TX`
- `site.AppleA7IOP`
- `role`
- `ignore-mailboxes`
- `AppleA7IOP(%s):WARNING: dart-map-firmware-debug-only is a debug only setting and should not be set in a normal build\n`
- `nullptr != _akfRegisterMap`
- `site.AppleIOP`
- `AppleA7IOP.cpp`
- `_autoBootRegisterMap != nullptr`
- `truncate-dvas`
- `AppleA7IOPNub: %s, %d: allocated nub %p\n\n`
- `virtual IOReturn AppleWrapperMailbox::getMailboxBulk(void *, unsigned int *)`
- ` %#018llx`
- `auto-boot`
- `cpu-ctrl-filtered`
- `dmaAddress <= real_start`
- `\"%s Overflow/Underflow: %08x\" @%s:%d`
- `size >= index`
- `function-device_reset`
- `real_start >= dart_vm_base`
- `virtual IOPhysicalAddress AppleA7IOP::getWrapperPhysicalAddress()`
- `\"%s\" @%s:%d`
- `12111112122212121112221111121211121122222111`
- `%#018llx %#018llx | [%s] |`
- `RX`
- `AppleA7IOP(%s):WARNING: timeout overrode to %ds\n`
- `retrieveVMLimits`
- `IODMACommand *AppleA7IOP::_dartMapMemoryDescriptor(IOMapper *, IOMemoryDescriptor *, IOPhysicalAddress *)`
- `_running()`
- `IODARTMapper`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `AppleA7IOP`
- `\"%s:%s:%u REQUIRE failed: %s\" @%s:%d`
- `dart-map-firmware-debug-only`
- `real_extent <= dart_vm_base + dart_vm_size`
- `virtual bool AppleA7IOP::_outboxHandler(IOInterruptEventSource *)`
- `virtual IOReturn AppleA7IOP::postMailbox(UInt32, void *, UInt32, bool)`
- `/Library/Caches/com.apple.xbs/AABFBD85-A37C-455C-9336-D4CF01B07B8C/TemporaryDirectory.eyQ48x/Sources/AppleA7IOP/AppleIOPBufferWriter.cpp`
- `void AppleIOPBufferWriter::write(const char *, ...)`
- `a7iop_enable_timeout`
- `tempData->getLength() >= 4`
- `void AppleA7IOP::_dartMapiBootFirmware(IOMapper *)`
- `nullptr != command`
- `OSBoundedPtr.h`
- `virtual bool AppleWrapperMailbox::setDoorbellAction(IOSlaveCPU::DoorbellAction, OSObject *, void *, UInt32)`
- `121111121222121211122211111212`
- `_akfRegisterMap != nullptr`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `AppleWrapperMailbox`
- `_akfMappedRegs != 0`
- `post-retry-freq`
- `AppleA7IOP(%s):WARNING: CPU already running\n`
- `__PRETTY_FUNCTION__ \": Expected stopCPU to be called first\" @%s:%d`
- `1211111212221212111`
- `(_akfLock != nullptr) && (_akfInboxLock != nullptr) && (_akfOutboxLock != nullptr)`
- `ignore-gating`
- `should-control-sram`
- `\"%s failed to become idle (0x%08x) in %dms\" @%s:%d`
- `virtual bool AppleA7IOP::setDoorbellAction(IOSlaveCPU::DoorbellAction, OSObject *, void *, UInt32)`
- `mailboxItem != nullptr`
- `_akfProvider != nullptr`
- `unknown`
- `segment-ranges`
- `_inboxFilter != nullptr`
- `no-activate-mapper`
- `doorbellIndex == 0`
- `AppleA7IOPNub: %s, %d: provider is not AKFProvider\n\n`
- `virtual IOPhysicalAddress AppleWrapperMailbox::getWrapperPhysicalAddress()`
- `/Library/Caches/com.apple.xbs/AABFBD85-A37C-455C-9336-D4CF01B07B8C/TemporaryDirectory.eyQ48x/Sources/AppleA7IOP/AppleA7IOP.cpp`
- `cpu-run-timestamp`
- `_autoBootMappedRegs != 0`
- `sram-index`
- `virtual IOReturn AppleA7IOP::startCPUWithOptions(IOSlaveFirmware *, IOOptionBits)`
- `result == kIOReturnSuccess`
- `AppleA7IOP(%s):WARNING: spurious ringDoorbell call\n`
- `mailboxItemCount != nullptr`
- `_outboxFilter != nullptr`
- `__PRETTY_FUNCTION__ \": Not implmented\" @%s:%d`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `withRegistryEntry`
- `AppleA7IOPNub: %s, %d: failed to init nub\n\n`
- `AppleIOPBufferWriter.cpp`
- `site.AppleWrapperMailbox`
- `\n`
- `\"%s unexpected stopCPU arguments %d %d\" @%s:%d`
- `dmaAddress + dmaLength >= real_extent`
- `virtual IOReturn AppleA7IOP::getMailboxBulk(void *, unsigned int *)`
- `Inbox`
- `AppleA7IOPNub`
- `virtual bool AppleWrapperMailbox::_outboxHandler(IOInterruptEventSource *)`
- `AppleIOP`
- ` Interrupt\n`
- `setActive`
- `1211111212221212111222111112121112112121122222111`
- `virtual bool AppleA7IOP::start(IOService *)`
