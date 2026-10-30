# `com.apple.driver.AppleMobileApNonce`

- Name: AppleMobileApNonce
- Version: `1`
- UUID: `AC81CF9F-3DE3-32FD-A80C-D22C564E03CC`
- Source version: `55.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.0, [`com.apple.iokit.IOCryptoAcceleratorFamily`](com.apple.iokit.IOCryptoAcceleratorFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/defaults`](../devicetree/root__defaults.md) | `AppleMobileApNonce` | `defaults` |

## IOKit personalities (1) [KC]

### AppleMobileApNonceNVRAM
- `CFBundleIdentifier`: `com.apple.driver.AppleMobileApNonce`
- `IOClass`: `AppleMobileApNonce`
- `IONameMatch`: `defaults`
- `IOPersonalityPublisher`: `com.apple.driver.AppleMobileApNonce`
- `IOProviderClass`: `IOPlatformDevice`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleMobileApNonce` | 0xe8 | IOService → IORegistryEntry |
| `AppleMobileApNonceUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002042 off=0x00665440-0x00667482 addr=0xfffffe0007669440-0xfffffe000766b482 r--/r--   __TEXT            
	sz=0x00001961 off=0x00665b08-0x00667469 addr=0xfffffe0007669b08-0xfffffe000766b469               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000012 off=0x00667470-0x00667482 addr=0xfffffe000766b470-0xfffffe000766b482               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00003fc4 off=0x0226ac60-0x0226ec24 addr=0xfffffe000926ec60-0xfffffe0009272c24 r-x/r-x   __TEXT_EXEC       
	sz=0x00003c74 off=0x0226ac60-0x0226e8d4 addr=0xfffffe000926ec60-0xfffffe00092728d4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000350 off=0x0226e8d4-0x0226ec24 addr=0xfffffe00092728d4-0xfffffe0009272c24          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000130 off=0x04979660-0x04979790 addr=0xfffffe000b97d660-0xfffffe000b97d790 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04979660-0x04979728 addr=0xfffffe000b97d660-0xfffffe000b97d728               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b97d728-0xfffffe000b97d788               __DATA.__common           (Zerofill)
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000b97d788-0xfffffe000b97d790               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000f10 off=0x0116c8b8-0x0116d7c8 addr=0xfffffe00081708b8-0xfffffe00081717c8 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x0116c8b8-0x0116c8c8 addr=0xfffffe00081708b8-0xfffffe00081708c8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x0116c8c8-0x0116c8d8 addr=0xfffffe00081708c8-0xfffffe00081708d8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000c70 off=0x0116c8d8-0x0116d548 addr=0xfffffe00081708d8-0xfffffe0008171548         __DATA_CONST.__const            
	sz=0x00000080 off=0x0116d548-0x0116d5c8 addr=0xfffffe0008171548-0xfffffe00081715c8         __DATA_CONST.__kalloc_type      
	sz=0x000001a8 off=0x0116d5c8-0x0116d770 addr=0xfffffe00081715c8-0xfffffe0008171770         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x0116d770-0x0116d7c0 addr=0xfffffe0008171770-0xfffffe00081717c0         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x0116d7c0-0x0116d7c8 addr=0xfffffe00081717c0-0xfffffe00081717c8         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 116 at 0x04adf528
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     AC81CF9F-3DE3-32FD-A80C-D22C564E03CC
008: LC_SOURCE_VERSION           55.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aaa738 size=0x88
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleMobileApNonce`
- `CFBundleIdentifier`: `com.apple.driver.AppleMobileApNonce`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleMobileApNonce`
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
- `NSHumanReadableCopyright`: `Copyright © 2012, 2015-2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleMobileApNonce.kext`
- `_PrelinkExecutableLoadAddr`: `-2198899092416`
- `_PrelinkExecutableRelativePath`: `AppleMobileApNonce`
- `_PrelinkExecutableSize`: `28742`
- `_PrelinkExecutableSourceAddr`: `-2198899092416`
- `_PrelinkKmodInfo`: `-2198828755360`

