# `com.apple.driver.AppleARMWatchdogTimer`

- Name: AppleARMWatchdogTimer
- Version: `1`
- UUID: `7B5A2853-BCC9-361E-A59F-8BDD7CC99F7C`
- Source version: `334.40.4.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) | `AppleARMWatchdogTimer` | `wdt,s5l8960x` |

## IOKit personalities (1) [KC]

### AppleARMWatchdogTimer
- `CFBundleIdentifier`: `com.apple.driver.AppleARMWatchdogTimer`
- `IOClass`: `AppleARMWatchdogTimer`
- `IONameMatch`: `wdt,s5l8960x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleARMWatchdogTimer`
- `IOPlatformActiveAction`: `80000`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformQuiesceAction`: `80000`
- `IOPlatformSleepAction`: `350`
- `IOPlatformWakeAction`: `350`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleARMWatchdogTimer` | 0x1d0 | IOWatchdog → IOService → IORegistryEntry |
| `AppleARMWatchdogTimerFunctionExpireWatchdog` | 0x30 | AppleARMFunction |
| `IOWatchdog` | 0xf8 | IOService → IORegistryEntry |
| `IOWatchdogUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001a77 off=0x0017d6f0-0x0017f167 addr=0xfffffe00071816f0-0xfffffe0007183167 r--/r--   __TEXT            
	sz=0x000013ff off=0x0017dd68-0x0017f167 addr=0xfffffe0007181d68-0xfffffe0007183167               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000593c off=0x0173d880-0x017431bc addr=0xfffffe0008741880-0xfffffe00087471bc r-x/r-x   __TEXT_EXEC       
	sz=0x0000540c off=0x0173d880-0x01742c8c addr=0xfffffe0008741880-0xfffffe0008746c8c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000530 off=0x01742c8c-0x017431bc addr=0xfffffe0008746c8c-0xfffffe00087471bc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x0000020e off=0x04930d50-0x04930f5e addr=0xfffffe000b934d50-0xfffffe000b934f5e rw-/rw-   __DATA            
	sz=0x00000118 off=0x04930d50-0x04930e68 addr=0xfffffe000b934d50-0xfffffe000b934e68               __DATA.__data             
	sz=0x000000e8 off=0x00000000-0x000000e8 addr=0xfffffe000b934e68-0xfffffe000b934f50               __DATA.__common           (Zerofill)
	sz=0x0000000e off=0x00000000-0x0000000e addr=0xfffffe000b934f50-0xfffffe000b934f5e               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001ae8 off=0x00fc7c30-0x00fc9718 addr=0xfffffe0007fcbc30-0xfffffe0007fcd718 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x00fc7c30-0x00fc7c50 addr=0xfffffe0007fcbc30-0xfffffe0007fcbc50         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x00fc7c50-0x00fc7c70 addr=0xfffffe0007fcbc50-0xfffffe0007fcbc70         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000014c8 off=0x00fc7c70-0x00fc9138 addr=0xfffffe0007fcbc70-0xfffffe0007fcd138         __DATA_CONST.__const            
	sz=0x00000100 off=0x00fc9138-0x00fc9238 addr=0xfffffe0007fcd138-0xfffffe0007fcd238         __DATA_CONST.__kalloc_type      
	sz=0x00000190 off=0x00fc9238-0x00fc93c8 addr=0xfffffe0007fcd238-0xfffffe0007fcd3c8         __DATA_CONST.__kalloc_var       
	sz=0x00000298 off=0x00fc93c8-0x00fc9660 addr=0xfffffe0007fcd3c8-0xfffffe0007fcd660         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b8 off=0x00fc9660-0x00fc9718 addr=0xfffffe0007fcd660-0xfffffe0007fcd718         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 189 at 0x04ad2934
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     7B5A2853-BCC9-361E-A59F-8BDD7CC99F7C
008: LC_SOURCE_VERSION           334.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004a97fa0 size=0xf0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleARMWatchdogTimer`
- `CFBundleIdentifier`: `com.apple.driver.AppleARMWatchdogTimer`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleARMWatchdogTimer`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2020 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleARMWatchdogTimer.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904236304`
- `_PrelinkExecutableRelativePath`: `AppleARMWatchdogTimer`
- `_PrelinkExecutableSize`: `37033`
- `_PrelinkExecutableSourceAddr`: `-2198904236304`
- `_PrelinkKmodInfo`: `-2198829052592`

## Strings (128) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IOPMUSetBootStagePanicSafe`
- `simple-reconfig-wdog-icc-time`
- `1`
- `simple-reconfig-wdog-support`
- `\"legacy reconfig watchdog is not supported for wdt-versions >= 3\" @%s:%d`
- `\"%s: The contents of the 'trigger-ce' property in the device tree are malformed\" @%s:%d`
- `IOKitQuiesceWatchdogSupported`
- `panic-forcepoweroff-flag-bit`
- `IOPMUBootStage`
- `IOKitQuiesceWatchdogEnabled`
- `AppleARMWatchdogTimer.cpp`
- `watchdog userspace and IOKit monitoring defanged on single user mode\n`
- `site.CETriggerConfiguration`
- `Device panic triggered by an external agent (via SMC doorbell)`
- `wdog: Nested panic detected: attempting to promote this panic to an APWD report...\n`
- `cpu-id`
- `watchdogd`
- `PanicWatchdogEnabled`
- `\"%s: Need to add 'reg' entry in device tree for the panic scratch register\" @%s:%d`
- `AP Watchdog enabled in panic flow (%llu secs)\n`
- `-wdt-no-iokit`
- `IOBSD`
- `watchdog timeout: no checkins from %s since %s (%llu seconds ago)`
- `in progress`
- `\"Simplified Reconfig watchdog cannot be supported without SMC AP watchdog support\" @%s:%d`
- `function-mcc_ctrl`
- `\"restart not handled by next PE_halt_restart routine\" @%s:%d`
- `-wdt-no-shutdown`
- `\"%s: Need to add a 'reg' entry in the device tree for the AP watchdog configuration\" @%s:%d`
- `\"improbable 'panic-forcepoweroff-flag-bit' flag specified in device tree (%d)\" @%s:%d`
- `site.AppleARMWatchdogTimer`
- `Reconfig Watchdog: ICC = %d\n`
- `\"improbable 'panic-save-flag-bit' specified in device tree (%d)\" @%s:%d`
- `debug`
- `Watchdog userspace monitoring defang count is decreased with reason %s\n`
- `function-panic_halt_helper`
- `stress-rack`
- `watchdog timeout: no checkins from %s in %llu seconds (%llu total checkins since monitoring last enabled)`
- `IOPMU`
- `finished`
- `panic flow Config Engine Trigger NOT found\n`
- `\"Reconfig Watchdog monitoring can't be disabled\" @%s:%d`
- `panic-save-flag-bit`
- `watchdog configured (source: %s) to monitor userspace, SoC watchdog %sabled, panic SoC watchdog %sabled, halt on SoC watchdog expiration: %s, userspace IOKit monitoring %sabled, shutdown monitoring %sabled\n`
- `com.apple.private.iowatchdog.user-access`
- `PanicSMCWatchdogEnabled`
- `reg`
- `IOWatchdog`
- `invalid watchdog (wdt) boot-arg specified, bits 0x%llx will be ignored\n`
- `detected kernel POST testing enabled, watchdog disabled\n`
- `root`
- `\"%s: clock speed %llu does not match absolute time\" @%s:%d`
- `\"%s: The contents of the 'trigger-config' property in the device tree are malformed\" @%s:%d`
- `Disabling AON Watchdog...\n`
- `AP Watchdog extended in panic flow by (%llu secs)\n`
- `site.AppleARMWatchdogTimerFunctionExpireWatchdog`
- `\"%s: Failed to allocate memory for the trigger configuration\" @%s:%d`
- `panic flow Config Engine Trigger found at 0x%llx\n`
- `wdt`
- `watchdog disabled by boot-arg\n`
- `watchdog timeout: no checkins from %s in %llu seconds (%llu totalcheckins since monitoring last enabled), shutdown in progress, vfs shutdown %s, last vfs completion time: %llu seconds ago`
- `site.IOMemoryMap*`
- `System Watchdog extended in panic flow by (%llu secs)\n`
- `debug_disable`
- `dis`
- `unexpected event: %u\n`
- `-panic_notify`
- `wdt boot-arg`
- `ShutdownWatchdogEnabled`
- `\"Reconfig watchdog cannot be supported without SMC AP watchdog support\" @%s:%d`
- `trigger-ce`
- `function-panic_notify`
- `System Watchdog enabled in panic flow (%llu secs)\n`
- `wdog: Nested panic detected: APWD promotion disabled, system will reset shortly...\n`
- `IOWatchdogUserClient`
- `en`
- `WDT timeout: CPU %d failed to respond`
- `\"simple-reconfig-wdog-support and reconfig-wdog-support can't be enabled at the same time. They are mutually exclusive\" @%s:%d`
- `\"%s: invalid width of 'panic-forcepoweroff-flag-bit' in device tree\" @%s:%d`
- `AP Watchdog disabled in panic flow\n`
- `site.IOWatchdogUserClient`
- `Watchdog userspace monitoring defang count is increased with reason %s\n`
- `\"panic SMC watchdog cannot be supported without SMC AP watchdog support\" @%s:%d`
- `trigger-config`
- `WDT timeout: unable to pend immediate cross-call on CPU %d`
- `\"PMU KEXT expected to handle restart but no saved PE_halt_restart routine found\" @%s:%d`
- `reconfig-wdog-support`
- `\"%s: Need to add 'reg' entry in device tree for the AP watchdog deadline\" @%s:%d`
- `function-panic_flush_helper`
- `no-pmu`
- `\"Reconfig Watchdog monitoring can't be enabled\" @%s:%d`
- `site.IOWatchdog`
- `no`
- `AppleARMWatchdogTimer`
- `extended-iokit-quiesce-timeout`
- `System Watchdog disabled in panic flow\n`
- `wdog: warn PMUSetVariable failed %#x\n`
- `wdog: panic chipreset\n`
- `I`
- `1211111212221212121112222221222`
- `\"%s: Need to add 'reg' entry in device tree for the panicsave register\" @%s:%d`
- `site.TriggerConfiguration`
- `AppleARMWatchdogTimerFunctionExpireWatchdog`
- `kernPOST`
- `-s`
- `yes`
- `IODeviceTree:/options`
- `wdt-version`
- `disable-halt-on-expiration`
- `121111`
- `monitoring resumed`
- `watchdog timeout: no checkins from %s in %llu seconds (%llu totalcheckins since monitoring last enabled), shutdown in progress, vfs shutdown not yet started`
- `defeature-panic-smc-watchdog`
- `\"%s: Missing or invalid 'panic-save-flag-bit' in device tree\" @%s:%d`
- `awl-scratch-supported`
- `/cpus`
- `inferred defaults`
- `\"failed to read wdt-version property\" @%s:%d`
- `site.UInt8`
- `info-has_phra`
- `IODTNVRAM`
- `userspace watchdog timeout: %s`
- `AppleARMWatchdogTimer::start: _wdtBaseAddress: %#lx _wdtResetCount=%#x _SMCWatchdogAvailable=%d\n`
- `12111112122212121111111111121`
- `defang_watchdogd`
- `boot`
- `1211111212221212121112222221222121111212222111122211221112`
- `wdog: restart\n`
