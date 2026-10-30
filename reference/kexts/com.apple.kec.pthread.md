# `com.apple.kec.pthread`

- Name: pthread
- Version: `1`
- UUID: `0AC2C136-E10C-326B-84B4-BD01406C7AB0`
- Source version: `553.40.2.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 12.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 13.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 11.2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 11.2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 11.2, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 11.2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (0) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 11 (Size: 1512)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, DylibInCache
000: LC_SEGMENT_64 sz=0x00000dbd off=0x001170a0-0x00117e5d addr=0xfffffe000711b0a0-0xfffffe000711be5d r--/r--   __TEXT            
	sz=0x00000040 off=0x001176f0-0x00117730 addr=0xfffffe000711b6f0-0xfffffe000711b730               __TEXT.__const            
	sz=0x0000072d off=0x00117730-0x00117e5d addr=0xfffffe000711b730-0xfffffe000711be5d               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000067a8 off=0x01513990-0x0151a138 addr=0xfffffe0008517990-0xfffffe000851e138 r-x/r-x   __TEXT_EXEC       
	sz=0x00006438 off=0x01513990-0x01519dc8 addr=0xfffffe0008517990-0xfffffe000851ddc8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000370 off=0x01519dc8-0x0151a138 addr=0xfffffe000851ddc8-0xfffffe000851e138          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000198 off=0x049240e0-0x04924278 addr=0xfffffe000b9280e0-0xfffffe000b928278 rw-/rw-   __DATA            
	sz=0x0000013c off=0x049240e0-0x0492421c addr=0xfffffe000b9280e0-0xfffffe000b92821c               __DATA.__data             
	sz=0x00000021 off=0x00000000-0x00000021 addr=0xfffffe000b928220-0xfffffe000b928241               __DATA.__bss              (Zerofill)
	sz=0x00000030 off=0x00000000-0x00000030 addr=0xfffffe000b928248-0xfffffe000b928278               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000648 off=0x00f68000-0x00f68648 addr=0xfffffe0007f6c000-0xfffffe0007f6c648 rw-/rw-   __DATA_CONST      
	sz=0x000003f8 off=0x00f68000-0x00f683f8 addr=0xfffffe0007f6c000-0xfffffe0007f6c3f8         __DATA_CONST.__const            
	sz=0x00000008 off=0x00f683f8-0x00f68400 addr=0xfffffe0007f6c3f8-0xfffffe0007f6c400         __DATA_CONST.__weak_got         (NonLazySymbolPointers)
	sz=0x00000080 off=0x00f68400-0x00f68480 addr=0xfffffe0007f6c400-0xfffffe0007f6c480         __DATA_CONST.__kalloc_type      
	sz=0x000001b8 off=0x00f68480-0x00f68638 addr=0xfffffe0007f6c480-0xfffffe0007f6c638         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000010 off=0x00f68638-0x00f68648 addr=0xfffffe0007f6c638-0xfffffe0007f6c648         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 113 at 0x04acf340
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     0AC2C136-E10C-326B-84B4-BD01406C7AB0
008: LC_BUILD_VERSION            Platform: iOSKernelKit, MinOS: 27.2, SDK: 27.2, Tool: ld (27106)
009: LC_SOURCE_VERSION           553.40.2.0.0
010: LC_FUNCTION_STARTS          offset=0x004a94d40 size=0x90
```

## Info.plist keys [KC]

- `AppleKernelExternalComponent`: `True`
- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `pthread`
- `CFBundleIdentifier`: `com.apple.kec.pthread`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `pthread`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `KernelKit.iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `kernelkit.iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: ``
- `DTSDKName`: `kernelkit.iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `NSHumanReadableCopyright`: `Copyright © 2012 Apple Inc. All rights reserved.`
- `OSBundleAllowUserLoad`: `True`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/KernelKit/System/Library/Extensions/pthread.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904655712`
- `_PrelinkExecutableRelativePath`: `pthread`
- `_PrelinkExecutableSize`: `32069`
- `_PrelinkExecutableSourceAddr`: `-2198904655712`
- `_PrelinkKmodInfo`: `-2198829104912`

## Strings (42) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `I`
- `kern_support.c`
- `cvwait: thread entry with same sequence already present\n`
- `_psynch_mutexdrop_internal: multiple preposts\n`
- `ksyn_wqfind`
- `PSYNCH: pid[%d]: uaddr 0x%llx busy for synch type 0x%x [pre %d:0x%x:0x%x]\n`
- `\"kwq_handle_unlock: writer pending but no writebit set %x\\n\" @%s:%d`
- `\"removing item from wrong queue\" @%s:%d`
- `\"workqueue thread start function pointer is NULL\" @%s:%d`
- `\"ksyn_mtxsignal: panic signaling empty queue\" @%s:%d`
- `\"ksyn_queue_find_signalseq(): unknown wait queue element type (%d)\\n\" @%s:%d`
- `PSYNCH: pid[%d]: uaddr 0x%llx busy for synch type 0x%x [ioc %d:%d]\n`
- `\"ksyn_wait continuation returned\" @%s:%d`
- `pthread_mutex_default_policy`
- `__func__ \": thread_set_wq_state failed: %d\" @%s:%d`
- `site.struct ksyn_wait_queue`
- `1111221`
- `cvbroad: invalid L, U and S values\n`
- `PSYNCH: pid[%d]: uaddr 0x%llx busy for synch type 0x%x [intr %d:0x%x:0x%x:0x%x]\n`
- `\"kw_turnstile still non-null upon release\" @%s:%d`
- `\"failed to allocate kwe\\n\" @%s:%d`
- `1111212222222222222211122112222`
- `psynch_mutexwait: more than one prepost\n`
- `\"pth_proc_hashinit: hash init returned 0\\n\" @%s:%d`
- `\"ksyn_signal: panic signaling non-waiting element\" @%s:%d`
- `\"ksyn_signal: panic waking up thread %x\\n\" @%s:%d`
- `\"unknown kwe state\\n\" @%s:%d`
- `PSYNCH: pid[%d]: uaddr 0x%llx busy for synch type 0x%x [inq %d:%d]\n`
- `psynch_mutexwait: returning 0 lseq in mutexwait with no EBIT \n`
- `\"rwunlock: invalid type for lock grants\" @%s:%d`
- `\"removing item from empty queue\" @%s:%d`
- `pthread`
- `PSYNCH: pid[%d]: %s\n`
- `\"ksyn_signal: panic signaling empty queue\" @%s:%d`
- `\"kwe is not in a valid state: %d\" @%s:%d`
- `\"CV:entries in queue durinmg reinit %d:%d\\n\" @%s:%d`
- `site.struct ksyn_waitq_element`
- `psync_cvwait; invalid sequence numbers\n`
- `kern_synch.c`
- `cvbroad: difference greater than maximum possible thread count\n`
- `\"psync_cvwait: unexpected wait queue element type\\n\" @%s:%d`
- `\"adding enqueued item to another queue\" @%s:%d`
