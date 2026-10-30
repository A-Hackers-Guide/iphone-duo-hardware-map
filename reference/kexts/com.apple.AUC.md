# `com.apple.AUC`

- Name: AUC
- Version: `1.0`
- UUID: `80AB69D5-EFB3-32DA-92CE-95BC30AEAA57`
- Source version: `638.12.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleMobileFileIntegrity`](com.apple.driver.AppleMobileFileIntegrity.md) 1.0.1, [`com.apple.iokit.IOAVFamily`](com.apple.iokit.IOAVFamily.md) 1.0.0, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.7.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.4.1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0d1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0d1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0d1, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d3, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 9.0.0d1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AUC
- `CFBundleIdentifier`: `com.apple.AUC`
- `IOClass`: `AUC`
- `IOPersonalityPublisher`: `com.apple.AUC`
- `IOProviderClass`: `IOResources`
- `IOUserClientClass`: `AUCUserClient`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AUC` | 0x130 | IOService → IORegistryEntry |
| `AUCAsynchronousScheduler` | 0x2c50 |  |
| `AUCUserClient` | 0x148 | IOUserClient → IOService → IORegistryEntry |
| `AUCWorkloop` | 0x18 |  |
| `ConnectionWatchdog` | 0x70 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002cf0 off=0x0014b340-0x0014e030 addr=0xfffffe000714f340-0xfffffe0007152030 r--/r--   __TEXT            
	sz=0x00000d62 off=0x0014ba58-0x0014c7ba addr=0xfffffe000714fa58-0xfffffe00071507ba               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000184c off=0x0014c7ba-0x0014e006 addr=0xfffffe00071507ba-0xfffffe0007152006               __TEXT.__os_log           
	sz=0x00000020 off=0x0014e010-0x0014e030 addr=0xfffffe0007152010-0xfffffe0007152030               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00007f08 off=0x0165e8a0-0x016667a8 addr=0xfffffe00086628a0-0xfffffe000866a7a8 r-x/r-x   __TEXT_EXEC       
	sz=0x00007b88 off=0x0165e8a0-0x01666428 addr=0xfffffe00086628a0-0xfffffe000866a428          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000380 off=0x01666428-0x016667a8 addr=0xfffffe000866a428-0xfffffe000866a7a8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001b4 off=0x0492dee8-0x0492e09c addr=0xfffffe000b931ee8-0xfffffe000b93209c rw-/rw-   __DATA            
	sz=0x000000d1 off=0x0492dee8-0x0492dfb9 addr=0xfffffe000b931ee8-0xfffffe000b931fb9               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b931fc0-0xfffffe000b932098               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000b932098-0xfffffe000b93209c               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001670 off=0x00f8f7b0-0x00f90e20 addr=0xfffffe0007f937b0-0xfffffe0007f94e20 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x00f8f7b0-0x00f8f7d8 addr=0xfffffe0007f937b0-0xfffffe0007f937d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x00f8f7d8-0x00f8f800 addr=0xfffffe0007f937d8-0xfffffe0007f93800         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001118 off=0x00f8f800-0x00f90918 addr=0xfffffe0007f93800-0xfffffe0007f94918         __DATA_CONST.__const            
	sz=0x00000240 off=0x00f90918-0x00f90b58 addr=0xfffffe0007f94918-0xfffffe0007f94b58         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x00f90b58-0x00f90bf8 addr=0xfffffe0007f94b58-0xfffffe0007f94bf8         __DATA_CONST.__kalloc_var       
	sz=0x000001c0 off=0x00f90bf8-0x00f90db8 addr=0xfffffe0007f94bf8-0xfffffe0007f94db8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000068 off=0x00f90db8-0x00f90e20 addr=0xfffffe0007f94db8-0xfffffe0007f94e20         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 125 at 0x04ad0cb4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     80AB69D5-EFB3-32DA-92CE-95BC30AEAA57
008: LC_SOURCE_VERSION           638.12.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a96410 size=0x138
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleDisplayName`: `AUC`
- `CFBundleExecutable`: `AUC`
- `CFBundleGetInfoString`: `AUC 1.0 Copyright 2017, Apple Inc.`
- `CFBundleIdentifier`: `com.apple.AUC`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AUC`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `LSApplicationCategoryType`: ``
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2017 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AUC.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904442048`
- `_PrelinkExecutableRelativePath`: `AUC`
- `_PrelinkExecutableSize`: `50204`
- `_PrelinkExecutableSourceAddr`: `-2198904442048`
- `_PrelinkKmodInfo`: `-2198829064472`