## Strings (159) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s%s:\n%s    can't allocate buffers\n`
- `AppleMobileApNonce`
- `crypto-hash-method`
- `fail`
- `%s%s:\n%s    calling _saveNonceInfoInNVRAM\n`
- `%s%s:\n%s    Unable to save nonce: 0x%08X\n`
- `static void AppleMobileApNonce::_printNonceAndHash(uint64_t, const void *, size_t)`
- `%s%s:\n%s    %s: Couldn't find a free nonce slot to use: %08x (%s)\n\n`
- `IONVRAM`
- `%s%s:\n%s    called _clearNonceInfoFromNVRAM\n`
- `%s%s:\n%s    leaving: 0x%X %p\n`
- `%s%s:\n%s    AMAN starting\n`
- `%s%s:\n%s    got _restore_boot = %d\n`
- `IOCommandGate *AppleMobileApNonce::_getCommandGate()`
- `IOReturn AppleMobileApNonce::_saveNonceGated(const char *)`
- `%s%s:\n%s    Nonce string was null\n`
- `%s%s:\n%s    bug in kext matching\n`
- `%s%s:\n%s    closed\n`
- `%s%s:\n%s    nonce slot ID not found\n`
- `%s%s:\n%s    %s: unable allocate hash buffer: %08x (%s)\n\n`
- `IOReturn AppleMobileApNonce::_generateNonceHash(uint64_t, uint8_t *)`
- `IODTNVRAM`
- `IOReturn AppleMobileApNonce::_readNonceGated(OSString **)`
- `%s%s:\n%s    _readNonce done: 0x%X (%s)\n\n`
- `success`
- `IOReturn AppleMobileApNonce::_retrieveNonce(uint64_t *)`
- `%s%s:\n%s    Waiting for IODTNVRAM\n`
- `%s:%u: REQUIRE failed`
- `%s%s:\n%s    start: _sandcatSupported=%d\n`
- `%s%s:\n%s    RL boot detected.\n`
- `%s%s:\n%s    deleting old nonce in slot %d\n`
- `%s%s:\n%s    retrieveNonce _allowApNonceRetrieval: %d\n`
- `%s%s:\n%s    _pickNewNonceSlot: found the slot %s, picked new slot id=%d\n`
- `0x%016llx`
- `site.AppleMobileApNonceUserClient`
- `ERROR: `
- `allow-ap-nonce-retrieval`
- `\"Timeout waiting for AES accelerator service\" @%s:%d`
- `%s%s:\n%s    _clearNonceInfoFromNVRAM done: 0x%X\n`
- `%s%s:\n%s    _readNonce: nonce(bncn) 0x%016llX\n`
- `%s%s:\n%s    nonce slot ID not supported\n`
- `%s%s:\n%s    Waiting for IONVRAM\n`
- `%s%s:\n%s    calling _readNonceFromNVRAM\n`
- `void AppleMobileApNonce::_readNonceFromNVRAM(OSString **)`
- `virtual IOReturn AppleMobileApNonceUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `IOReturn AppleMobileApNonce::generateNonce(void *, size_t *)`
- `%s%s:\n%s    possible update in flight, cleanup skipped.\n`
- `%s%s:\n%s    _pickNewNonceSlot: found booted slot failed\n`
- `%s%s:\n%s    %s: unable read nonce: %08x (%s)\n\n`
- `%s%s:\n%s    start: _entangleNonce=%d\n`
- `IOReturn AppleMobileApNonce::_readNonce(OSString **)`
- `%s%s:\n%s    bad selector %u\n`
- `12111112122212121111111112212`
- `INFO: `
- `sha1`
- `SPEW: `
- `IOReturn AppleMobileApNonce::getSlotID(uint32_t *)`
- `%s%s:\n%s    %s: invalid nonce %s, residue = %p (%d)\n\n`
- `%s%s:\n%s    _readNonceFromNVRAM done: 0x%X\n`
- `GenerateNonce`
- `SEPApNonce *AppleMobileApNonce::_getSEPApNonce()`
- `_generateNonce`
- `%s%s:\n%s    _readNonce: _sandcatSupported=%d\n`
- `%s%s:\n%s    leaving: 0x%X\n`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:com.apple.System.boot-nonce`
- `AppleMobileApNonceUserClient`
- `INIT: `
- `void AppleMobileApNonce::_cleanupNonceSlots()`
- `%s%s:\n%s    super failed to start\n`
- `%s%s:\n%s    bad output struct\n`
- `%s%s:\n%s    _saveNonceInfoInNVRAM done: 0x%X\n`
- `%s%s:\n%s    _readNonce get slot info: possible_proposed_nonce_slot_state=%d, possible_proposed_nonce_slot_id=%d\n`
- `void AppleMobileApNonce::_saveNonceInfoInNVRAM(const char *)`
- `%s%s:\n%s    NVRAM was null\n`
- `void AppleMobileApNonce::_startupTasks()`
- `%s%s:\n%s    nonce previously generated\n`
- `void AppleMobileApNonce::_waitForNVRAMReadable()`
- `%s%s:\n%s    started\n`
- `%s%s:\n%s    start: _restoreBoot=%d\n`
- `%s%s:\n%s    start: _allowApNonceRetrieval=%d\n`
- `%s%s:\n%s    %s: hash mismatch\n\n`
- `%s%s:\n%s    promoting nonce in slot %d\n`
- `%s%s:\n%s    nonce generated\n`
- `%s%s:\n%s    Got IONVRAM\n`
- `IOReturn AppleMobileApNonce::_saveNonce(const char *)`
- `%s%s:\n%s    not authorized\n`
- `%s%s:\n%s    super did not start\n`
- `sha2-384`
- `AppleMobileApNonce.cpp`
- `%s%s:\n%s    couldn't acquire command gate\n`
- `%s%s:\n%s    _pickNewNonceSlot: found booted slot id %d, state =%d\n`
- `%s%s:\n%s    _readNonce: get booted slot failed\n`
- `/arm-io/sep/iop-sep-nub/Sandcat`
- `entangle-nonce`
- `%s%s:\n%s    %s: nonce entanglement failed: %08x (%s)\n\n`
- `%s%s:\n%s    Got IODTNVRAM\n`
- `IOReturn AppleMobileApNonce::_clearNonceGated()`
- `%s%s:\n%s    entering\n`
- `aes-service-publish-timeout`
- `\"Invalid crypto hash method: %d\" @%s:%d`
- `%s%s:\n%s    _readNonce: failed because SEP is not up\n`
- `%s%s:\n%s    _readNonce: return string %p, nonce_string %s\n`
- `%s%s:\n%s    _startupTasks to _cleanupNonceSlots\n`
- `virtual void AppleMobileApNonce::registerService(IOOptionBits)`
- `sidp-rom-manifest-hash`
- `%s%s:\n%s    %s: unable save nonce: %08x (%s)\n\n`
- `%s%s:\n%s    called _readNonceFromNVRAM\n`
- `%s%s:\n%s    _readNonce call _getCommandGate action: 0x%X\n`
- `/chosen`
- `%s%s:\n%s    generating nonce in slot %d\n`
- `%s%s:\n%s    %s: unable to prepare input buffer: %08x (%s)\n\n`
- `1211111212221212111111111111`
- `seeker-restore`
- `%s%s:\n%s    thread_call_allocate failed\n`
- `IOReturn AppleMobileApNonce::retrieveNonce(void *, size_t *)`
- `%s%s:\n%s    Nonce: 0x%016llX\n`
- `%s%s:\n%s    %s: unable to prepare output buffer: %08x (%s)\n\n`
- `void AppleMobileApNonce::_waitForSandcatInit()`
- `IOReturn AppleMobileApNonce::_clearNonce()`
- `CLIENT: `
- `IOAESAccelerator`
- `%s%s:\n%s    bad output argument\n`
- `%s%s:\n%s    retrieveNonce done: 0x%X\n`
- `0x%02x`
- `%s%s:\n%s    %s: no nonce\n\n`
- `%s%s:\n%s    %s: nonce length %d expected %zu\n\n`
- `void AppleMobileApNonce::_waitForNVRAMWritable()`
- `virtual IOReturn AppleMobileApNonceUserClient::clientClose()`
- `%s%s:\n%s    couldn't init work loop\n`
- `%s%s:\n%s    L boot detected.\n`
- `%s%s:\n%s    retrieveNonce assign result to kIOReturnNotPermitted\n`
- `bool AppleMobileApNonce::_getBootedSlotAndState(uint8_t *, uint8_t *)`
- `%s%s:\n%s    _getBootedSlotAndState: current_slot_state=%d, current_slot_id=%d\n`
- `IOReturn AppleMobileApNonce::_generateNonce(void *, size_t *)`
- `%s%s:\n%s    raw nonce: 0x%016llx  plaintext 0x%016llx%016llx\n`
- `%s%s:\n%s    start: _cryptoHashMethod=%d\n`
- `%s%s:\n%s    Timeout waiting for AES accelerator service\n`
- `%s%s:\n%s    Unable to create OSString value object\n`
- `_generateNonceHash`
- `%s%s:\n%s    raw nonce: 0x%016llx  ciphertext 0x%016llx%016llx\n`
- `%s%s:\n%s    called _saveNonceInfoInNVRAM\n`
- `IONVRAM-FORCESYNCNOW-PROPERTY`
- `%s%s:\n%s    Bad input\n`
- `%s%s:\n%s    start: aes-service-publish-timeout %llu seconds\n`
- `%s%s:\n%s    Hash: %s\n`
- `virtual bool AppleMobileApNonceUserClient::start(IOService *)`
- `virtual bool AppleMobileApNonce::start(IOService *)`
- `%s%s:\n%s    _getBootedSlotAndState: booted slot id = %d\n`
- `_retrieveNonce`
- `%s%s:\n%s    calling _clearNonceInfoFromNVRAM\n`
- `void AppleMobileApNonce::_clearNonceInfoFromNVRAM()`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:anid`
- `site.AppleMobileApNonce`
- `%s%s:\n%s    booting to ramdisk, skipping nonce cleanup.\n`
- `%s%s:\n%s    _getBootedSlotAndState: look up sidp-rom-manifest-hash failed\n`
- `%s%s:\n%s    Invalid nonce string length\n`
- `root`
- `IOReturn AppleMobileApNonce::_pickNewNonceSlot(uint8_t *)`
- `%s%s:\n%s    %s: unable to hash nonce: %08x (%s)\n\n`
