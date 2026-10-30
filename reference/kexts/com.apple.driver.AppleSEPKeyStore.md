# `com.apple.driver.AppleSEPKeyStore`

- Name: AppleSEPKeyStore
- Version: `2`
- UUID: `751A5211-599F-3F8A-B2C4-612DD0FDC396`
- Source version: `2383.40.18.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEffaceableStorage`](com.apple.driver.AppleEffaceableStorage.md) 1.0.0, [`com.apple.driver.AppleMobileFileIntegrity`](com.apple.driver.AppleMobileFileIntegrity.md) 1.0.2, [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.iokit.IOCryptoAcceleratorFamily`](com.apple.iokit.IOCryptoAcceleratorFamily.md) 1.0.0, [`com.apple.kec.corecrypto`](com.apple.kec.corecrypto.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleKeyStore
- `CFBundleIdentifier`: `com.apple.driver.AppleSEPKeyStore`
- `IOClass`: `AppleKeyStore`
- `IOMatchCategory`: `AppleKeyStore`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSEPKeyStore`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `AppleKeyStoreUserClient`

### AppleKeyStoreTest
- `CFBundleIdentifier`: `com.apple.driver.AppleSEPKeyStore`
- `IOClass`: `AppleKeyStoreTest`
- `IOMatchCategory`: `AppleKeyStoreTest`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSEPKeyStore`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `AppleKeyStoreTestUserClient`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleKeyStore` | 0x1f8 | IOService → IORegistryEntry |
| `AppleKeyStoreCommand` | 0x28 | IOCommand |
| `AppleKeyStoreTest` | 0x88 | IOService → IORegistryEntry |
| `AppleKeyStoreTestUserClient` | 0xd8 | IOUserClient → IOService → IORegistryEntry |
| `AppleKeyStoreUserClient` | 0x118 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000609c off=0x00734e40-0x0073aedc addr=0xfffffe0007738e40-0xfffffe000773eedc r--/r--   __TEXT            
	sz=0x00004db6 off=0x007355a8-0x0073a35e addr=0xfffffe00077395a8-0xfffffe000773e35e               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000083 off=0x0073a35e-0x0073a3e1 addr=0xfffffe000773e35e-0xfffffe000773e3e1               __TEXT.__os_log           
	sz=0x00000aec off=0x0073a3f0-0x0073aedc addr=0xfffffe000773e3f0-0xfffffe000773eedc               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00040754 off=0x025da100-0x0261a854 addr=0xfffffe00095de100-0xfffffe000961e854 r-x/r-x   __TEXT_EXEC       
	sz=0x0003fd24 off=0x025da100-0x02619e24 addr=0xfffffe00095de100-0xfffffe000961de24          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000a30 off=0x02619e24-0x0261a854 addr=0xfffffe000961de24-0xfffffe000961e854          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000a30 off=0x04995828-0x04996258 addr=0xfffffe000b999828-0xfffffe000b99a258 rw-/rw-   __DATA            
	sz=0x00000444 off=0x04995828-0x04995c6c addr=0xfffffe000b999828-0xfffffe000b999c6c               __DATA.__data             
	sz=0x000000e8 off=0x00000000-0x000000e8 addr=0xfffffe000b999c70-0xfffffe000b999d58               __DATA.__common           (Zerofill)
	sz=0x00000500 off=0x00000000-0x00000500 addr=0xfffffe000b999d58-0xfffffe000b99a258               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00005240 off=0x011e62e8-0x011eb528 addr=0xfffffe00081ea2e8-0xfffffe00081ef528 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x011e62e8-0x011e62f8 addr=0xfffffe00081ea2e8-0xfffffe00081ea2f8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x011e62f8-0x011e6308 addr=0xfffffe00081ea2f8-0xfffffe00081ea308         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003e38 off=0x011e6308-0x011ea140 addr=0xfffffe00081ea308-0xfffffe00081ee140         __DATA_CONST.__const            
	sz=0x00000d80 off=0x011ea140-0x011eaec0 addr=0xfffffe00081ee140-0xfffffe00081eeec0         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x011eaec0-0x011eaf60 addr=0xfffffe00081eeec0-0xfffffe00081eef60         __DATA_CONST.__kalloc_var       
	sz=0x00000518 off=0x011eaf60-0x011eb478 addr=0xfffffe00081eef60-0xfffffe00081ef478         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000098 off=0x011eb478-0x011eb510 addr=0xfffffe00081ef478-0xfffffe00081ef510         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000018 off=0x011eb510-0x011eb528 addr=0xfffffe00081ef510-0xfffffe00081ef528         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 345 at 0x04ae43a0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     751A5211-599F-3F8A-B2C4-612DD0FDC396
008: LC_SOURCE_VERSION           2383.40.18.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab0148 size=0x638
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSEPKeyStore`
- `CFBundleIdentifier`: `com.apple.driver.AppleSEPKeyStore`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSEPKeyStore`
- `CFBundleNumericVersion`: `33587200`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `LSMinimumSystemVersion`: `4.0`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2009-2016 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSEPKeyStore.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898241984`
- `_PrelinkExecutableRelativePath`: `AppleSEPKeyStore`
- `_PrelinkExecutableSize`: `312416`
- `_PrelinkExecutableSourceAddr`: `-2198898241984`
- `_PrelinkKmodInfo`: `-2198828640216`

## Strings (433) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid ttl %llu%s\n`
- `e-apfs`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s kern_get_extended_state failed%s\n`
- `/options`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sinvalidating background policy gen %lld due to qualifying event.%s\n`
- `source`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %scalled state, for handle %d: %x%s\n`
- `bundle_id`
- `/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/platform/platform_kernel.c`
- `/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/platform/platform.c`
- `sepfw-load-at-boot`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Deleting identity %s%s\n`
- `com.apple.keystore.class.wku`
- `com.apple.applekeystore.selector.set_config`
- `entitled_for_%s`
- `kAppleKeyStoreKeyBagCreate`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s sleeping waiting for endpoint to wake up again.%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s manually picked up response%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %ssdv udv map lookup failed%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s ### proc: %s inode: %llu ### entiled: %i%s\n`
- `fs_migrate_media_key_to_class`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity_migrate: %d%s\n`
- `result`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s No input data%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s class mismatch %d vs %d%s\n`
- `AppleKeyStoreHelper.cpp`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Loaded identity %s as session %d%s\n`
- `com.apple.keystore.device`
- `keybag_create_access`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %skAppleKeyStoreUnlockDevice=%d%s\n`
- `com.apple.keystore.absinthe`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Invalid scalar counts%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n`
- `apfs_to_uea`
- `uea_to_app`
- `aks-endpoint`
- `\"not inside aks gate\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity_get_primary failed%s\n`
- `timer update`
- `com.apple.keystore.config.set.prederived_salt`
- `aks-cache-device-state`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s _sep_enabled = %d%s\n`
- `none`
- `duration_ms`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s map_sdv_udv: %d, enable: %i%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %scurrent task is kernel task%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sfailed to get proc_self%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Loading identity %s to handle %d%s\n`
- `root-ticket-hash`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to queue vfs notification%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unwrap class D key. Continuing anyways.%s\n`
- `com.apple.keystore.lockassertion`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAppleKeyStoreBackupKeyForVolume: Bad Argument %s\n`
- `com.apple.keystore.config.bind_kek_to_kb`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Wrong scalar argument%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s operation %s(sel: %d ret: %x%s)%s\n`
- `\"AppleSEPKeyStore\"`
- `site.encode_list_t`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s notifying user space of inactivity reboot%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unexpected error while reading effaceable (err: %x).%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s created identity, keybag handle = %d%s\n`
- `com.apple.keystore.access-keychain-keys`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid handle %d (_device_keybag_access: %d)%s\n`
- `com.apple.keystore.devicebackup`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s  %s : %4d %s (options:%08x, flags: 0x%x)%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sglobal assertion timer fired, destroy assertion%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sfailed to delete effaceable %d = 0x%x%s\n`
- `com.apple.keystore.auth-token`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Wrong packed count %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s not entitled to use console domain%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %scurrent time is %llu, assert set: %d, deadline: %llu, force: %d, pid: %d%s\n`
- `com.apple.keystore.config.set.max_unlock_attempts`
- `AppleKeyStoreTestUserClient`
- `AKSFileVaultServices`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s log filter %llx%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %spromote global assertion%s\n`
- `v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=(?=^{ipc_port}^{ipc_port}^{ipc_port})b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sget escrow token from effaceable %x, len: %u%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to undo %d: %x%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s process %s (bundle_id: %s) must have %s entitlement for %s%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to initialize _workLoop%s\n`
- `\"failed to decode state\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Cache enabled notification%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sinvalid policy type %d%s\n`
- `no-effaceable-storage`
- `unlocked`
- `locking`
- `wipe sandman blob`
- `/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/timestamp_ticket.c`
- `23:33:39`
- `aks events`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity create returned %x, handle_out %d%s\n`
- `prederived_passcode`
- `user_uuid`
- `/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/ipc.c`
- `121111121222121211111111111`
- `IODeviceTree:/filesystems`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Mapping volume without a valid persona.%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Can't find AppleSEPManager%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %scurrent state: %s, new state: %s (%lu), (ex:%u, new_ex:%u)%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s policy is invalid%s\n`
- `msg.c`
- `\"device state der too big to cache: %u > %zu\" @%s:%d`
- `AppleKeyStore`
- `\"sep_wait_for_reply called from within sep_action\" @%s:%d`
- `\"set_env failed\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad uuid length%s\n`
- `site.AppleKeyStoreUserClient`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s missing com.apple.keystore.device%s\n`
- `com.apple.keystore.memento`
- `\"invalid version %d\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to notify %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Invalid persona_uuid: %08x specified (not present in keybag), volume mapping failed!%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s existing mapping with mismatched flags 0x%x:0x%x%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s media key doesn't specify the class%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to negotiate, defaulting to v1%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s D-key effaceable locker does not exist, attempt to init it implicitly.%s\n`
- `\"Failed to write effaceable.\" @%s:%d`
- `com.apple.keystore.se.passcode_derivation`
- `media_key_log_event`
- `com.apple.keystore.enable_cache_flow`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s No packed items%s\n`
- `recovery success`
- `\"corrupted state?\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n`
- `site.AppleKeyStoreTestUserClient`
- `com.apple.keystore.config.set.oneness_automatic_mode`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s overflow%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n`
- `sks request timeout`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s loaded keybag, handle = %d%s\n`
- `com.apple.keystore.keybag.load`
- `com.apple.keystore.domain.select`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAppleKeyStoreIdentityVerify: result 0x%x%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n`
- `\"Failed to sep->allocateVisibleMemory() for OOL send Buffer\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Sending notification for volume %s %s (action %d, handle %d)%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Sending lock state change %s (%d) for handle %d (0x%x)%s\n`
- `\"no SEP endpoint\" @%s:%d`
- `sel:%u`
- `com.apple.keystore.stash.persist`
- `prederived_iterations`
- `bind_kek`
- `AKSKernelServices`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s skipping lock notification%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to map %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %ssuccessfully deleted effaceable, %d%s\n`
- `AppleEffaceableStorage`
- `com.apple.keystore.config.set.user_uuid`
- `prederived_type`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n`
- `version`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sForce updated timer%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity_migrate_first: %d%s\n`
- `memento blob effaced`
- `oneness_automatic_mode`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected session uid: %d requested by: %s (%d)%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s error %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s -- Volume keybags:%s\n`
- `fs_unwrap_media_key_from_class`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity_migrate%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s not fs key %d%s\n`
- `com.apple.keystore.sik.access`
- `com.apple.keystore.lockunlock`
- `com.apple.keystore.aux.auth`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Effective handle failed: %d%s\n`
- `com.apple.keystore.config.set.prederived_passcode`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s buffer size %d too small for data size %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to notify system keybag updation %d%s\n`
- `1222222`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Preparing for System Shutdown%s\n`
- `com.apple.keystore.config.set`
- `com.apple.keystore.device.verify`
- `failed `
- `wipe effaceable dkey`
- `fs_new_media_key_wrapped_to_class`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s negotiated to ipc header theirs:v%llu, ours:v%u -> negotiated:v%llu%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s creation of D key failed unexpectedly 0x%x%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %soverclock is %s%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Create keybag failed: %d.  Retrying %d more times.%s\n`
- `, name: '%s' rate: %d.%d/s`
- `locked`
- `com.apple.keystore.config.set.prederived_iterations`
- `board-id`
- `\"max inactivity window expired, failed to reboot the device\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s notified volume uuid %s - lock state = %d (err = %d)%s\n`
- `site.struct events_entry_s`
- `aks-inactivity`
- `keybag_load_access`
- `utils.c`
- `site.encode_list_data`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to queue update timer%s\n`
- `\"background policy generation counter wrapped\" @%s:%d`
- `AppleSEPManager`
- `inactivity_reboot`
- `112`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s: (%s) result=0x%x, class=%d, kcv=0x%02x%02x%02x%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sfailed to update policy expiration%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Found armIODriver node ID: %llx%s\n`
- `kAppleKeyStoreKeyBagCreateWithData`
- `com.apple.keystore.config.set.inactivity_reboot`
- `unique-chip-id`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s unkonwn state %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s existing mapping with mismatched personal uuid%s\n`
- `\"sks request timeout (%d strikes)\" @%s:%d`
- `com.apple.keystore.se.secret_drop`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %slock assert hold, duplicate : %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to prepare output memory descriptor.%s\n`
- `\"unexpected length\" @%s:%d`
- `SecureRoot`
- `\"Failed to sep->allocateVisibleMemory() for OOL recv Buffer\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %spolicy is null%s\n`
- `inactivity panic`
- `max_unlock_attempts`
- `prederived_salt`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported request %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Mapping volume without a cookie, failing.%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s existing mapping with mismatched options %d:%d%s\n`
- `com.apple.keystore.allow.background-processing-assertions`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Initialize effacable d_key.%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Cannot unwrap d_key from effaceable.%s\n`
- `com.apple.keystore.stash.access`
- `\"submit_coreanalytics_set_config_selector: idx %d != kConfigAnalyticsFieldCount %d\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s notification for handle: %d, state: %d, value: %d, flags: 0x%x%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %spfk_params sanity check failed%s\n`
- `com.apple.keystore.obliterate-d-key`
- `com.apple.keystore.device.uuid`
- `com.apple.keystore.config.set.escrow_period`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s AppleKeyStoreUserClient: Assertion timer fired%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOPerfControlClient::copyClient failed%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s ----------------%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s mapped uuid %s to bag %d, persona %s, compressed uuid: %d, flags: %d%s\n`
- `com.apple.applekeystore.apfs.cp_action`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s No space left for s_key (length: %zu, available: %llu)%s\n`
- `12111112122212121`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sinvalidated cache (async)%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdrop device assertion, type: %u%s\n`
- `112232222222`
- `com.apple.keystore.lockassertion.restore_from_backup`
- `com.apple.keystore.fairplay`
- `passcode`
- `com.apple.keystore.config.set.graceperiod`
- `site.AppleKeyStore`
- `Oct 13 2026`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s cmd: %d, booted_from: %d, result: %d%s\n`
- `com.apple.keystore.device.remote-session`
- `reboot`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %shandle 0 requested outside of user session pid=%d (%s) for sel=%d%s\n`
- `2221`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid soc: %llu%s\n`
- `i8@?0`
- `site.AppleKeyStoreTest`
- `\"failed to cast value %s\" @%s:%d`
- `kext_to_apfs`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to queue client notification%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s SEP timeout multiplier = %u%s\n`
- `\"unexpected wakeup reason 0x%x\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s un-entitled access to non-wku%s\n`
- `sks_to_kext`
- `12112`
- `AppleKeyStore.cpp`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s unloaded keybag%s\n`
- `com.apple.keystore.bak`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sno assertion set, ignore this%s\n`
- `fv authenticated`
- `com.apple.keystore.config.set.prederived_type`
- `development-cert`
- `AKSFileSystemKeyServices`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s notified volume uuid %s - locked%s\n`
- `first_unlock`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s wrong scalars count%s\n`
- `site.circular_queue_t`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sinvalidated cache (sync)%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s ipc digest failed%s\n`
- `boot-manifest-hash`
- `🌽 `
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s fs request with NULL volume uuid%s\n`
- `fs_unwrap_media_key_from_uid`
- `com.apple.keystore.lockassertion.global_assertion`
- `event`
- `site.struct aks_params_s`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sfs_check_class returned %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Wrong items count %d%s\n`
- `clientClose`
- `site.struct aks_ref_key_s`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks-cache-device-state disabled%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sfailed to get policy blob length for policy type %d%s\n`
- `unknown`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sinvalid state, cannot consume lock assert, device is in state: %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Sending First Unlock notification for handle %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s set handle %d as backup bag for handle %d%s\n`
- `12`
- `IODeviceTree:/chosen`
- `1`
- `121111121222121211112121221111122121121221111222111111211222222`
- `aks-bfu`
- `\"device state call is not gated\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s decode_primary_identity_state failed%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s no sks endpoint to send to%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity_verify: %x%s\n`
- `platform_kernel.c`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to extract passcode from ACM context (TDM?)%s\n`
- `com.apple.keystore.keybag.create`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sAssertion timeout delayed by %llu us (%llu secs)%s\n`
- `update keybag`
- `cache invalidation`
- `/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/AppleKeyStore.cpp`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s sks timeout strike %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity_migrate_first%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s no uuid%s\n`
- `AppleKeyStoreUserClient`
- `aks-log-filter`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioPerfControl is enabled: %d, %d%s\n`
- `\"failed to re-encode state\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Volume cookie mismatch, not mapping volume%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s existing mapping marked as booted from, handle:%d, flags:0x%x%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s setting new debug filter %llx -> %llx%s\n`
- `IODeviceTree:/defaults`
- `12111112122212121111111111112121221`
- `1211121212`
- `2383.40.18`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s we're on our way down and endpoint is disabled; fail request%s\n`
- `OFF`
- `process_name`
- `has_%s`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %snew timeout scheduled to: %llu%s\n`
- `cx expired`
- `fs_new_media_key`
- `com.apple.keystore.dsme_access`
- `root`
- `com.apple.keystore.fdr-access`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s un-entitled access to wku; get approval from #help-data-protection-disclosed%s\n`
- `graceperiod`
- `escrow_token_period`
- `/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/msg.c`
- `site.AppleKeyStoreCommand`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOPerfControlClient::registerDevice failed%s\n`
- `sep-booted`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s fs_get_dsme_key result: %d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Cannot set s_key (%d).%s\n`
- `secureRoot`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %scannot obtain lock assert, device is in state: %d%s\n`
- `com.apple.keystore.filevault`
- `image4-supported`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s SEP is not booted. AKS request is not processed%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s sep_endpoint() failed to initialize%s\n`
- `\"Failed to initialize SEP\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Ready for System Shutdown%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s cant get vek blob state%s\n`
- `bag_type`
- `cache flow enabled`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected length %u%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s unmapped uuid %s from bag %d%s\n`
- `sep-endpoint,sks`
- `fv_unwrap_media_key`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s set handle %d as special bag %d%s\n`
- `\"failed to encode\" @%s:%d`
- `AppleKeyStoreTest`
- `pearl-sep`
- `com.apple.keystore.opts`
- `com.apple.keystore.config.set.backoff_delay`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s result: %d, encrypted: %d%s\n`
- `site.struct encode_list_entry_t`
- `AppleKeyStoreTest::%s: terminate() failed.\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s starting (BUILT: %s %s) (%s variant %s, %s)%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s effacement notification for %d%s\n`
- `com.apple.keystore.class.d.allow`
- `\"Failed to save s_key\" @%s:%d`
- `chip-id`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s no passcode%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAppleKeyStoreUnlockWithSyncBag%s\n`
- `com.apple.keystore.info`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s Incorrect seal_data%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s sks response after %d strikes%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity change secret returned %x%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid handle? (%lld) result=%d, %s\n`
- `AppleKeyStoreCommand`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s CoreAnalytics: Failed to send CA event %d%s\n`
- `com.apple.keystore.escrow.create`
- `\"REQUIRE (%s:%d)\" @%s:%d`
- `\"Failed endpoint->setReceiveOOLBuffer() for SEP\" @%s:%d`
- `com.apple.keystore.lockassertion.time_machine`
- `key available`
- `escrow_passcode_period`
- `-apfs_shared_datavolume`
- `\"Failed endpoint->setSendOOLBuffer() for SEP (ret=%x)\" @%s:%d`
- `fv_new_media_key`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s no wkek%s\n`
- `com.apple.keystore.icsc_srp`
- `ep invalidated`
- `\"normal\"`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s existing mapping with mismatched handle %d:%d%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sanswer: %d%s\n`
- `cp_action`
- `ON`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s cant decode state%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s requested ttl is greater than max allowed%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sfailed to get cdhash of process%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sconsume global assertion%s\n`
- `site.struct volume_entry`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s missing entitlement for dsme access%s\n`
- `\"Failed to read s_key (%d).\" @%s:%d`
- `entitled_for_config_set`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s missing com.apple.keystore.access-keychain-keys%s\n`
- `passcode threshold`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid charging: %llu%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s global assertion claimed by client%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s disabling use of effaceable storage, using fake key, 0x%x%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n`
- `\"this should never happen\" @%s:%d`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %shold device assertion, type: %u%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s global assertion has been created, timeout for consumption in %llu secs%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s client process does not have keystore background processing entitlements%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sattempt to set lock assert failed%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s not entitled to switch domain%s\n`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected version %d%s\n`
- `\"unexpected call to kern_platform_get_device_id()\" @%s:%d`
- `aks-io-perf-control`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s keybagd has not registered for system keybag update notifications%s\n`
- `com.apple.applekeystore.selector.keybag_create`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdeadline has already passed, fire timer now%s\n`
- `backoff_delay`
- `acm_handle`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s allowing identical volume mapping%s\n`
- `\"Failed to read effaceable.\" @%s:%d`
- `cpx-encryption-mode`
- `device_keybag_access`
- `%s:%spid:%d,%s:%s%s%s%s%s%u:%s %supdated lock assert timer with timeout: %u, deadline: %llu%s\n`
- `com.apple.applekeystore.selector.keybag_load`

**[__TEXT.__os_log]**

- `processing(delta_id:%d): last_timestamp=0x%llx`
- `delta: %s = %x0x`
- `no matching volume bag for: handle = %d, action = %d, flags = 0x%x`