## Strings (187) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `<<<< AUC >>>>`
- `auclog_level`
- `ConnectionWatchdog`
- `IOReturn AUC::DPRemovedNotificationGated(IOService *)`
- `virtual IOReturn AUC::hdcp_get_reply(uint8_t *, size_t *)`
- `CloseUserClient`
- `Not Capable`
- `IOReturn AUC::hdcp_send_request_gated(const uint8_t *, size_t, ConnectionWatchdog *)`
- `NO`
- `AUC`
- `1`
- `AUCUUID`
- `upstreamConnectionSendMessage`
- `upstreamConnectionGetStatusFromAULFlags`
- `auc_dcp_queue`
- `\"%s, Could not cast newService: %p to CommonAVVideoInterface\\n\" @%s:%d`
- `AUC:%s`
- `%s[%p]::%s(): terminate() failed.\n`
- `AUCWorkloop`
- `site.AUCAsynchronousScheduler`
- `upstreamConnectionGetMessage`
- `checkForHooverProtocolRequired`
- `\n`
- `AUCWorkloop[%p] released.`
- `site.AUCLock`
- `EnableMessageTimer`
- `Unknown`
- `site.AUC`
- `success`
- `hdcp-hoover-protocol`
- `IOAVVideoInterface`
- `EDID UUID`
- `hdcp_get_reply`
- `Up`
- `displayLocation != kIOAVLocationCount`
- `fail`
- `protectedIOSurfaceSeenRecentlyTimer_Handler`
- `IOReturn auc_CreateAUPPacketCallback(OSObject *, OSData *, void *)`
- `void AUC::InterfaceStatusAndType(IOAVVideoInterface *, UInt32 *, UInt32 *)`
- `bool AUC::DPPluggedNotification(void *, IOService *)`
- `DPRemovedNotification`
- `void AUC::DPRemovedNotificationAsync(void *, void *)`
- `site.ConnectionWatchdog`
- `12111112122212121111111111111111111111112`
- `121`
- `AUCAsynchronousScheduler`
- `12112122222112`
- `init`
- `bool AUC::DPRemovedNotification(void *, IOService *)`
- `site.AUCRecursiveLock`
- `site.AUCTimer`
- `:type0`
- `site.AUCScheduler`
- `void AUC::protectedIOSurfaceSeen(IOAVVideoInterface *)`
- `12111112122212121122112112111111111122`
- `%s[%p]::%s()\n`
- `free`
- `void AUC::aucUpstreamConnectionStatusChanged()`
- `IOMobileFramebuffer`
- `Down`
- `Unsupported Interface`
- `DPPluggedNotification`
- `AUC.cpp`
- `AUCUserClient`
- `site.AUCWorkloop`
- `timer_handler_gated`
- `YES`
- `AssertMacros: %s, %s file: %s, line: %d, value: %lld\n`
- `IOReturn AUC::DPPluggedNotificationGated(IOService *)`
- `AUCWorkLoop`
- `122121111111121211111111212111111112121111111121211111111212111111112121111111121211111111212111111112121111111121211111111212111111112121111111121211111111212111111112121111111121211111111212111111112121111111121211111111212111111112121111111121211111111212111111112121111111121211111111212111111112`
- `LocalAULRcvRspMsg`
- `:Unknown`
- `site.AUCUserClient*`
- `/Library/Caches/com.apple.xbs/C57CF2F6-5552-405F-94A7-90D29015B482/TemporaryDirectory.HbIjCG/Sources/CoreAUCKext/Kernel/Embedded/AUC.cpp`
- `21`
- `upstreamConnectionSetStatus`
- `:type1`
- `DPRemovedNotificationGated`
- `site.AUCUserClient`

**[__TEXT.__os_log]**

- `%s PL read_edt(%s) provider=%p\n`
- `%s: [%p] %s:IOMobileFramebuffer not found.\n`
- `%s [%p] first protected surface in a while (%llu milliseconds)`
- `%s create ConnectionWatchdog [%p]`
- `%s [%p] upstreamConnectionGetStatusFromAULFlags flags: 0x%08x; digitalTransmitting: %d; hdcpUp: %d; supportsHDCP: %d`
- `%s [%p]::%s: INTERNAL, returning Up/Type1\n`
- `%s [%p] Status is now '%s%s:%d. mSendCallbackOnSetStatus = %d ' (was '%s%s:%d').`
- `%s: tempIOMFB NOT set!!!!!!!.\n`
- `%s [%p] displayType = %u, status = %u, type = %u, ioSurfaceProtectionOption = 0x%llx, displayCapable = %s . \n`
- `%s [%p] In AUC::InterfaceCapable\n`
- `%s [%p]::%s: Call to hdcp_send_request:  r = %X.\n`
- `%s [%p]::%s: DTT & !hdcpUp, returning kUpstreamConnectionStatus_UnsupportedInterface\n`
- `%s: [%p] HDCPGetSecureStatusForDisplay: displayType = %u, status = %u, type = %u, isDetermined = %s\n`
- `%s terminate coreauc [%p] with optionBits:%u`
- `%s timeSinceLastSeen > %llu ms: setting SeenRecently to false and disabling SeenRecently timer`
- `%s: [%p]found userClient[%p] at index = %d.\n`
- `%s [%p]::%s, created ConnectionWatchdog object \n`
- `%s [%p]::AppleRGBOUT: DP cable removed\n`
- `%s [%p]::%s: mAULMessageBuffer(%p) = %d bytes.\n`
- `%s [%p]::%s: none of the above, returning Down\n`
- `%s seenRecentlyTimer_Handler: protected surface NOT seen recently, disabling SeenRecently timer`
- `%s [%p]::%s Unable to get location of interface from CommonAVVideoInterface.\n`
- `%s [%p]::%s, Releasing mStaleConnectionWatchdog_DP object\n`
- `%s [%p]::%s newService(%p) != mDriver_DP(%p)\n`
- `%s [%p]::%s: protected surface NOT seen recently: message timer going to sleep : Status is '%s%s:%d.\n`
- `%s [%p] Status is still '%s%s:%d'.`
- `%s PL read_edt: data=%p, len=%d\n`
- `%s [%p] InterfaceCapable: status = %u, type = %u, surfaceBits = 0x%llx, capable = %s. \n`
- `%s [%p] %s: no hdcp reply available while not pending\n`
- `%s [%p]::%s: Call to LocalAULRcvRspMsg: protocolType=%d, hdcpFlags = 0x%X, err = %d. header->status = %d\n`
- `%s [%p]::%s: upstreamConnectionSendMessage result r = %d,  mAUCDriver = %p, loopCount = %d.\n`
- `%s [%p]::%s: !DTT, returning UnsupportedInterface\n`
- `%s [%p] interface == NULL; using kUpstreamConnection{Status,Type}_Unknown.\n`
- `%s [%p] InterfaceStatusAndType: special case for internal display\n`
- `%s [%p]::%s: enabling SeenRecently timer\n`
- `%s [%p]::%s, Could not cast newService: %p to CommonAVVideoInterface\n`
- `%s [%p] In AUC::InterfaceCapable: returning false EARLY because AVVideoInterface is inactive`
- `%s: [%p] Want to remove userClient[%p] at index = %d`
- `%s PL read_edt(%s) provider=%d\n`
- `%s PL read_edt: done\n`
- `%s: tempIOMFB set!!!!!!!.\n`
- `%s: hdcp-hoover-protocol set!!!!!!!.\n`
- `%s [%p] In AUC::InterfaceForDisplayType(%u)\n`
- `%s [%p]::%s,  release DP driver\n`
- `%s [%p] DisplayProtectionOptions: prot = 0x%llx, error = %d. \n`
- `%s [%p] Could not cast param0: %p to AUCOUT instance\n`
- `%s [%p] AppleRGBOUT: DP cable attached.\n`
- `%s [%p]::%s: can't allocate ConnectionWatchdog\n`
- `%s [%p]::%s: createAUPPacketAsync failed with: 0x%x\n`
- `%s [%p] %s: ProcessStatusChange for userClient[%p] at index = %d.\n`
- `%s %s: AULInitContext failed, protocolType = %d, r = %X\n`
- `%s [%p]::%s[%p] Received timer callback \n`
- `%s started coreauc [%p] %s`
- `<<<< AUC >>>> loggingLevel = %d`
- `%s [%p] Status = %d, Type = %d, protectionOptions = 0x%llx. \n`
- `%s [%p]::%s but no DP driver\n`
- `%s [%p]::%s: protected surface seen recently: re-arming message timer for %ull milliseconds from now`
- `%s [%p] upstreamConnectionGetMessage: hhdcp_get_reply failed with return code %d`
- `%s seenRecentlyTimer_Handler: timeSinceLastSeen = %llu ms (lastSeen = %llu, timeNow = %llu)`
- `%s: [%p] Setting userClient[%p] at index = %d.\n`
- `%s: [%p] In HDCPGetSecureStatusForDisplay`
- `%s [%p] protectedIOSurfaceSeenRecentlyTimer to be run only on an external display`
- `%s [%p] InterfaceStatusAndType: if=%p, dispLoc=%u, status=%u, type=%u`
- `%s [%p] no Service received in call_DPPluggedNotificationGated \n`
- `%s [%p]::%s: no map or size passed\n`
- `%s [%p]::%s: Call to LocalAULGetReqMsg failed:  r = %X.\n`
- `%s: [%p] incoming userClient[%p]`
- `%s [%p]::%s(%p:%ld)\n`
- `%s %s: dropping callback for non pending notification\n`
- `%s [%p]::%s: protected surface NOT seen recently: but re-arming message timer for %ull milliseconds from now to finish determining`
- `%s [%p] upstreamConnectionGetMessage: hdcpFlags=0x%x`
- `%s [%p]::%s: DTT & supportsHDCP & hdcpUp`
- `%s PL read_edt: values=%d\n`
- `%s PL read_edt: buf=%p\n`
- `%s [%p]::%s called \n`
- `%s [%p] InterfaceForDisplayType: Special case for internal display\n`
- `%s [%p] In AUC::DisplayCapable\n`
- `%s [%p]::%s, Storing mConnectionWatchdog_DP to mStaleConnectionWatchdog_DP object\n`
- `%s %s: Processed HDCP packet successfully\n`
- `%s %s: ConnectionWatchdog message timer waking up...\n`
- `%s [%p] InterfaceForDisplayType: displayType %u is not being tracked. \n`
- `%s [%p] InterfaceStatusAndType: IOAVVideoInterface is not being tracked, interface:%p, location:%u, mDriver_DP:%p.\n`
- `%s [%p]::%s(%p)\n`
- `%s [%p]::%s: upstreamConnectionSendMessage call is kIOReturnBusy.\n`
- `%s [%p]::%s: REVOKED, returning DownNotCapable\n`
- `%s [%p] topologyType=%d\n`
- `%s [%p]::%s: DTT & !supportsHDCP, returning DownNotCapable\n`
- `%s [%p]::%s: Ignoring status change, numberOfTimes:%d, from '%s' to '%s'.\n`
- `%s [%p] InterfaceStatusAndType: calling Watchdog\n`
- `%s [%p]::%s but newService is NULL\n`
- `%s %s: dropped HDCP packet notification\n`
- `%s [%p] upstreamConnectionGetStatusFromAULFlags_continue flags: 0x%08x; repeater: %s; statusVersion:%d`
- `%s [%p]::%s(%p, %p)\n`
- `%s: [%p] Removing userClient[%p] at index = %d.\n`
- `%s PL read_edt: databytes=%d\n`
- `%s PL read_edt: databytes=%p\n`
- `%s [%p] DisplayCapable: returning true EARLY because ioSurface is not protected\n`
- `%s [%p]::%s hot plug notification while we already have an interface available\n`
- `%s [%p]::%s, Could not cast param0: %p to AUCOUT instance\n`
- `%s [%p]::%s: HDCP reply was never collected\n`
- `%s [%p]::%s called`
- `%s timeSinceLastSeen <= %llu ms: scheduling SeenRecently timer to check again in a bit`
- `%s PL read_edt: data=%d, len=%d\n`
- `%s [%p] setting LastSeenAtTimeMS to %llu`
- `%s [%p] In DisplayProtectionOptions\n`
- `%s [%p] In AUC::InterfaceCapable: returning true EARLY because ioSurface is not protected\n`
- `%s [%p]::%s: hdcp reply is not ready\n`
